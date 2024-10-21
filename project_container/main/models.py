from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os

content_img = 'content_images/'
card_img = 'card_img/'
research_section_image_path = 'research_section_img/'
carousel_img_path = 'carousel_images/'
lab_member_img_path = 'lab_member_images/'

class ContentImage(models.Model):
    image = models.ImageField(upload_to=content_img, null=False, blank=False)
    alt = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.alt if self.alt else "Content Image"

class Card(models.Model):
    image = models.ImageField(upload_to=card_img, null=False, blank=False)
    title = models.CharField(max_length=300, blank=False, null=False)
    description = models.CharField(max_length=2000, blank=False, null=False)
    alt = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.alt if self.alt else "Card Image"

class CarouselImage(models.Model):
    image = models.ImageField(upload_to=carousel_img_path, null=False, blank=False)
    alt = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.alt if self.alt else "Carousel Image"

class LabMember(models.Model):
    TITLES = [
        ('MS', 'Masters'),
        ('Ph.D Student', 'Ph.D Student'),
        ('Ph.D Candidate', 'Ph.D Candidate'),
        ('Ph.D', 'Ph.D'),
        ('Principal Investigator', 'Principal Investigator')
    ]

    POSITION_CHOICES = [
        ('HS', 'High School'),
        ('UG', 'Undergraduate'),
        ('GR', 'Graduate'),
        ('PD', 'Post Doc'),
    ]
    name = models.CharField(max_length=100, blank=False, null=False)
    title = models.CharField(max_length=22, choices=TITLES, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=lab_member_img_path, blank=True, null=True)
    year_joined = models.PositiveIntegerField(blank=False, null=True)
    year_finished = models.PositiveIntegerField(blank=True, null=True)
    position = models.CharField(max_length=2, choices=POSITION_CHOICES, blank=True, null=True)
    is_alumni = models.BooleanField(null=True, blank=False)
    employer = models.CharField(max_length=350, blank=True, null=True)

    def __str__(self):
        return self.name

class Publication(models.Model):
    name = models.CharField(max_length=1000, blank=False, null=True)
    publication_number = models.PositiveIntegerField(blank=False, null=True, unique=True)
    authors = models.CharField(max_length=1000, blank=False, null=False)
    title = models.CharField(max_length=1000, blank=False, null=False)
    url = models.CharField(max_length=1000, blank=True, null=True)
    journal = models.CharField(max_length=1000, blank=True, null=True)
    year = models.PositiveBigIntegerField(blank=True, null=True)
    volume = models.PositiveBigIntegerField(blank=True, null=True)
    issue = models.PositiveBigIntegerField(blank=True, null=True)
    pages = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.name

class GroupPhoto(models.Model):
    name = models.CharField(max_length=1000, blank=False, null=False)
    image = models.ImageField(upload_to='group_photo/', blank=False, null=False)

    def delete(self):
        self.image.delete()
        super().delete()

class Funding(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    funding_source = models.CharField(max_length=2000, blank=False, null=False)
        
    def __str__(self):
        return self.name
    
class FundingImg(models.Model):
    image = models.ImageField(upload_to=content_img, blank=False, null=False)
    name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name

class ResearchSection(models.Model):
    title = models.CharField(max_length=1000, blank=False, null=False)
    research_summary = models.TextField(max_length=10000, blank=False, null=False)
    image = models.ImageField(upload_to=research_section_image_path, blank=False, null=False)

    def __str__(self):
        return self.title

# Define a signal receiver function to delete associated image files
@receiver(pre_delete)
def delete_related_image_files(sender, instance, **kwargs):
    # Check if the sender has an image field
    if any(isinstance(field, models.ImageField) for field in sender._meta.fields):
        # Get the name of the image field
        image_field_name = next(field.name for field in sender._meta.fields if isinstance(field, models.ImageField))
        # Get the path of the image
        image_path = getattr(instance, image_field_name)
        # Delete the image file if it exists
        if image_path:
            if os.path.isfile(image_path.path):
                os.remove(image_path.path)

# from  .pub_data import publications_data

# # Create Publication instances
# publications_instances = []
# for data in publications_data:
#     publication_instance = Publication(
#         name=data.get('name'),
#         publication_number=data.get('publication_number'),
#         authors=data.get('authors'),
#         title=data.get('title'),
#         journal=data.get('journal'),
#         year=data.get('year'),
#         volume=data.get('volume'),
#         pages=data.get('pages'),
#         url=data.get('url')
#     )
#     publications_instances.append(publication_instance)

# # Bulk create the instances
# Publication.objects.bulk_create(publications_instances)

# # Output success message
# print("Publications added successfully.")
