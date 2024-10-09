from django.urls import path
from .views import (
    HomeView,
    SignUpView,
    AuthView,
    UserLogoutView,
    BlogListView,
    BlogDetailView,
    LikeCommentView,
    ShareBlogView,
    SearchBlogView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', AuthView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('blogs/', BlogListView.as_view(), name='blog_list'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('like/<int:comment_id>/', LikeCommentView.as_view(), name='like_comment'),
    path('share/<int:blog_id>/', ShareBlogView.as_view(), name='share_blog_via_email'),
    path('search/', SearchBlogView.as_view(), name='search_blog'),
]
