from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    # Add any additional fields you need for your custom user model
    email = models.EmailField(unique=True, verbose_name="Email manzil")
    avatar = models.ImageField(upload_to='media/avatars/', null=True, blank=True, verbose_name="Profil rasmi")
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Telefon raqam")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    EMAIL_FIELD = 'email'

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural= 'Foydalanuvchilar'

    def __str__(self):
        return self.username