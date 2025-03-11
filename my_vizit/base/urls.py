from django.urls import path
from . import views
urlpatterns = [
    path("home/",views.home_views,name="home"),
    path("projects/",views.posts_view,name ="projects"),
    path("about/",views.about_view,name ="about_site")
]