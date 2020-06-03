from django.db import models
from Trinamic.models import Item

MEDIA_TYPES = [
    ('PICTURE', '图片'),
    ('VIDEO', '视频')
]


class Media(models.Model):
    title = models.CharField(max_length=30, default='请输入标题')
    filename = models.CharField(max_length=50)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    origin_url = models.URLField()
    using_url = models.URLField(blank=True)

    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        db_table = 'trinamic_media'
