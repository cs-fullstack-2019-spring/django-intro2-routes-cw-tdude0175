from django.urls import path

from . import views

urlpatterns = \
    [
        path('',views.index, name = 'index'), #added for basic entry
        path('gogetthegood/',views.firstProblem, name = "problem one"),
        path('happyhappyjoyjoy',views.problemTwo, name = "problem2")
    ]