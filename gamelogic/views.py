from django.shortcuts import render

# Create your views here.
def basic(request):
    return render(request, 'basic.html')
def index(request):
    return render(request, 'index.html')
def index2(request):
    return render(request, 'index2.html')

def base(request):
    return render(request, 'base.html')
