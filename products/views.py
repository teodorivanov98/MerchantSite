from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    category_choices = Product.CATEGORY_CHOICES  # ← This must match template
    selected_category = request.GET.get('category')

    if selected_category:
        products = products.filter(category=selected_category)

    return render(request, 'products/product_list.html', {
        'products': products,
        'category_choices': category_choices,  # ← THIS name
        'selected_category': selected_category
    })
