from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'title': 'Головна сторінка',
        'values': ['fisting','is','300'],
        'obj': {
            'car': 'Жигуль',
            'age': 300,
            'hobby': 'scam'
        }
    }
    return render(request,'main/index.html',data)
def about(request):
    return render(request,'main/about.html')
