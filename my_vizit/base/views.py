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
            return HttpResponse("404, такого пользователя не существует")
        return render(request, "home.html", context={"user_home": user_home,"categories":categoryes,"stacks":stacks})
