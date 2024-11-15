from django.shortcuts import render
from .models import PageVisit
from .decorators import permission_required_403

@permission_required_403('page_visits.view_PageVisits')
def page_visits(request):
    title = 'Page Visits'
    
    # Get total page visit count
    page_visits_count = PageVisit.objects.count()

    # Get the most popular URL and visit count using the class method
    most_popular_url, most_popular_url_count = PageVisit.get_most_popular_url_and_num_visits()

    # Get the past number of days with the visit count to get JSON data for bar chart.
    chart_data_json = PageVisit.get_past_x_day_visits(7)    
    
    # Calculate percent increase/decrease from previous day
    percentage_change_in_visits = PageVisit.get_percentage_change_in_visits()

    # Get the field names dynamically
    field_names = PageVisit.get_model_fields()

    url_total_visits = PageVisit.get_unique_url_total_visits()

    # Pass the data to the template
    context = {
        'title': title,
        
        # Chart data
        'page_visits_count': page_visits_count,
        'most_popular_url': most_popular_url,
        'most_popular_url_count': most_popular_url_count,
        'chart_data': chart_data_json,  # This contains the dynamically generated data
        'percentage_change_in_visits': percentage_change_in_visits,
        

        'unique_urls_data': PageVisit.unique_url_table(),

        'field_names': field_names,
        'url_total_visits': url_total_visits,
    }
    
    return render(request, 'page_visits/pages/page_visits.html', context)
