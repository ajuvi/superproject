from django.urls import path

from . import views

# si no posem app_name no funcionen el links
# les urls dels links les fem a partir de polls:name
app_name = "super"

urlpatterns = [
    path("", views.IndexView, name="index"),
    path("product", views.IndexView, name="product"),
    path("customer", views.IndexView, name="customer"),
    path("order", views.IndexView, name="order"), 
]
