from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return  HttpResponse("there is nothing here")

def firstProblem(request):
    return  HttpResponse("Here you go! Matching socks!")
# meets requirements for both things.

def problemTwo(request):
    return  HttpResponse(" Ren and Stimpy Forever!")
