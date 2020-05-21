from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50, default='')
    excerpt = models.TextField(default='')

    class Meta:
        db_table = 'trinamic_product'


class Category(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50, default='')
    excerpt = models.TextField(default='')

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'trinamic_category'


class Item(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    model = models.CharField(max_length=50)
    excerpt = models.TextField(default='')

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'trinamic_item'
