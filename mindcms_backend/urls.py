from django.urls import path
from .views import generate_blog
<<<<<<< HEAD
from .views import generate_caption
=======
from . import views
>>>>>>> 2238b225a04f077ba0b53acd724ca70a5c885fce
from .views import generate_image_api

urlpatterns = [
    path("generate-blog/", generate_blog, name="generate_blog"),
<<<<<<< HEAD
    path('generate-caption/', generate_caption, name='generate_caption'),
     path('generate-image/', generate_image_api, name='generate-image'),
=======
    path('generate/', views.generate_caption, name='generate_caption'),
    path('generate-image/', views.generate_image_api, name='generate-image'),
>>>>>>> 2238b225a04f077ba0b53acd724ca70a5c885fce
]
