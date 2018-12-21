from django.urls import path
from .views import (
    ListCreateArticleAPIView,
    UpdateDestroyArticleAPIView,
    BookMarkArticleAPIView,
    LikeArticleAPIView,
    CreateRatings,
    FavoriteArticles,
    RetrieveArticlesWithFavoritesStatus,
    ListCreateCommentsAPIView,
    CommentRetrieveDestroyAPIView,
    ListCreateThreadAPIView,
    CommentLikeAPIView,
    ViewUserBookmarks,
)

urlpatterns = [
    path('', ListCreateArticleAPIView.as_view()),
    path('<slug>', UpdateDestroyArticleAPIView.as_view(), ),
    path('<slug>/bookmark', BookMarkArticleAPIView.as_view(), ),
    path('bookmarks/', ViewUserBookmarks.as_view(), ),
    path('<slug>/likes', LikeArticleAPIView.as_view(), ),
    path('<slug>/ratings/', CreateRatings.as_view()),
    path('<slug>/likes', LikeArticleAPIView.as_view(), ),
    path('<slug>/favorites/', FavoriteArticles.as_view(), ),
    path('favorites/', RetrieveArticlesWithFavoritesStatus.as_view(), ),
    path('<str:slug>/comments',
         ListCreateCommentsAPIView.as_view()),
    path('<str:slug>/comments/<int:pk>',
         CommentRetrieveDestroyAPIView.as_view()),
    path('<str:slug>/comments/<int:pk>/threads',
         ListCreateThreadAPIView.as_view()),
    path('<int:pk>/comments/like',
         CommentLikeAPIView.as_view()),

]
