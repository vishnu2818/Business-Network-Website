from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

class Company(models.Model):
    company_name = models.CharField(max_length=255,null=True)
    company_description = models.CharField(max_length=255,null=True)
    logo = models.ImageField(upload_to='company_logos')
    banner_image = models.ImageField(upload_to='company_banners')
    linkedin_url = models.URLField(max_length=200)
    facebook_url = models.URLField(max_length=200)
    instagram_url = models.URLField(max_length=200)
    youtube_url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(max_length=254,null=True)
    password = models.CharField(max_length=255,null=True)

    def check_password(self, raw_password):
        """Checks if the provided password matches the stored hashed password."""
        return check_password(raw_password, self.password)