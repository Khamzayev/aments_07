from django.db import models
from django.utils.translation import gettext_lazy as _



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True



class OrderModel(models.Model):
    order = models.IntegerField(verbose_name=_('order'))

    class Meta:
        abstract = True


class ActiveModel(models.Model):
    active = models.BooleanField(default=True, verbose_name=_('active'))


    class Meta:
        abstract = True