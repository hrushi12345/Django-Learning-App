from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True) # Additional field to existing User fields
    
    # Additional
    portfolioSite = models.URLField(blank=True)
    profilePic = models.ImageField(upload_to = 'ProfilePics', blank=True)

    def __str__(self):
        return self.user.username