from django.db import models
from django.utils import timezone
from django.db.models import Count, Sum
from django.utils import timezone
from datetime import timedelta
import json
# Create your models here.

class PageVisit(models.Model):
    # URL of the page that was visited
    url = models.CharField(max_length=2000)  # Should be long enough to store full URLs
    # Timestamp of when the page was visited
    visited_at = models.DateTimeField(default=timezone.now)
    # Optional: Store the IP address of the visitor
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    # Optional: Store the User-Agent string to identify the browser/device
    user_agent = models.CharField(max_length=512, null=True, blank=True)
    # Optional: You can also store the referring URL
    referer = models.CharField(max_length=2000, null=True, blank=True)
    
    # Count the number of visits to each URL
    visit_count = models.IntegerField(default=1)
    
    def __str__(self):
        return f"Visit to '{self.url}' on {self.get_local_time()}"

    # Optional: If you want to return time in the user's local timezone:
    def get_local_time(self):
        # Convert the stored UTC time to the local time zone
        local_time = timezone.localtime(self.visited_at)
        return local_time.strftime('%b %d, %Y - %I:%M %p')  # Format example: 'Nov 12, 2024 - 02:48 PM'

    @classmethod
    def get_model_fields(cls):
        # Get the field names (attributes) of the model dynamically
        field_names = [field.name for field in cls._meta.fields]
        return field_names

    @classmethod
    def get_model_fields(cls):
        # Return the fields you want to dynamically retrieve (e.g., `url` and `visit_count`)
        return ['url', 'visit_count']

    @classmethod
    def get_unique_url_total_visits(cls):
        # Group by 'url' and sum 'visit_count' for each unique URL
        url_total_visits = PageVisit.objects.values('url')\
            .annotate(total_visits=Sum('visit_count'))\
            .order_by('url')  # Optionally, you can order by the URL
        return url_total_visits

    @classmethod
    def unique_url_table(cls):
        # Fetch the unique URLs along with their attributes
        unique_urls = PageVisit.objects.values_list('url', flat=True).distinct()
        return unique_urls

    @classmethod
    def get_percentage_change_in_visits(cls):
        """
        Calculates the percentage change in page visits between today and yesterday.
        If there's no visits for yesterday, return 0 (no change).
        """
        # Get today's date (local time) and yesterday's date
        today = timezone.localtime(timezone.now()).date()
        yesterday = today - timedelta(days=1)

        # Get total visits for today
        visits_today = cls.objects.filter(visited_at__date=today).aggregate(total_visits_today=Sum('visit_count'))['total_visits_today'] or 0

        # Get total visits for yesterday
        visits_yesterday = cls.objects.filter(visited_at__date=yesterday).aggregate(total_visits_yesterday=Sum('visit_count'))['total_visits_yesterday'] or 0

        # Avoid division by zero error
        if visits_yesterday == 0:
            # If there were no visits yesterday, we cannot calculate the percentage change
            return 0  # No change or 100% increase depending on context

        # Calculate percentage change: ((today - yesterday) / yesterday) * 100
        percentage_change = ((visits_today - visits_yesterday) / visits_yesterday) * 100

        return round(percentage_change)

    @classmethod
    def get_most_popular_url_and_num_visits(cls):
        # Get the most popular URL, with safe handling for None
        most_popular_url = PageVisit.objects.values('url')\
            .annotate(total_visits=Sum('visit_count'))\
            .order_by('-total_visits')\
            .first()

        if most_popular_url:
            most_popular_url_value = most_popular_url['url']
            most_popular_url_count = most_popular_url['total_visits']
        else:
            most_popular_url_value = None
            most_popular_url_count = 0

        return most_popular_url_value, most_popular_url_count

    @classmethod
    def get_past_x_day_visits(cls, x: int = 5):
        '''
        Description
        -----------
        Gets the current date calculates previous `x` number of dates and returns chart data for a bar chart.

        Args
        ----
            `x`: The variable that specifies the previous number of dates to go back

        Returns
        ------
            `json`: Data for an Apexchart bar chart is returned.
        '''
        
        # Get the current date (in local timezone)
        today = timezone.localtime(timezone.now()).date()

        # Get the past x days (ensure that the range includes only the last x complete days)
        past_x_days = [today - timedelta(days=i) for i in range(x)]

        # Query the database for the visit counts on each of the past x days
        page_visits_per_day = PageVisit.objects.filter(visited_at__date__in=past_x_days) \
            .values('visited_at__date') \
            .annotate(total_visits=Count('id')) \
            .order_by('visited_at__date')

        # Format the data for the chart
        chart_data = []
        for day in reversed(past_x_days):  # Reverse the list so the most recent date is last
            # Find the record for the current day
            visits_for_day = next((item for item in page_visits_per_day if item['visited_at__date'] == day), None)
            
            # If no visits for this day, set the count to 0
            visits_count = visits_for_day['total_visits'] if visits_for_day else 0
            
            # Add the formatted data to the list
            chart_data.append({
                'x': day.strftime('%b. %d'),  # Format the date like 'Nov. 6'
                'y': visits_count,
            })

        # Ensure no future dates show up in the chart data
        chart_data = [data for data in chart_data if data['x'] <= today.strftime('%b. %d')]
        return json.dumps(chart_data)
