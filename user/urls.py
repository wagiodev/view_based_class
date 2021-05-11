
from django.urls import path
from . import views

urlpatterns = [
    path('login2/',    views.login,     name='login2'),
    path('logout/',   views.logout,    name='logout'),
    path('saludo/',   views.saludo,    name='saludo'),
    path('info/',     views.info,      name='info'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('list_user/', views.UserListView.as_view()),
]
