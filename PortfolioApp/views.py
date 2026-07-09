from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import *




def DashboardPage(request):
    
    pdata = PersonalInfoModel.objects.first()
    sdata= SkillModel.objects.all()
    prdata= ProjectModel.objects.all()
    exdata= ExperienceModel.objects.all()
    edudata= EducationModel.objects.all()
    condata= ContactModel.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Send Your Message Successfully')
            return redirect('dashboard')
    else:
        form = ContactForm()


    cont = {
        'pdata': pdata,
        'sdata': sdata,
        'prdata': prdata,
        'exdata': exdata,
        'edudata': edudata,
        'condata': condata,
        'form': form

            
    }
    return render(request, 'pages/dashboard.html',cont)





@login_required
def ContacListtPage(request):
    
    data = ContactModel.objects.all()
    print(data)
    cont = {'data':data}
    return render(request, 'pages/ContacList.html', cont)








def LoginPage(request):
    if request.method == 'POST':
        form = AuthForm(request, data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('dashboard')
    else:
        form = AuthForm()
    
    cont = {
        'form': form,
        'title': 'Login Form',
        'btn':'Login',
    }
    return render(request, 'auth/BaseForm.html', cont)


@login_required
def LogoutPage(request):
    logout(request)
    messages.warning(request, 'You are Logged Out!!!')
    return redirect('dashboard')


@login_required
def PersonalInfoPage(request , id=None):
    try:
        data = PersonalInfoModel.objects.get(id=id)
    except PersonalInfoModel.DoesNotExist:
        data= None
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request, 'Personal Info Added Successfully')
            return redirect('dashboard')
    else:
        form = PersonalInfoForm(instance=data)
    
    cont = {
        'form': form,
        'title': 'Personal Info',
        'btn':'Add',
        'data':data
    }
    return render(request, 'auth/BaseForm.html',cont)



@login_required
def SkillPage(request, id=None):
    try:
        data = SkillModel.objects.get(id=id)
    except SkillModel.DoesNotExist:
        data= None

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill Added Successfully')
            return redirect('dashboard')
    else:
        form = SkillForm(instance=data)
    
    cont = {
        'form': form,
        'title': 'Skill Details',
        'btn':'Add',
    }
    return render(request, 'auth/BaseForm.html',cont)




@login_required
def ProjectPage(request, id=None):
    try:
        data = ProjectModel.objects.get(id=id)
    except ProjectModel.DoesNotExist:
        data= None
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()            
            messages.success(request, 'Project Details Added Successfully')
            return redirect('dashboard')
    else:
        form = ProjectForm(instance=data)
    
    cont = {
        'form': form,
        'title': 'Project Info',
        'btn':'Add',
    }
    return render(request, 'auth/BaseForm.html',cont)




@login_required
def ExperiencePage(request, id=None):
    try:
        data = ExperienceModel.objects.get(id=id)
    except ExperienceModel.DoesNotExist:
        data= None
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=data)
        if form.is_valid():
            form.save()            
            messages.success(request, 'Experience Details Added Successfully')
            return redirect('dashboard')
    else:
        form = ExperienceForm(instance=data)
    
    cont = {
        'form': form,
        'title': 'Experience Info',
        'btn':'Add',
    }
    return render(request, 'auth/BaseForm.html',cont)



@login_required
def EducationPage(request, id=None):
    try:
        data = EducationModel.objects.get(id=id)
    except EducationModel.DoesNotExist:
        data= None
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=data)
        if form.is_valid():
            form.save()            
            messages.success(request, 'Education Details Added Successfully')
            return redirect('dashboard')
    else:
        form = EducationForm(instance=data)
    
    cont = {
        'form': form,
        'title': 'Education Info',
        'btn':'Add',
        
    }
    return render(request, 'auth/BaseForm.html',cont)



@login_required
def ContactPage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()            
            messages.success(request, 'Contact Details Added Successfully')
            return redirect('dashboard')
    else:
        form = ContactForm()
    
    cont = {
        'form': form,
        'title': 'Contact Info',
        'btn':'Add',
    }
    return render(request, 'auth/BaseForm.html',cont)









# Create your views here.
