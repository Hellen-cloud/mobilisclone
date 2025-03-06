from django.urls import path
from hellenapp import views

urlpatterns=[
    path('',views.index,name='index'),

    path('tails/',views.details,name='details'),

    path('meet/',views.meet,name='meet'),

]