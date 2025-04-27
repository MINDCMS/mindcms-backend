from django.urls import path
from .views import generate_blog
from . import views
from .views import generate_image_api

urlpatterns = [
    path("generate-blog/", generate_blog, name="generate_blog"),
    path('generate/', views.generate_caption, name='generate_caption'),
    path('generate-image/', views.generate_image_api, name='generate-image'),
]
