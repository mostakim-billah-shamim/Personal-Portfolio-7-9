from django.urls import path
from .views import *

urlpatterns = [
    path('', DashboardPage, name='dashboard'),
    path('contact/', ContacListtPage, name='contact'),

    path('login/', LoginPage, name='login'),
    path('logout/', LogoutPage, name='logout'),

    path('personal/', PersonalInfoPage, name='personal'),
    path('editPersonal/<str:id>/', PersonalInfoPage, name='editPersonal'),

    path('skill/', SkillPage, name='skill'),
    path('editSkill/<str:id>/', SkillPage, name='editSkill'),

    path('project/', ProjectPage, name='project'),
    path('editProject/<str:id>/', ProjectPage, name='editProject'),

    path('experience/', ExperiencePage, name='experience'),
    path('editExperience/<str:id>/', ExperiencePage, name='editExperience'),

    path('education/', EducationPage, name='education'),
    path('editEducation/<str:id>/', EducationPage, name='editEducation'),

    path('contact/', ContactPage, name='contact'),
]