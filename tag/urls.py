from django.urls import path
from tag import views

app_name = 'tag'
urlpatterns = [
    path('new/', views.TagView.create, name='create'),
    path('<int:id>/', views.TagView.read, name='read'),
    path('<int:id>/update/', views.TagView.update, name='update'),
    path('<int:id>/delete/', views.TagView.delete, name='delete'),
]