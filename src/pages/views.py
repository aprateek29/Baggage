from django.shortcuts import render, redirect
from .models import Product, Contact
from django.contrib import messages



# Create your views here.
def index_view(request):
    return render(request, 'pages/index.html', {})

def about_view(request):
    return render(request, 'pages/about.html', {})

def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        obj = Contact.objects.create(name=name, email=email, phone=phone, message=message)
        obj.save()
        messages.success(request, f"We will contact you soon!")
        return redirect('/')
    return render(request, 'pages/contact.html', {})

def coming_view(request):
    return render(request, 'pages/coming.html', {})

def shop_view(request):
    product_list = Product.objects.all()
    return render(request, 'pages/shop.html', {'product_list': product_list})

def shop_single_view(request, id):
    product = Product.objects.get(id=id)
    product_list = Product.objects.all()[:4]
    return render(request, 'pages/single.html', {'product': product, 'product_list': product_list})

def newsletter(request):
    messages.success(request, f"Request Received!")
    return redirect('/')