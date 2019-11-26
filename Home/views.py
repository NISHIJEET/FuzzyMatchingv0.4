from django.shortcuts import render
from Input.views import data
# This will be the landing page of your tool

def Home(request):
    # data = {'modal': "", 'file_selected': False}
    return render(request, 'home.html' )





