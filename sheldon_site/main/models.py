from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os

carousel_img_path = 'carousel_images/'
lab_member_img_path = 'lab_member_images/'

class CarouselImage(models.Model):
    image = models.ImageField(upload_to=carousel_img_path, null=False, blank=False)
    alt = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.alt if self.alt else "Carousel Image"

class LabMember(models.Model):
    POSITION_CHOICES = [
        ('HS', 'High School'),
        ('UG', 'Undergraduate'),
        ('GR', 'Graduate'),
        ('AL', 'Alumni'),
        ('PI', 'Principle Investigator')
    ]
    TITLES = [
        ('Ph.D Student', 'Ph.D Student'),
        ('Ph.D Candidate', 'Ph.D Candidate'),
        ('Ph.D', 'Ph.D'),
        ('Principle Investigator', 'Principle Investigator')
    ]

    name = models.CharField(max_length=100, blank=False, null=False)
    title = models.CharField(max_length=22, choices=TITLES, null=True, blank=False)
    email = models.EmailField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=lab_member_img_path, blank=True, null=True)
    year_joined = models.PositiveIntegerField()
    position = models.CharField(max_length=2, choices=POSITION_CHOICES)
    is_alumni = models.BooleanField(null=True, blank=False)

    def __str__(self):
        return self.name

class Publication(models.Model):
    authors = models.CharField(max_length=1000, blank=False, null=False)
    title = models.CharField(max_length=1000, blank=False, null=False)
    url = models.CharField(max_length=1000, blank=False, null=False)
    year = models.PositiveBigIntegerField()
    journal = models.CharField(max_length=1000, blank=False, null=False)




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
