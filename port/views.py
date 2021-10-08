# Create your views here.

from django.shortcuts import render


# Create your views here.

def main(request):
    return render(request,'main.html')

def about(request):
    return render(request,'about.html')

def projects(request):
    return render(request,'projects.html')

def contact(request):
    return render(request,'contact.html')

def details(request):
    return render(request,'details.html')

def details2(request):
    return render(request,'details2.html')

def details3(request):
    return render(request,'details3.html')

def details4(request):
    return render(request,'details4.html')

