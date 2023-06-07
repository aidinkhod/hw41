from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request, 'index.html')

def page_2(request):
    return render(request, 'page2.html')

def page_3(request):
    return render(request, 'page3.html')