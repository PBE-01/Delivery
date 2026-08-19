from django.contrib import admin
from django.contrib.auth import get_user_model
from apps.products.models import Order

# Register your models here.

User = get_user_model()

# admin.site.register(User)
class OrderInline(admin.TabularInline):
    model = Order
    extra = 0
    fields = ('id', 'status', 'total_price', 'created_at')
    can_delete = False
    readonly_fields = ('id', 'status', 'total_price', 'created_at')

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "phone"
    )
    list_filter = (
        "is_active",
        "is_staff",
        "is_superuser"
    )
    search_fields = (
        "username",
        "first_name"
    )
    order = (
        "id",
    )
    inlines = (
        OrderInline,
    )


