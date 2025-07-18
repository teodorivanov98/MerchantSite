
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='cart'),  # <-- this is named 'cart', NOT 'view_cart'
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
