from django import forms

from .models import Info, Educations, Skill, Job, Traits



class TraitsForm(forms.ModelForm):

    class Meta:
        model = Traits
        fields = ('title', 'text')

#Not used, prototypical
class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        exclude = ('owner',)


class EducationsForm(forms.ModelForm):
    class Meta:
        model = Educations
        exclude = ('info',)

        widgets = {
        'start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'finish_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),

    }


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('info',)

        widgets = {
        'start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'finish_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),

    }


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = ('info',)
