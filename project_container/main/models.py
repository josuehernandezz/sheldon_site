from django.db import models
from django.db.models.signals import pre_delete
from django.db.models.signals import pre_save
from django.dispatch import receiver
import os

content_img = 'content_images/'
card_img = 'card_img/'
research_section_image_path = 'research_section_img/'
carousel_img_path = 'carousel_images/'
lab_member_img_path = 'lab_member_images/'

# Has Image
class ContentImage(models.Model):
    alt = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to=content_img, blank=False, null=False)

    def delete(self):
        self.image.delete()
        super().delete()

    def __str__(self):
        return self.alt if self.alt else "Content Image"

# Has Image
class Card(models.Model):
    title = models.CharField(max_length=300, blank=False, null=False)
    alt = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to=card_img, blank=False, null=False)
    description = models.TextField(max_length=2000, blank=False, null=False)

    def delete(self):
        self.image.delete()
        super().delete()

    def __str__(self):
        return self.alt if self.alt else "Card Image"

# Has Image
class CarouselImage(models.Model):
    alt = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to=carousel_img_path, blank=False, null=False)

    def delete(self):
        self.image.delete()
        super().delete()

    def __str__(self):
        return self.alt if self.alt else "Carousel Image"

class Funding(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    funding_source = models.CharField(max_length=2000, blank=False, null=False)
        
    def __str__(self):
        return self.name
    
# Has Image
class FundingImg(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    image = models.ImageField(upload_to=content_img, blank=False, null=False)

    def delete(self):
        self.image.delete()
        super().delete()

    def __str__(self):
        return self.name

# Has Image
class GroupPhoto(models.Model):
    name = models.CharField(max_length=1000, blank=False, null=False)
    image = models.ImageField(upload_to='group_photo/', blank=False, null=False)

    def delete(self):
        self.image.delete()
        super().delete()

    def str(self):
        return self.name

# Has Image
class LabMember(models.Model):
    TITLES = [
        ('Undergraduate', 'Undergraduate'),
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

    def delete(self):
        self.image.delete()
        super().delete()

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

# Has Image
class ResearchSection(models.Model):
    title = models.CharField(max_length=1000, blank=False, null=False)
    research_summary = models.TextField(max_length=10000, blank=False, null=False)
    image = models.ImageField(upload_to=research_section_image_path, blank=False, null=False)

    def delete(self):
        self.image.delete()
        super().delete()

    def __str__(self):
        return self.title

@receiver(pre_save)
def delete_old_image(sender, instance, **kwargs):
    # Check if the model has an 'image' field
    if hasattr(instance, 'image'):
        if instance.pk:  # If the instance already exists
            old_instance = sender.objects.get(pk=instance.pk)

            # Check if the image field is being cleared
            if old_instance.image and not instance.image:
                if os.path.isfile(old_instance.image.path):
                    os.remove(old_instance.image.path)  # Delete the old file
            
            # Check if a new image is being uploaded
            elif old_instance.image and instance.image and old_instance.image != instance.image:
                if os.path.isfile(old_instance.image.path):
                    os.remove(old_instance.image.path)  # Delete the old file

pre_save.connect(delete_old_image, sender=ContentImage)
pre_save.connect(delete_old_image, sender=Card)
pre_save.connect(delete_old_image, sender=CarouselImage)
pre_save.connect(delete_old_image, sender=FundingImg)
pre_save.connect(delete_old_image, sender=GroupPhoto)
pre_save.connect(delete_old_image, sender=ResearchSection)

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
