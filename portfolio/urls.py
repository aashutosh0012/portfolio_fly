"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from home import views as homeView



urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('',homeView.portfolio, name='portfolio'),     #-> 'root' url -  portfolio
    # path('portfolio/',homeView.home, name='portfolio'),
    # path('',homeView.home, name='home'),          #-> 'root' url -  
    # path('',blogHome.as_view(),name='blog-home'),
    # path('',include('blog.urls'),name='blog'), #-> 'root' url - Blog 
]


urlpatterns += [
    path('blog/',include('blog.urls'),name='blog'),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]


# Edit portfolio/urls.py to server Static Files in gunicorn in heroku
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
