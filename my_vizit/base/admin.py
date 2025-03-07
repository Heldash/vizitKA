from django.contrib import admin
from .models import (UserVizit,Category,ImagesPost,Post,StackUserRelate,Stack)
# Register your models here.
admin.site.register(UserVizit)
admin.site.register(Category)
admin.site.register(ImagesPost)
admin.site.register(Post)
admin.site.register(StackUserRelate)
admin.site.register(Stack)