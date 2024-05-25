from django.shortcuts import render
from .models import CarouselImage
from .models import LabMember

# Create your views here.

def home(request):
    title = 'Home'
    title_style = 'text-3xl text-uci-blue-dk mx-auto px-4 pt-2 font-semibold'
    carousel_images = CarouselImage.objects.all()
    carousel_images_with_index = [(index, image) for index, image in enumerate(carousel_images)]
    num_pics = carousel_images.count()
    context = {
        "title": title,
        "title_style": title_style,
        "carousel_images": carousel_images,
        'carousel_images_with_index': carousel_images_with_index, 
        "num_pics": num_pics
    }
    return render(request, 'pages/index.html', context)

def research(request):
    title = 'Research'
    context = {
        "title": title,
    }
    return render(request, 'pages/research.html', context)

def publications(request):
    title = 'Publications'
    context = {
        "title": title,
    }
    return render(request, 'pages/publications.html', context)

def members(request):
    title = 'members'
    # Query all lab members
    current_lab_members = LabMember.objects.filter(is_alumni=False).order_by('-id')
    
    # Pass lab members to the template
    context = {
        "title": title,
        'current_lab_members': current_lab_members,
    }
    
    # Render the template with the context
    return render(request, 'pages/members.html', context)

def alumni(request):
    title = 'alumni'
    # Query all lab members
    alumni = LabMember.objects.filter(is_alumni=True).order_by('-id')
    
    # Pass alumni to the template
    context = {
        "title": title,
        'alumni': alumni,
    }

    return render(request, 'pages/alumni.html', context)

def outreach(request):
    title = 'outreach'
    context = {
        "title": title,
    }
    return render(request, 'pages/outreach.html', context)

def funding(request):
    title = 'funding'
    context = {
        "title": title,
    }
    return render(request, 'pages/funding.html', context)

def calendar(request):
    title = 'calendar'
    context = {
        "title": title,
    }
    return render(request, 'pages/calendar.html', context)

def contact_us(request):
    title = 'Contact Us'
    context = {
        "title": title,
    }
    return render(request, 'pages/contact_us.html', context)
