# from django.shortcuts import render, redirect, get_object_or_404
# from cart.models import CartItem
# from .models import Order, OrderItem
# from django.contrib.auth.decorators import login_required
#
#
# @login_required
# def checkout(request):
#     items = CartItem.objects.filter(user=request.user)
#     if not items:
#         return redirect('cart')
#
#     order = Order.objects.create(user=request.user)
#
#     for item in items:
#         OrderItem.objects.create(
#             order=order,
#             product=item.product,
#             quantity=item.quantity,
#             price=item.product.price
#         )
#         item.delete()
#
#     return redirect('order_summary', order_id=order.id)
#
#
# @login_required
# def order_summary(request, order_id):
#     order = get_object_or_404(Order, pk=order_id, user=request.user)
#     total = sum(item.quantity * item.price for item in order.items.all())
#     return render(request, 'orders/order_summary.html', {'order': order, 'total': total})
#
# # @login_required
# # def order_history(request):
# #     orders = Order.objects.filter(user=request.user).order_by('-created_at')
# #     return render(request, 'orders/order_history.html', {'orders': orders})
#
# @login_required
# def order_history(request):
#     orders = Order.objects.filter(user=request.user).prefetch_related('items__product').order_by('-created_at')
#
#     # Build a list of orders with totals
#     orders_with_totals = []
#     for order in orders:
#         total = sum(item.price * item.quantity for item in order.items.all())
#         orders_with_totals.append({
#             'order': order,
#             'total': total,
#         })
#
#     return render(request, 'orders/order_history.html', {
#         'orders_with_totals': orders_with_totals
#     })
#
from django.shortcuts import render, redirect, get_object_or_404
from cart.models import CartItem
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required

@login_required
def checkout(request):
    items = CartItem.objects.filter(user=request.user)
    if not items:
        return redirect('cart')

    order = Order.objects.create(user=request.user)
    for item in items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )
        item.delete()
    return redirect('order_summary', order_id=order.id)

@login_required
def order_summary(request, order_id):
    order = get_object_or_404(Order, pk=order_id, user=request.user)
    total = sum(item.quantity * item.price for item in order.items.all())
    return render(request, 'orders/order_summary.html', {'order': order, 'total': total})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).prefetch_related('items__product').order_by('-created_at')
    orders_with_totals = []
    for order in orders:
        total = sum(item.price * item.quantity for item in order.items.all())
        orders_with_totals.append({
            'order': order,
            'total': total,
        })
    return render(request, 'orders/order_history.html', {
        'orders_with_totals': orders_with_totals
    })
