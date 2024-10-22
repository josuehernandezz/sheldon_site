from django.shortcuts import render
from .models import CarouselImage, LabMember, Publication, GroupPhoto, ContentImage, Card, Funding, FundingImg, ResearchSection

# Create your views here.

def home(request):
    title = 'Home'
    title_style = 'text-3xl text-uci-blue-dk mx-auto px-4 pt-2 font-semibold'
    content_images = ContentImage.objects.all()[:2]
    cards = Card.objects.all()
    carousel_images = CarouselImage.objects.all()
    carousel_images_with_index = [(index, image) for index, image in enumerate(carousel_images)]
    latest_group_photo = GroupPhoto.objects.latest('id')
    num_pics = carousel_images.count()
    context = {
        "title": title,
        "title_style": title_style,
        "content_images": content_images,
        "carousel_images": carousel_images,
        "cards": cards,
        'carousel_images_with_index': carousel_images_with_index, 
        "latest_group_photo": latest_group_photo,
        "num_pics": num_pics
    }
    return render(request, 'pages/index.html', context)

def research(request):
    research_sections = ResearchSection.objects.all()
    title = 'Research'
    context = {
        "research_sections": research_sections,
        "title": title,
    }
    return render(request, 'pages/research.html', context)

def publications(request):
    title = 'Publications'
    publications = Publication.objects.all().order_by('-publication_number')
    context = {
        "title": title,
        "publications": publications,
    }
    return render(request, 'pages/publications.html', context)

def members(request):
    title = 'members'
    current_lab_members = LabMember.objects.filter(is_alumni=False).order_by('year_joined')
    principal_investigator = LabMember.objects.filter(title='Principal Investigator')[0]
    context = {
        "title": title,
        'current_lab_members': current_lab_members,
        'principal_investigator': principal_investigator
    }
    
    # Render the template with the context
    return render(request, 'pages/members.html', context)

def alumni(request):
    title = 'alumni'
    # Query all lab members
    post_docs = LabMember.objects.filter(is_alumni=True).filter(position='PD').order_by('-year_joined')
    grads = LabMember.objects.filter(is_alumni=True).filter(position='GR').order_by('-year_joined')
    undergrads = LabMember.objects.filter(is_alumni=True).filter(position='UG').order_by('-year_joined')
    high_schoolers = LabMember.objects.filter(is_alumni=True).filter(position='HS').order_by('-year_joined')

    # Pass alumni to the template
    context = {
        'title': title,
        'post_docs': post_docs,
        'grads': grads,
        'undergrads': undergrads,
        'high_schoolers': high_schoolers,
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
    funding = Funding.objects.all()
    fund_img = FundingImg.objects.all()[0]
    context = {
        "title": title,
        "funding": funding,
        "fund_img": fund_img,
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
