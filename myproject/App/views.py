from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,"App/index.html",{})

def aboutus(request):
    return render(request,"App/about.html",{})

def contact(request):
    return render(request,"App/contact.html",{})

def faq(request):
    return render(request,"App/faq.html",{})

def productdetail(request):
    return render(request,"App/product-detail.html",{})

def products(request):
    return render(request,"App/products.html",{})

def signin(request):
    return render(request,"App/sign-in.html",{})

def signup(request):
    return render(request,"App/sign-up.html",{})

