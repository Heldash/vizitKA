from django.urls import path
from .views import (home_views)
urlpatterns = [
    path("home/",home_views,name="home"),
    path("category/",lambda x:x,name ="category_url"),
    path("about/",lambda x:x,name ="about_site")
]