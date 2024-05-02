from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
     path('signup/', views.signup, name="signup"),
     path('signin/', views.signin, name="signin"),
     path('signout/', views.signout, name="signout"),

    path('<slug:slug_c>/', views.home, name="product by category"),
    path('<slug:slug_c>/<slug_p>/', views.products, name="product_details"),

 ]