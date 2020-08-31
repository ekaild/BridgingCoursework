from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect, render_to_response, HttpResponseRedirect
from .models import Traits
from .forms import TraitsForm
from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import reverse
from .models import Info, Skill, Educations, Job
from .forms import InfoForm, EducationsForm, JobForm, SkillForm
from django.contrib import messages

def cv(request):
    return render(request, 'cv.html', {})

def cv_edit(request, pk):
    trait = get_object_or_404(Traits, pk=pk)
    if request.method == "POST":
        form = TraitsForm(request.POST, instance=trait)
        if form.is_valid():
            trait = form.save(commit=False)
            trait.save()
            return redirect('cv_edit', pk=trait.pk)
    else:
        form = TraitsForm(instance=trait) 
    return render(request, 'cv/cv_edit.html', {'form': form})



def cv(request):
    try:
        cv_data = Info.objects.first()
        if not cv_data:
            cv_data = {}
    except:
        cv_data = {}
    return render(request, 'cv/cv.html', {'cv_data':cv_data})



def add_info(request):
    
       

    template_name='cv/add_data.html'
    title = "Add CV Info"
    context = {
        'title':title,
        'addform':InfoForm(),
    }

    if request.method == 'POST':
        addform = InfoForm(request.POST)

        if addform.is_valid():
            addform_ = addform.save(commit=False)
            addform_.owner = request.user
            addform_.save()
        
        messages.success(request, f'Data has been updated ')

        return redirect('cv:cv')

    return render(request, template_name, context)   





def edit_info(request):
    
       

    try:
        obj_ = Info.objects.filter(owner=request.user).order_by('-pk').first()
        if obj_ is None:
            messages.success(request, f'You have no previous information to edit')
            return redirect('cv:cv')
    except:
        messages.success(request, f'You have no previous information to edit')
        return redirect('cv:cv')

    template_name='cv/edit_data.html'
    title = "Edit/Update CV Info"
    context = {
        'title':title,
        'UpdateForm':InfoForm(instance=obj_),
    }

    if request.method == 'POST':
        infoform = InfoForm(data=request.POST, instance=obj_)

        if infoform.is_valid():
            infoform_ = infoform.save(commit=False)
            infoform_.owner = request.user
            infoform_.save()
        
        messages.success(request, f'Data has been updated ')

        return redirect('cv:cv')

    return render(request, template_name, context)   




def add_skill(request):
    
       

    try:
        info_obj = Info.objects.first()
    except:
        messages.success(request, f'You have no previous information to edit.')
        return redirect('cv:cv')


    template_name='cv/add_data.html'
    title = "Add Skill"
    context = {
        'title':title,
        'addform':SkillForm(),
    }

    if request.method == 'POST':
        addform = SkillForm(request.POST)

        if addform.is_valid():
            addform_ = addform.save(commit=False)
            addform_.info = info_obj
            addform_.save()
        
        messages.success(request, f'Data has been updated ')

        return redirect('cv:cv')

    return render(request, template_name, context)   



def add_education(request):
    
       

    try:
        info_obj = Info.objects.first()
    except:
        messages.success(request, f'You have no previous information to edit')
        return redirect('cv:cv')


    template_name='cv/add_data.html'
    title = "Add Education"
    context = {
        'title':title,
        'addform':EducationsForm(),
    }

    if request.method == 'POST':
        addform = EducationsForm(request.POST)

        if addform.is_valid():
            addform_ = addform.save(commit=False)
            addform_.info = info_obj
            addform_.save()
        
        messages.success(request, f'Data has been updated ')

        return redirect('cv:cv')

    return render(request, template_name, context)   




def add_job(request):
    
       

    try:
        info_obj = Info.objects.first()
    except:
        messages.success(request, f'You have no previous information to edit')
        return redirect('cv:cv')


    template_name='cv/add_data.html'
    title = "Add Education"
    context = {
        'title':title,
        'addform':JobForm(),
    }

    if request.method == 'POST':
        addform = JobForm(request.POST)

        if addform.is_valid():
            addform_ = addform.save(commit=False)
            addform_.info = info_obj
            addform_.save()
        
        messages.success(request, f'Data has been updated ')

        return redirect('cv:cv')

    return render(request, template_name, context)   



