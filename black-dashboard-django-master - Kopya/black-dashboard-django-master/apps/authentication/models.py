from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username
