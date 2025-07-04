from .models import CartItem

def cart_total(request):
    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(user=request.user).count()
        return {'cart_count': cart_count}
    return {'cart_count': 0}
