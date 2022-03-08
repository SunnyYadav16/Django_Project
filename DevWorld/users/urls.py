from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_profile, name='profile'),
    path('user_profile/<str:pk>', views.user_profile, name='user_profile')
]
