from django.shortcuts import render

def index_pro(request):
    return render(request,'index_pro.html')
 
# Create your views here.

def login_page(request):
    return render(request,'login_page.html')

def register(request):
    return render(request,'register.html')

