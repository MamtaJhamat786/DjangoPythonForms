from django.urls import path
from . import views



urlpatterns = [
    path('',views.index, name= 'home'),
    path('home/', views.index, name='index'),
    path('formpage/', views.form_name_view, name='formname')
]


