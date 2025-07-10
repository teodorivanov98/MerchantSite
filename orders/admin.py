import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import Order, OrderItem


def export_orders_csv(modeladmin, request, queryset):
    # Create the HttpResponse object with a CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="orders.csv"'

    writer = csv.writer(response)

    # Write header row. Customize columns as needed.
    writer.writerow(['Order ID', 'Username', 'Created At', 'Item Product', 'Quantity', 'Price', 'Total Price'])

    for order in queryset:
        # If you want to include all items for an order in separate rows,
        # loop through the order items:
        for item in order.items.all():
            writer.writerow([
                order.id,
                order.user.username,
                order.created_at,
                item.product.name,
                item.quantity,
                item.price,
                item.total_price()  # Calculates quantity * price
            ])
        # Optionally, add a blank row between orders for clarity:
        writer.writerow([])

    return response


export_orders_csv.short_description = "Export selected orders to CSV"


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'id']
    inlines = [OrderItemInline]
    actions = [export_orders_csv]  # Register the custom action


admin.site.register(Order, OrderAdmin)
