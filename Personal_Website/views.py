from django.shortcuts import render

def index(requests):
    return render(requests,'Personal_Website/index.html')
