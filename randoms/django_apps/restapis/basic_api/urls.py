from django.urls import path
from . import views

urlpatterns = [
    path("basics/",views.BasicsApi.as_view()),
    path("add/<int:a>/<int:b>/",views.AsmallComputation.as_view()),
    path("add2/",views.AsmallComputation2.as_view()),
]