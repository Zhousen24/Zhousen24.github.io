from django.urls import path
from . import views

app_name = 'verifications'

urlpatterns = [
    path('image_codes/<uuid:image_code_id>/', views.ImageCodeView.as_view(), name='image_code')
]