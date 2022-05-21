from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from .choices import *

# Create your models here.
class User(AbstractUser, models.Model):
    password = models.CharField(max_length=100, default='12345678')
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True, default='my_name', unique=True)
    image = models.ImageField(default='users_images/user_image_default.png', upload_to='users_images/')
    email = models.EmailField(unique=True)
    experience = models.CharField(max_length=400, blank=True)
    enterprise = models.BooleanField(default=False)
    if enterprise:
        username = models.CharField(max_length=50, blank=True, null=True, default='enterprise', unique=True)
        enterprise_description = models.CharField(max_length=500, blank=True, null=True, default='none', unique=False)
    def __str__(self):
        return f"{self.username}"
    def serialize(self):
        return {
            "id":              self.id,
            "first_name":      self.first_name,
            "last_name":       self.last_name,
            "username":        self.username,
            "image":        f'{self.image}',
            "email":        f'{self.email}',
            "experience":   f'{self.experience}',
        }

class JobRegister(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=3000)
    minimum_salary = models.BigIntegerField(default=0000)
    maximum_salary = models.BigIntegerField(default=0000)
    business_name = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=TECH
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='user_image_default.png', upload_to='jobs_images/%m')

    def serialize(self):
        return {
            "id":               self.id,
            "title":            self.title,
            "business_name":    self.business_name.username,
            "timestamp":        self.timestamp,
            "image":         f'{self.image}',
        }


class RegisterUserInJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(JobRegister, on_delete=models.CASCADE)
    situation = models.CharField(default='Under analysis', max_length=50)

    def __str__(self):
        return f"{self.id}: {self.user} => {self.job.id}"

    def serialize(self):
        return {
            "user_id": self.user.id,
            "job_id": self.job.id,
            "situation": self.situation
        }


class ClosedJobs(models.Model):
    ex_id_job = models.IntegerField(default=0)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=3000)
    business_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='business_name')
    closed_in = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=False, default='2003-03-04')
    image = models.ImageField(default='user_image_default.png', upload_to='jobs_images/%m')
    hired = models.IntegerField(default=0)

    def serialize(self):
        return {
            "id":               self.id,
            "title":            self.title,
            "business_name":    self.business_name.username,
            "closed_in":        self.closed_in,
            "timestamp":        self.timestamp,
            "image":         f'{self.image}',
            "hired":            self.hired,

        }


class UsersHired(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_hired")
    job = models.ForeignKey(ClosedJobs, on_delete=models.CASCADE)
    enterprise = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}: {self.user} => {self.job.id}"

    def serialize(self):
        return {
            "user_id": self.user.id,
            "job_id": self.job.id,
            "enterprise": self.enterprise.username
        }


allModels = [
    User,
    JobRegister,
    RegisterUserInJob,
    ClosedJobs,
    UsersHired,
]
