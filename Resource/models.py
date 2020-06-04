from django.db import models
from Trinamic.models import Item


# Create your models here.
class ResourceType(models.Model):
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)

    class Meta:
        db_table = 'trinamic_resource_type'


class ResourceContent(models.Model):
    name = models.CharField(max_length=100)
    origin_url = models.URLField()
    using_url = models.URLField()

    resource_type = models.ForeignKey(ResourceType, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        db_table = 'trinamic_resource_content'
