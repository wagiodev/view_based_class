from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # path('about', views.about, name='about'),
    path('about/', views.AboutView.as_view()),
    path('post/', views.PostListView.as_view()),
    path('post/new2', views.PostFormView.as_view()),


]