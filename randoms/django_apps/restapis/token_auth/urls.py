from django.urls import path
from . import views
#obtain user token
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("hello/",views.HelloView.as_view()),
    path("register/",obtain_auth_token,name="register"),
]

