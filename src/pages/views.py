from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'pages/index.html', {})

def about_view(request):
    return render(request, 'pages/about.html', {})

def contact_view(request):
    return render(request, 'pages/contact.html', {})

def coming_view(request):
    return render(request, 'pages/coming.html', {})