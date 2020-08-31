from django.db import models
from django.conf import settings
from django.utils import timezone
from django.conf import settings
from django.urls import reverse

class Traits(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title




 #This is redundant! I wanted to make it more complicated but got stuck so I made it simple instead.
class Info(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)



    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    overview = models.TextField()
    locality = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    emails = models.EmailField()
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    def __str__(self):
        return f"{self.full_name()}"
    



class Educations(models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    school_url = models.URLField('School URL')
    start_date = models.DateField()
    finish_date = models.DateField()
    summary = models.TextField()
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"


class Job(models.Model):
    info                = models.ForeignKey(Info, on_delete=models.CASCADE)
    company             = models.CharField(max_length=255)
    location            = models.CharField(max_length=255)
    title               = models.CharField(max_length=255)
    company_url         = models.URLField('Company URL', blank=True)
    description         = models.TextField(blank=True)
    start_date          = models.DateField()
    finish_date         = models.DateField()
    is_current          = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.company}"


class Skill(models.Model):
    info  = models.ForeignKey(Info, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=255)
    skill_detail = models.TextField()
    skill_url = models.URLField('Skill URL',null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

