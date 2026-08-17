from django.db import models

class OrderStatus(models.TextChoices):
    PENDING = 'pending', 'Pending'
    ON_WAY = 'on_way', 'On Way'
    DELIVERED = 'delivered', 'Delivered'