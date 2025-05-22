# app/context_processors.py

from .models import HiringPosition, PostDocHelpLink
from datetime import datetime

def navbar_context(request):
    nav_item = ["Research", "Publications", "Members", "Funding", "Calendar"]
    nav_url = ["research", "publications", "members", "funding", "calendar"]
    
    if HiringPosition.objects.exists() or PostDocHelpLink.objects.exists():
        nav_item.append("Work With Us")
        nav_url.append("positions")

    nav_info = zip(nav_item, nav_url)

    member_type = ["Current Members", "Alumni"]
    member_urls = ["members", "alumni"]
    member_dropdown_items = zip(member_type, member_urls)

    return {
        "nav_info": nav_info,
        "member_dropdown_items" : member_dropdown_items
    }

def global_settings(request):
    return {
        "CURRENT_YEAR": datetime.now().year,  # Dynamic current year
    }
