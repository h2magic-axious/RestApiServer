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
            query_queue = [article.category.name, article.title, article.excerpt, article.body] + [tag.name for tag in
                                                                                                   article.tag.all()]
            for query in query_queue and article not in self.queryset:
                if self.query in query:
                    self.queryset.append(article)

    def results(self):
        self.search()
        return [article.json() for article in self.queryset]


class ItemSearcher(BaseSearcher):
    def search(self):
        queryset = Item.objects.all()
        for item in queryset:
            query_queue = [item.category.name, item.category.product.name, item.model, item.excerpt]
            for query in query_queue:
                if self.query in query and item not in self.queryset:
                    self.queryset.append(item)

    def results(self):
        self.search()
        return [item.json() for item in self.queryset]


def search(request, query):
    return JsonResponse({'article': BlogSearcher(query).results(), 'item': ItemSearcher(query).results()})
