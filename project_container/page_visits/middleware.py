from django.utils.timezone import localtime
from django.http import HttpRequest
from .models import PageVisit

class TrackPageVisitsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        # print('request', request.META)
        # Exclude certain paths from being tracked
        excluded_paths = ['/media/', '/static/', '/supersecretadmin', '/page_visits/', 'favicon.ico']
        
        # Skip tracking for URLs matching the excluded paths
        if any(request.path.startswith(excluded_path) for excluded_path in excluded_paths):
            return self.get_response(request)

        # Normalize the URL (remove query params and fragments if necessary)
        url = request.path.split('?')[0].split('#')[0]

        # Get other optional data like the user's IP address, User-Agent, and referer
        ip_address = self.get_client_ip(request)  # Call the method to get the client IP
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        referer = request.META.get('HTTP_REFERER', '')

        # Record the visit (for URLs that are not excluded)
        PageVisit.objects.create(url=url, ip_address=ip_address, user_agent=user_agent, referer=referer)
        # Process the request
        response = self.get_response(request)
        return response

    # Method to get the client's IP address (moved outside the class)
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # Take the first IP from the list
        else:
            ip = request.META.get('REMOTE_ADDR')  # Fallback to REMOTE_ADDR
        return ip
