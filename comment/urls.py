from django.urls import path

from comment import views

urlpatterns = [
    path('comments/create/<int:pk>/', views.CommentCreateView.as_view(), name='comment-create'),
]