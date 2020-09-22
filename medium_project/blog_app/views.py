from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse 
from django.http import JsonResponse

# Create your views here.

def root(request):
  return HttpResponse("Hello everyone")


def index(request):
  return HttpResponse('place holder to later display a list of all blog')

def new(request):
  return HttpResponse("Place holder to display a new form to create a new blog!")

def create(request):
  return HttpResponseRedirect(reverse(root))

def show(request, number):
  return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request, number):
  return HttpResponse(f"placeholder to edit blog number {number}")

def destroy(request, number):
  return HttpResponseRedirect(reverse(index))

def json_return(request):
  return JsonResponse(
    {
      "Title": "Durer Golpo",
     "Content": "Lyirics"
     }
     
     )