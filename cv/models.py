from django.conf import settings
from django.db import models
from django.utils import timezone

class Overview(models.Model):
    text = models.TextField()

class Info(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    emails = models.EmailField()
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    
    def full_name(self):
        return " ".join([self.first_name, self.last_name])

class Educations(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    school_url = models.URLField('School URL')
    start_date = models.DateField()
    finish_date = models.DateField()
    summary = models.TextField()
    is_current = models.BooleanField(default=False)

class Job(models.Model):
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    company_url = models.URLField('Company URL', blank=True)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    finish_date = models.DateField()
    is_current = models.BooleanField(default=False)

class Accomplishment(models.Model):
    description = models.TextField()

class Skillset(models.Model):
    name = models.CharField(max_length=255)

class Skill(models.Model):
    name = models.CharField(max_length=255)
    skill_url = models.URLField('Skill URL', blank=True)

class Post(models.Model):
    text = models.TextField(default='Placeholder text')
    title = models.CharField(max_length=255, default='Placeholder title')
