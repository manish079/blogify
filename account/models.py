from django.db import models
from cores.models import CoreModel

class About(CoreModel):
    about_heading = models.CharField(max_length=25)
    about_description = models.TextField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.about_heading
    

class SocialLink(CoreModel):
    platform = models.CharField(max_length=25)
    link = models.URLField(max_length=100)
  
    def __str__(self):
        return self.platform