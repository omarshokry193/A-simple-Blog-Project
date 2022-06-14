from django.urls import path
from .views import *
app_name = 'core'
urlpatterns = [
    path('', HomeView.as_view(),name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('create-post', AddPostView.as_view(), name="add_post"),
    path('article/<int:pk>/edit', UpdatePostView.as_view(), name="edit_post"),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
    path('add-category/', AddCategoryView.as_view(), name="add_category"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('like/<int:pk>/', LikeView, name="like_post"),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name="add_comment"),
]