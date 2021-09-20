from django.urls import path

from . import views

app_name = 'student'
urlpatterns = [   
    #path('', views.IndexView, name='index'),  
    path('panel', views.IndexView, name='index'),
    path('<str:request_id>/profile', views.Profile, name='profile'),
    path('login', views.LogIn, name='login'),
    path('', views.LogIn, name='login'),
    path('print', views.PrintDegree, name='PrintDegree'),
    path('salary', views.Salary, name='SalaryPayment'),
    path('terminfo',views.TermInfo, name='TermInfo'),
    
    #Error Page
    path('400',views.error400,name='400'),
    path('403',views.error403,name='403'),
    path('404',views.error404,name='404'),
    path('500',views.error500,name='500'),
    path('503',views.error503,name='503'),
]
