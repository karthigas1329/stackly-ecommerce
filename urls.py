"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from storeapp import views
from storeapp.views import SignUp,PostDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('detail/',views.detail),
    path('about/',views.about),
    path('contact/',views.contact),
    path('index/', views.index),
    path('gallery/', views.gallery),
    path('base/', views.base),
    path('signup/',SignUp.as_view()),
    path('logout/',views.logout),
    path('details/<int:pk>/',PostDetailView.as_view()),
    path('elecgallery/', views.elecgallery),
    path('wears/',views.wears),
    path('kids/', views.kids),
    path('grocery/',views.grocery),
    path('jewel/', views.jewel),
    path('cart/', views.static_cart_view, name='static_cart'),
    path('product/', views.product),
]
