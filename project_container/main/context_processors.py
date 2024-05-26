# app/context_processors.py

def navbar_context(request):
    nav_btn_name = ["Research", "Publications", "Members", "Outreach", "Funding", "Calendar", "Contact Us"]
    nav_url = ["research", "publications", "members", "outreach", "funding", "calendar", "contact-us"]
    nav_info = zip(nav_btn_name, nav_url)

    member_names = ["Current Members", "Alumni"]
    member_urls = ["members", "alumni"]
    member_dropdown_items = zip(member_names, member_urls)

    return {
        "nav_info": nav_info,
        "member_dropdown_items" : member_dropdown_items
    }
