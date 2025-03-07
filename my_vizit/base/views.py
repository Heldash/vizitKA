from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import UserVizit
# Create your views here.
def home_views(request:HttpRequest):
    if request.GET.get("id",-1) == -1:
        UserVizit.objects.get(is_superuser=True)
        return render(request,"home.html",context={"user_home":UserVizit})
    else:
        try:
            UserVizit.objects.get(id = request.GET.get("id",-1))
        except:
            return HttpResponse("404, такого пользователя не существует")
        return render(request, "home.html", context={"user_home": UserVizit})
