from django.shortcuts import render
from .models import *

# Create your views here.
def IndexView(request):
    return render(request,"super/index.html",{})

# Create your views here.
def ProductView(request):
    ctx_productes = Product.objects.all()

    return render(request,"super/products.html",
                {
                    "ctx_productes":ctx_productes,
                })    
