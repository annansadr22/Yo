from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='dashboard/home.html'),name='home'),
    path('faq/', TemplateView.as_view(template_name='extra/faq.html'),name='faq'),
    path('contact-us/', TemplateView.as_view(template_name='extra/contactus.html'),name='contact_us'),
    path('form-job/', TemplateView.as_view(template_name='databases/formjob.html'),name='form_job'),
    path('form-freelance/', TemplateView.as_view(template_name='databases/formfreelance.html'),name='form_freelance'),
    
]