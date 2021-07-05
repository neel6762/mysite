from django.urls import path
from . import views
# url patterns

urlpatterns = [
    path('', views.index, name='index'),
    path('education/', views.education, name='education'),
    path('projects/', views.projects, name='projects'),
]