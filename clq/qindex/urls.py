from django.urls import include,path
from . import views

app_name = "qindex"

urlpatterns = [
     
     path('', views.home, name='home'),
     path('about', views.about, name='about'),
     path('bhome', views.bhome, name='bhome'),
     path('ehome', views.ehome, name='ehome'),
     path('qr', views.qr,name='qr'), 
     path('vspl/', views.vspl,name='vspl'),
     path('vbspl/', views.vbspl,name='vbspl'),
     path('bqr', views.bqr,name='bqr'), 
     path('tl', views.tl,name='tl'),
     path('btl', views.btl,name='btl'),
     path('tl1/', views.tl1,name='tl1'),
     path('tl2/', views.tl2,name='tl2'),
     path('tl3/', views.tl3,name='tl3'),
     path('tl4/', views.tl4,name='tl4'),
     path('tl5/', views.tl5,name='tl5'),
     path('tl6/', views.tl6,name='tl6'),
     path('tl7/', views.tl7,name='tl7'),
     path('btl1/', views.btl1,name='btl1'),
     path('btl2/', views.btl2,name='btl2'),
     path('btl3/', views.btl3,name='btl3'),
     path('contact/', views.contact,name='contact'),
     path('contact/contactsave', views.contactsave, name="contactsave"),
]
