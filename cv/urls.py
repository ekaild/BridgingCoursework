from django.urls import path
from . import views

app_name = 'cv'

urlpatterns = [
    path('', views.cv, name="cv"),
    # I tried something too complicated.
   # path('add/info/', views.add_info, name='add_info'),


   # path('add/education/', views.add_education, name='add_education'),

   # path('add/job/', views.add_job, name='add_job'),

   # path('add/skill/', views.add_skill, name='add_skill'),

]