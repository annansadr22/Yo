"""HireApex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView

#from django.views.static import serve
#from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('land.urls')),
    #path('home/', TemplateView.as_view(template_name='dashboard/home.html'),name='home'),
    #path('faq/', TemplateView.as_view(template_name='extra/faq.html'),name='faq'),
    #path('contact-us/', TemplateView.as_view(template_name='extra/contactus.html'),name='contact_us'),
    path('accounts/', include('allauth.urls')),

    #url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    #url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]