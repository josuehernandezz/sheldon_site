# app/context_processors.py

from .models import HiringPosition

def navbar_context(request):
    # Removed Outreach
    # nav_btn_name = ["Research", "Publications", "Members", "Outreach", "Funding", "Calendar", "Contact Us"]
    
    # Removed Contact Us
    # nav_btn_name = ["Research", "Publications", "Members", "Funding", "Calendar", "Contact Us"]
    
    
    # Removed Outreach
    # nav_url = ["research", "publications", "members", "outreach", "funding", "calendar", "contact-us"]
    
    # Removed Contact Us
    # nav_url = ["research", "publications", "members", "funding", "calendar", "contact-us"]
    
    nav_item = ["Research", "Publications", "Members", "Funding", "Calendar"]
    nav_url = ["research", "publications", "members", "funding", "calendar"]
    
    if HiringPosition.objects.exists():
        nav_item.append("Postdoc Positions")
        nav_url.append("positions")

    nav_info = zip(nav_item, nav_url)

    member_type = ["Current Members", "Alumni"]
    member_urls = ["members", "alumni"]
    member_dropdown_items = zip(member_type, member_urls)

    return {
        "nav_info": nav_info,
        "member_dropdown_items" : member_dropdown_items
    }
