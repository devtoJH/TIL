from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:post_pk>/answer/<int:answer>', views.answer, name='answer'),
    path('<int:post_pk>/likes/', views.likes, name='likes'),
    path('<int:post_pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:post_pk>/comments/<int:comment_pk>/likes/', views.comment_likes, name='comment_likes'),
    path('<int:post_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
]
