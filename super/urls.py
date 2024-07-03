from django.urls import path

from . import views

# si no posem app_name no funcionen el links
# les urls dels links les fem a partir de polls:name
app_name = "super"

urlpatterns = [
    path("", views.IndexView, name="index"),
    path("products", views.ProductView, name="products"),
    path("customers", views.IndexView, name="customers"),
    path("orders", views.IndexView, name="orders"), 
]

