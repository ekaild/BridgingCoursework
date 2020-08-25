from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv, name='cv'),
    path('cv/edit', views.cv_edit, {}, 'cv_edit'),
]