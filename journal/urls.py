from django.urls import path
from . import views 

urlpatterns = [
    path('new/list_news/', views.NewListView.as_view(), name='list-news'),
    path('new/<int:pk>/', views.new_detail, name='new_detail'),
    path('new/add/', views.NewCreate.as_view(), name='new-add'),
    path('new/edit/<int:pk>/', views.NewUpdate.as_view(), name='new-update'),
    path('new/<int:pk>/delete/', views.NewDelete.as_view(), name='new-delete')
]