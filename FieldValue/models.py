from django.db import models

from Trinamic.models import Item


class Field(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50, default='')

    class Meta:
        db_table = 'web_field'


class FieldValue(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    value = models.TextField(default='')

    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        db_table = 'web_fieldvalue'
