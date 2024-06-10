from django.db import models
from users.models import CustomUser
from phonenumber_field.modelfields import PhoneNumberField
import pytz
from django.core.validators import RegexValidator



class Client(models.Model):
    client = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    address = models.TextField()
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    timezone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')
    postal_code = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^[0-9A-Za-z\s-]+$',
                message='Enter a valid postal code.'
            )
        ]
    )

class Freelancer(models.Model):
    freelancer = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    job_title = models.TextField()
    hourly_rate = models.PositiveIntegerField()
    job_description = models.TextField()
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    address = models.TextField()
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    timezone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')
    postal_code = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^[0-9A-Za-z\s-]+$',
                message='Enter a valid postal code.'
            )
        ]
    )
    



