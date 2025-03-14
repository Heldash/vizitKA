from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# from .models import
from . import models
# Create your views here.
def home_views(request:HttpRequest):
    categoryes = models.Category.objects.all()

    if request.GET.get("id",-1) == -1:
        user_home = models.UserVizit.objects.get(is_superuser=True)
        stacks = models.StackUserRelate.objects.all().filter(user_id=user_home)
        return render(request,"home.html",context={"user_home":user_home,"categories":categoryes,"stacks":stacks})
    else:
        try:
            user_home = models.UserVizit.objects.get(id = request.GET.get("id",-1))
            stacks = models.StackUserRelate.all().filter(user_id=user_home)
        except:
            render(request,"404page.html",context={"error_text":"Данный пользователь не найден"})
        return render(request, "home.html", context={"user_home": user_home,"categories":categoryes,"stacks":stacks})
def about_view(request:HttpRequest):
    try:
        user = models.UserVizit.objects.get(is_superuser=True)
        staks = models.StackUserRelate.objects.all().filter(user_id=user)
        links = models.LinksAcc.objects.all().filter(user_id=user)
        # for i in staks:
        #     print(staks)
    except Exception as ex:
        return HttpResponse(ex)
    return render(request,"about.html",
                  context={"user":user,"stacks":staks,"links":links})
def posts_view(request:HttpRequest):
    id = request.GET.get("id",-1)
    if id == -1:
        try:
            user = models.UserVizit.objects.get(is_superuser=True)
            posts = models.Post.objects.all().filter(author=user,is_posted=True)
        except:
            return render(request,"404page.html",context={"error_text":"Пост не найден"})
        return render(request, "posts.html", context={"user": user, "posts": posts})
    else:
        try:
            # user = models.UserVizit.objects.get(is_superuser=True)
            post = models.Post.objects.get(id=id,is_posted=True)
            images = models.ImagesPost.objects.all().filter(post_id=post)
        except:
            return render(request,"404page.html",context={"error_text":"Пост не найден"})
        return render(request, "post_page.html", context={"post": post,"images_post":images})

def login_user(request:HttpRequest):
    if request.method=="POST":
        pass
def user_edit(request:HttpRequest):
    pass