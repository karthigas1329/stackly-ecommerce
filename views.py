from django.shortcuts import render,redirect
from storeapp.models import Post
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView


def base(request):
	return render(request,'apps/base.html')

def index(request):
	return render(request,'apps/index.html')

def detail(request):
    return render(request,'apps/detail.html')

def about(request):
    return render(request,'apps/about.html')

def contact(request):
    return render(request,'apps/contact.html')

def gallery(request):
    return render(request,'apps/gallery.html')

def base(request):
    return render(request, 'apps/base.html')

class SignUp(generic.CreateView):
    form_class    = UserCreationForm
    success_url   = reverse_lazy('login')
    template_name = 'signup.html'

def logout(request):
    return render(request,'apps/logout.html')

class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'


def elecgallery(request):
    return render(request,'apps/elecgallery.html')

def wears(request):
    return render(request, 'apps/wears.html')

def kids(request):
    return render(request,'apps/kids.html')

def grocery(request):
    return render(request,'apps/grocery.html')

def jewel(request):
    return render(request,'apps/jewel.html')

def static_cart_view(request):
    return render(request, 'apps/cart.html')

def product(request):
    return render(request,'apps/product.html')

