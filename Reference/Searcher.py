from Blog.models import BlogCategory, BlogTag, BlogArticle, BlogComment
from Trinamic.models import Item
from FieldValue.models import FieldValue
from Resource.models import ResourceContent, ResourceType

from django.http import JsonResponse


class BaseSearcher:
    def __init__(self, query):
        self.query = query
        self.queryset = []


class BlogSearcher(BaseSearcher):
    def search(self):
        queryset = BlogArticle.objects.all()
        for article in queryset:
            if self.query in article.title:
                self.queryset.append(article)
                continue

            if self.query in article.excerpt:
                self.queryset.append(article)
                continue

            if self.query in article.body:
                self.queryset.append(article)
                continue

            if self.query in article.category.name:
                self.queryset.append(article)
                continue

            for tag in article.tag.all():
                if self.query in tag.name:
                    self.queryset.append(article)
                    break

    def results(self):
        self.search()
        return [article.json() for article in self.queryset]


class ItemSearcher(BaseSearcher):
    def search(self):
        queryset = Item.objects.all()
        for item in queryset:
            if self.query in item.model:
                self.queryset.append(item)
                continue

            if self.query in item.excerpt:
                self.queryset.append(item)
                continue

            if self.query in item.category.name:
                self.queryset.append(item)
                continue

            if self.query in item.category.product.name:
                self.queryset.append(item)
                continue

    def results(self):
        self.search()
        return [item.json() for item in self.queryset]


def search(request, query):
    return JsonResponse({'article': BlogSearcher(query).results(), 'item': ItemSearcher(query).results()})
