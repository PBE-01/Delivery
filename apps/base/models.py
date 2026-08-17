from django.db import models

# Create your models here.

class BaseMoodel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    update_at =  models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True