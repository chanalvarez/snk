from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('' , views.index, name ='home'),
    path('test' , views.test),
    path('Favor/<str:pk>/', views.Favor, name = 'Favor'),
    path('UpdateFavor/<str:ak>/<str:pk>/' , views.UpdateFavor , name = 'UpdateFavor'),
    path('search' , views.search , name='search'),
    path('RemoveFavor/<str:ak>/<str:pk>/' , views.RemoveFavor , name = 'RemoveFavor'),
    path('register' , views.register, name = 'register'),
    path('loginPage' , views.loginPage , name = 'loginPage'),
    path('logoutUser' , views.logoutUser , name = 'logoutUser'),
    path('about' , views.about , name = 'about'),
    path('adminpage', views.admin , name = 'adminpage'),
    path('ap' , views.ap , name = 'ap'),
    path('Delete/<str:pk>/' , views.delete , name = 'delete'),
    path('homework/<str:pk>' , views.homework , name='homeworkpage'),
    path('removehomework/<str:ak>/<str:pk>/' , views.removehomework , name = 'removehomework'),
    



    
]
