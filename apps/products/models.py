from decimal import Decimal
from django.db import models
from apps.base.models import BaseMoodel
from django.contrib.auth import get_user_model
from apps.products.chaoices import OrderStatus

User = get_user_model()
# Create your models here.  

class Category(BaseMoodel):
    name = models.CharField(max_length=255, verbose_name="Kategoriya nomi")

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'  

    def __str__(self):
        return self.name

class Product(BaseMoodel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='products', verbose_name="Kategoriya")
    name = models.CharField(max_length=255, verbose_name="Mahsulot nomi")
    description = models.TextField(verbose_name="Mahsulot tavsifi")
    price = models.DecimalField(max_digits=10 , decimal_places=2, verbose_name="Narxi")

    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'

    def __str__(self):
        return self.name

class Order(BaseMoodel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders', verbose_name="Foydalanuvchi")
    status = models.CharField(max_length=50, choices=OrderStatus.choices, default=OrderStatus.PENDING, verbose_name="Holat")

    class Meta:
        verbose_name = 'Buyurtma'
        verbose_name_plural = 'Buyurtmalar'

    @property
    def total_price(self):
        return sum(
            item.subtotal
            for item in self.item.all()
        )

    def __str__(self):
        username = self.user.username if self.user else "No'malum"
        return f"Order #{self.id} - {username} - {self.status}"


class OrderItem(BaseMoodel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items', verbose_name="Buyurtma")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, related_name='order_items', verbose_name="Mahsulot")
    quantity = models.PositiveBigIntegerField(verbose_name='Miqdori')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Sotilgan narxi")

    class Meta:
        verbose_name = 'Buyurtma elementi'
        verbose_name_plural = 'Buyurtma elementlari'

    @property
    def subtotal(self):
        if self.price is None or self.quantity is None:
            return Decimal('0.00')
        return self.price * self.quantity
        
    def __str__(self):
        product = self.product.name if self.product else "O'chirilgan mahsulot"
        return f"OrderItem #{self.id} - {product.name}"

    