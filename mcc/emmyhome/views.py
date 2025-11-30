import pathlib
from django.shortcuts import render
from django.http import HttpResponse

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *arg, **kwargs):


    return HttpResponse("<h1>Hello world</h1>")