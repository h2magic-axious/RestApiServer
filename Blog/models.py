from django.db import models
from django.utils import timezone


# Create your models here.
class BlogCategory(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'trinamic_blog_category'


class BlogTag(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'trinamic_blog_tag'


class BlogArticle(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    excerpt = models.CharField(max_length=255)
    created = models.DateTimeField(default=timezone.now)

    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    tag = models.ManyToManyField(BlogTag)

    def save(self, *args, **kwargs):
        if not self.excerpt:
            self.excerpt = self.body[:200]

        super().save(*args, **kwargs)

    class Meta:
        db_table = 'trinamic_blog_article'


class BlogComment(models.Model):
    email = models.EmailField()
    score = models.IntegerField(default=3)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    blog_article = models.ForeignKey(BlogArticle, on_delete=models.CASCADE)

    class Meta:
        db_table = 'trinamic_blog_comment'
