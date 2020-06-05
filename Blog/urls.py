from django.urls import path

from Blog import views

urlpatterns = [
    path('blog/category', views.BlogCategoryList.as_view()),
    path('blog/category/<int:pk>', views.BlogCategoryDetail.as_view()),
    path('blog/category/whole', views.whole_blog_categories),

    path('blog/tag', views.BlogTagList.as_view()),
    path('blog/tag/<int:pk>', views.BlogTagDetail.as_view()),
    path('blog/tag/whole', views.whole_blog_tag),

    path('blog/article', views.BlogArticleList.as_view()),
    path('blog/article/<int:pk>', views.BlogArticleDetail.as_view()),
    path('blog/article/whole', views.whole_blog_article),

    path('blog/comment', views.BlogCommentList.as_view()),
    path('blog/comment/<int:pk>', views.BlogCommentDetail.as_view()),
    path('blog/comment/whole', views.whole_blog_comment)
]
