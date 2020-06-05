from Blog.models import BlogArticle, BlogTag, BlogCategory, BlogComment
from Blog.serializers import BlogArticleSerializer, BlogTagSerializer, BlogCategorySerializer, BlogCommentSerializer
from rest_framework import generics
from rest_framework.filters import SearchFilter
from django.http import JsonResponse

from Reference.Pagination import OwnPagination


def whole_blog_categories(request):
    return JsonResponse({'results': [{'id': bc.id, 'name': bc.name} for bc in BlogCategory.objects.all()]})


class BlogCategoryList(generics.ListCreateAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    pagination_class = OwnPagination
    filter_backends = [SearchFilter]
    search_fields = ['name']


class BlogCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer


def whole_blog_tag(request):
    return JsonResponse({'results': [{'id': bt.id, 'name': bt.name} for bt in BlogTag.objects.all()]})


class BlogTagList(generics.ListCreateAPIView):
    serializer_class = BlogTagSerializer
    queryset = BlogTag.objects.all()
    pagination_class = OwnPagination
    filter_backends = [SearchFilter]
    search_fields = ['name']


class BlogTagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogTag.objects.all()
    serializer_class = BlogTagSerializer


def whole_blog_article(request):
    return JsonResponse({'results': [{'id': ba.id, 'title': ba.title} for ba in BlogArticle.objects.all()]})


class BlogArticleList(generics.ListCreateAPIView):
    serializer_class = BlogArticleSerializer
    pagination_class = OwnPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'excerpt', 'body']

    def get_queryset(self):
        queryset = BlogArticle.objects.all()

        category_id = self.request.query_params.get('category', None)
        if category_id:
            return queryset.filter(category_id=category_id)

        tag_id = self.request.query_params.get('tag', None)
        if tag_id:
            return queryset.filter(tag=tag_id)

        score = self.request.query_params.get('score', None)
        if score:
            return queryset.filter(blogcomment__score=score)

        return queryset


class BlogArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogArticle.objects.all()
    serializer_class = BlogArticleSerializer


def whole_blog_comment(request):
    return JsonResponse({'results': [{'id': bc.id, 'email': bc.email} for bc in BlogComment.objects.all()]})


class BlogCommentList(generics.ListCreateAPIView):
    serializer_class = BlogCommentSerializer
    pagination_class = OwnPagination
    filter_backends = [SearchFilter]
    search_fields = ['email', 'body']

    def get_queryset(self):
        queryset = BlogComment.objects.all()

        article_id = self.request.query_params.get('article', None)
        if article_id:
            return queryset.filter(article_id=article_id)

        score = self.request.query_params.get('score', None)
        if score:
            return queryset.filter(score=score)

        return queryset


class BlogCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogCommentSerializer
    queryset = BlogComment.objects.all()
