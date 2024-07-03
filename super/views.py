from django.shortcuts import render
from django import forms
from django.db.models import Q
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

class ProductSearchForm(forms.Form):
    txt_cerca = forms.CharField(label="Entrada", max_length=200, required=False)
 
def ProductSearchView(request):
    form = ProductSearchForm()
    ctx_products = Product.objects.all()

    if request.method == "POST":
        form = ProductSearchForm(request.POST)
        if form.is_valid():
            txt_cerca = form.cleaned_data.get("txt_cerca")
            ctx_products = Product.objects.filter(
                Q(name__icontains=txt_cerca) |
                Q(product_code__icontains=txt_cerca)
            )

    context = {
        "form": form,
        "ctx_products": ctx_products,
    }   
    return render(request, "super/products_search.html", context)