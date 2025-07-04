from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('summary/<int:order_id>/', views.order_summary, name='order_summary'),
    path('history/', views.order_history, name='order_history'),
]
