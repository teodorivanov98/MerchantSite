from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import CartItem
from django.contrib.auth.decorators import login_required


@login_required
def view_cart(request):
    items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.total_price() for item in items)
    return render(request, 'cart/cart.html', {'cart_items': items, 'total_price': total_price})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))

    # Get or create cart item
    item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': quantity}
    )

    if not created:
        item.quantity += quantity
        item.save()

    return redirect('cart')


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id, user=request.user)
    item.delete()
    return redirect('cart')
