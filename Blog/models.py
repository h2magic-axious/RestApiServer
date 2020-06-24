from django.db import models
from django.utils import timezone


# Create your models here.
class BlogCategory(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'trinamic_blog_category'


class BlogTag(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'trinamic_blog_tag'


class BlogArticle(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    excerpt = models.CharField(max_length=255)
    created = models.DateField(default=timezone.now)

    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    tag = models.ManyToManyField(BlogTag)

    def save(self, *args, **kwargs):
        if not self.excerpt:
            self.excerpt = self.body[:200]

        super().save(*args, **kwargs)

    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'excerpt': self.excerpt,
            'body': self.body,
            'created': self.created,
            'category': self.category.name,
        }

    class Meta:
        db_table = 'trinamic_blog_article'


class BlogComment(models.Model):
    email = models.EmailField()
    score = models.IntegerField(default=3)
    body = models.TextField()
    created = models.DateField(default=timezone.now)

    blog_article = models.ForeignKey(BlogArticle, on_delete=models.CASCADE)

    class Meta:
        db_table = 'trinamic_blog_comment'
