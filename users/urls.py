from django.urls import path,include
from . import views

urlpatterns = [  # Add this line
    path('',views.register,name='register'),
    path('logout/',views.logout, name='logout'),
    path('profile/',views.profile, name='profile'),
    path('edit-profile/',views.edit_profile, name='edit-profile'),
]