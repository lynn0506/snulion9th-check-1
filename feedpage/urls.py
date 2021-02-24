from django.urls import path
from feedpage import views

app_name = 'feedpage'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:id>/', views.show, name='show'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/edit/', views.edit, name='edit'),
    path('<int:id>/comments/', views.CommentView.create, name='comment_create'),
    path('<int:id>/comments/<int:cid>/', views.CommentView.delete, name='comment_delete'),
    path('<int:id>/like/', views.LikeView.create, name='like'),
]