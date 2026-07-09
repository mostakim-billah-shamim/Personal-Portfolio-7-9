from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import AuthenticationForm




class AuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i in self.fields.values():
            i.widget.attrs.update({'class': 'form-control'})
    
        

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfoModel
        fields = '__all__'
        exclude = ['user']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i in self.fields.values():
            i.widget.attrs.update({'class': 'form-control'})
    
        


class SkillForm(forms.ModelForm):
    class Meta:
        model = SkillModel
        fields = '__all__'

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i in self.fields.values():
            i.widget.attrs.update({'class': 'form-control'})
    
        


class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields = '__all__'

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i in self.fields.values():
            i.widget.attrs.update({'class': 'form-control'})
    
        



class ExperienceForm(forms.ModelForm):
    class Meta:
        model = ExperienceModel
        fields = '__all__'

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i in self.fields.values():
            i.widget.attrs.update({'class': 'form-control'})
    
        


class EducationForm(forms.ModelForm):
    class Meta:
        model = EducationModel
        fields = '__all__'

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i in self.fields.values():
            i.widget.attrs.update({'class': 'form-control'})
    
    


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i in self.fields.values():
            i.widget.attrs.update({'class': 'form-control'})
    
        


