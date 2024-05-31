from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django_countries.fields import CountryField

class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(_("email address"), unique=True)
    is_client = models.BooleanField('client status', default=False)
    is_freelancer = models.BooleanField('freelancer status', default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    country = CountryField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    def __str__(self):
        return self.email





