from django.urls import path
from . import views

urlpatterns = [
    path(r'api/', views.get_info, name='get_info'),
]
