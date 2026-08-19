from django.contrib import admin

from apps.products.models import Product, Category, Order, OrderItem

# admin.site.register(Product)
# admin.site.register(Category)
# admin.site.register(Order)
# admin.site.register(OrderItem)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name"
    )
    list_filter = (
        "is_active",
    )
    search_fields = (
        "name",
    )
    order = (
        "created_at","updated_at"
    )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'get_category_name', 'price'
        ) 
    list_filter = (
        'is_active',
        )
    search_fields = (
        'name',
        )
    ordering = (
        'id',
        )    

    @admin.display(ordering='category__name', description='Category Name')
    def get_category_name(self, obj):
        return obj.category.name if obj.category else "Kategoriya yo'q"

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ('product', 'quantity', 'price')
    extra = 4
    autocomplete_fields = (
        'product',
    )

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'status', 'total_price', 'created_at'
    ) 
    list_filter = (
        'is_active',
    )
    search_fields = (
        'created_at', 'status'
    )
    ordering = (
        'created_at',
    ) 

    inlines = (
    OrderItemInline,
    )
    
    
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'order', 'product', 'quantity', 'price'
    )
    list_filter = (
        'is_active',
    )
    search_fields = (
        'order', 'product'
    )
    ordering = (
        'id',
    )
