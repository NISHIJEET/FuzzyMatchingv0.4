from django.shortcuts import render

# Create your views here.

def Output(request):
    return render(request, 'Output.html',  )