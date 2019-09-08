from . import views
from django.urls import path

app_name = 'users'

urlpatterns = [
       path('login/', views.login, name='login'),
       path('register/', views.RegisterView.as_view(), name='register'),
]
