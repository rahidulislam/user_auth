from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """Custom User Manager"""

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_customer(self, email, password=None, **extra_fields):
        """
        Creates and saves a Customer with the given email and password.
        """
        extra_fields.setdefault('role', 3)
        user = self.create_user(email, password=password, **extra_fields)
        return user
    
    def create_staff(self, email, password=None, **extra_fields):
        """
        Creates and saves a Customer with the given email and password.
        """
        extra_fields.setdefault('role', 2)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Staff must have is_staff=True.')
        user = self.create_user(email, password=password, **extra_fields)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 1)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password=password, **extra_fields)
    