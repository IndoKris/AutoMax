from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from localflavor.in_.models import INStateField
from .utils import user_directory_path

class Location(models.Model):
    address_1 = models.CharField(max_length=128, blank=True)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=68)
    state = INStateField()
    zip_code = models.CharField(
        max_length=6,
        blank=True,
        validators=[RegexValidator(r'^\d{6}$', 'Enter a 6-digit PIN code.')],
    )

    def __str__(self):
        return f"{self.city}, {self.state}"


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    bio = models.CharField(max_length=140, blank=True)
    phone_number = models.CharField(
        max_length=10,
        blank=True,
        validators=[RegexValidator(r'^\d{10}$', 'Enter a 10-digit phone number.')],
    )
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"