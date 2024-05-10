from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('createTopic/', views.createTopic, name='topic'),
    path('', views.index, name="home"),
    path('post/<str:pk>', views.single, name='single'),
    path('create/', views.create, name='create'),
    path('updatePost/<str:pk>', views.update, name='update'),
    path('delete/<str:pk>', views.delete,name='delete'),
    path('delete-comment/<str:pk>', views.deleteComment, name='deleteComment'),
    path('edit-comment/<str:pk>', views.editComments, name='edit'),
    path('profile/<str:pk>', views.userProfile, name='profile')
]   
