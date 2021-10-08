"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import main,about,projects,contact,details,details2,details3,details4

app_name = 'portfolio'
urlpatterns = [
    path('', main, name='main'),
    # path('about/',about,name='about'),
    path('projects/',projects,name='projects'),
    path('contact/',contact,name='contact'),
    path('details/',details,name='details'),
    path('details2/',details2,name='details2'),
    path('details3/',details3,name='details3'),
    path('details4/',details4,name='details4'),
]