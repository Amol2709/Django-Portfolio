
from portfolio import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='home'),
    path('home', views.home,name='home'),
    path('takeaway', views.takeaway,name='takeaway'),
    path('form', views.form,name='form'),
    path('viewpaper', views.viewpaper,name='viewpaper'),
    path('contact', views.contact,name='contact'),
]
