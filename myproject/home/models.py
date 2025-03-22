from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.hashers import check_password, make_password

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class RegistrationManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class registration_data(AbstractBaseUser):
    email = models.EmailField(max_length=50, unique=True)
    type = models.CharField(max_length=100, default='user')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Add any fields you want to be required on user creation

    def __str__(self):
        return self.email

    # username = models.CharField(max_length=50, null=False)
    # contact = models.CharField(max_length=20)
    
class counsellor_data(models.Model):
    counsellorid = models.CharField(max_length=50)
    counsellorname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    username = models.CharField(max_length=50)

class test_data(models.Model):
    username = models.EmailField()  # Make sure this is EmailField or CharField
    date = models.DateTimeField()
    testid = models.CharField(max_length=100)
    result = models.CharField(max_length=100)

class appointement_data(models.Model):
    # appointmentid = models.CharField(max_length=50)
    # counsellorid = models.CharField(max_length=50)
    # userid = models.DateField(max_length=50)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    date = models.DateField(max_length=50)
    time = models.TimeField(max_length=50)
    address = models.CharField(max_length=50)
    # result = models.DateField(max_length=50)
    status = models.CharField(max_length=50)

class StressAssessmentResponse(models.Model):
    # name = models.CharField(max_length=100)
    # email = models.EmailField()
    responses = models.JSONField()  
    submitted_at = models.DateTimeField(auto_now_add=True)

    def total_score(self):
        return sum(self.responses.values())

    def stress_level(self):
        score = self.total_score()
        if score <= 50:
            return "Low"
        elif 51 <= score <= 75:
            return "Moderate"
        else:
            return "High"