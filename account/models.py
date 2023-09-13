from django.db import models
from django.contrib.auth.models import AbstractUser
from account.managers import UserManager
from user_auth.base import TimeStamp

# Create your models here.


class User(AbstractUser):
    SUPER_ADMIN = 1
    STAFF = 2
    CUSTOMER = 3
      
    ROLE_CHOICES = (
        (SUPER_ADMIN, 'SuperAdmin'),
        (STAFF, 'Staff'),
        (CUSTOMER, 'Customer'),


    )
    
    username = None
    email = models.EmailField(unique=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Profile(TimeStamp):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')

    mobile = models.CharField(max_length=20)
    address = models.TextField()
    profile_image = models.ImageField(upload_to="profile/", blank=True)

    def __str__(self):
        return self.user.email