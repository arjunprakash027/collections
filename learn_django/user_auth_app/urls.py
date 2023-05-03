from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('login',views.login_user,name='login'),
    path('onlyloggedin',views.onlyloggedin,name='onlyloggedin'),
    path('logout',views.logout_user,name='logout'),
    path('index',views.index,name='index')
]

