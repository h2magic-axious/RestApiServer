from rest_framework import serializers

from Blog.models import BlogCategory, BlogComment, BlogArticle, BlogTag


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['id', 'name', 'blogarticle_set']


class BlogTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTag
        fields = ['id', 'name']


class BlogArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogArticle
        fields = ['id', 'title', 'body', 'excerpt', 'created', 'category', 'tag', 'blogcomment_set']


class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = '__all__'
