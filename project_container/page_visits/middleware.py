from django.utils.timezone import localtime
from django.http import HttpRequest
from django.urls import resolve, Resolver404
from .models import PageVisit
from main.urls import urlpatterns  # Assuming you want to get URLs from the main app

class TrackPageVisitsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        # Exclude certain paths from being tracked
        excluded_paths = ['/media/', '/static/', '/supersecretadmin', '/page_visits/', 'favicon.ico']

        # Skip tracking for URLs matching the excluded paths
        if any(request.path.startswith(excluded_path) for excluded_path in excluded_paths):
            return self.get_response(request)

        # Extract app URLs from urlpatterns
        app_urls = self.get_app_urls()

        # Check if the request URL matches any of the app URLs
        try:
            match = resolve(request.path)
            if match.url_name in app_urls:
                self.track_visit(request, match)
        
        except Resolver404:
            pass  # If the URL doesn't resolve, we don't track it

        # Process the request
        response = self.get_response(request)
        return response

    def get_app_urls(self):
        """
        Get the names of URLs belonging to a specific app (from urlpatterns).
        Adjust this to fit your app's structure.
        """
        app_urls = set()  # Use a set to avoid duplicates
        for pattern in urlpatterns:
            # Ensure that the URL pattern is a valid one for the specific app
            if hasattr(pattern, 'name') and pattern.name:  # Check if it has a URL name
                app_urls.add(pattern.name)  # Add the URL name to the set
        return app_urls

    def track_visit(self, request, match):
        """
        Track the visit for a matching URL.
        """
        # Normalize the URL (remove query params and fragments if necessary)
        url = request.path.split('?')[0].split('#')[0]

        # Get other optional data like the user's IP address, User-Agent, and referer
        ip_address = self.get_client_ip(request)  # Call the method to get the client IP
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        referer = request.META.get('HTTP_REFERER', '')

        # Record the visit (for URLs that match the app URLs)
        PageVisit.objects.create(url=url, ip_address=ip_address, user_agent=user_agent, referer=referer)

    # Method to get the client's IP address
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # Take the first IP from the list
        else:
            ip = request.META.get('REMOTE_ADDR')  # Fallback to REMOTE_ADDR
        return ip
