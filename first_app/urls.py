from django.urls import path,include
from django.contrib import admin
from .import views

urlpatterns = [
    path('signup',views.signup , name='signup'),
    path('login/',views.user_login , name='user_login'),
    path('logout/',views.user_logout , name='user_logout'),
    path('profile/',views.profile , name='profile'),
    path('profile/edit1/pass_change1',views.pass_change1 , name='pass_change1'),
    path('profile/edit2/pass_change2',views.pass_change2 , name='pass_change2'),
    path('profile/edit/',views.edit_profile , name='edit_profile'),
]
