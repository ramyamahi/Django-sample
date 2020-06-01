# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

import datetime

import requests

# Create your views here.

def hello(request):
    text = """<h1>Welcome </h1>"""
    return HttpResponse(text)



def get_data(request, id):
    text = "Article Id is: %s"%id
    return HttpResponse(text)


def template_example(request):
    today = datetime.datetime.now().date()
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return render(request, "hello.html", {"today":today, "days_of_week": daysOfWeek})


def get_json_data(request):
   # get the list of todos
   response = requests.get('https://jsonplaceholder.typicode.com/todos/')
   # transfor the response to json objects
   todos = response.json()
   return render(request, "hello.html", {"todos": todos})
