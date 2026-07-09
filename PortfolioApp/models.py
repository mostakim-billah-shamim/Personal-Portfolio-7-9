from django.db import models
from django.contrib.auth.models import User


class PersonalInfoModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=120, null=True)
    bio = models.TextField(null=True)
    photo = models.ImageField(upload_to='media/profile', null=True, blank=True)
    phone = models.CharField(max_length=35, null=True)
    email = models.CharField(max_length=50, null=True)
    linkedin = models.CharField(max_length=100, null=True)
    github = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name





class SkillModel(models.Model):
    name = models.CharField(max_length=120, null=True)
    level = models.IntegerField(default=0)

    def __str__(self):
        return self.name




class ProjectModel(models.Model):
    title = models.CharField(max_length=120, null=True)
    description = models.TextField(null=True)
    language = models.CharField(max_length=120, null=True)
    github_repo = models.CharField(max_length=100, null=True)
    live_link = models.CharField(max_length=100, null=True)
    photo = models.ImageField(upload_to='media/project', null=True, blank=True)

    def __str__(self):
        return self.title





class ExperienceModel(models.Model):
    company = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)
    duration = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.company





class EducationModel(models.Model):
    degree = models.CharField(max_length=100, null=True)
    institute = models.CharField(max_length=100, null=True)
    year = models.DateField(null=True)

    def __str__(self):
        return self.degree





class ContactModel(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=80, null=True)
    phone = models.CharField(max_length=20, null=True)
    message = models.TextField(null=True)
    time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name



# Create your models here.
