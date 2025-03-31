from django.urls import path
from .views import generate_blog

urlpatterns = [
    path("generate-blog/", generate_blog, name="generate_blog"),
]
