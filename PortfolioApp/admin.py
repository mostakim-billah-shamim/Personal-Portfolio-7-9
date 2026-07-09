from django.contrib import admin
from .models import *

admin.site.register([PersonalInfoModel, SkillModel, ProjectModel, ExperienceModel, EducationModel, ContactModel ])

# Register your models here.
