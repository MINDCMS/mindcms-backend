from django.urls import path
from .views import generate_blog
from .views import generate_caption
from .views import generate_image_api

urlpatterns = [
    path("generate-blog/", generate_blog, name="generate_blog"),
    path('generate-caption/', generate_caption, name='generate_caption'),
     path('generate-image/', generate_image_api, name='generate-image'),
]
