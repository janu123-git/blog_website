from django.contrib import admin
<<<<<<< HEAD
<<<<<<< HEAD

# Register your models here.
=======
from .models import NavItem,Post
=======
from .models import NavItem,Post,Comment
>>>>>>> a6a901d (added blog)
# Register your models here.
class navItemAdmin(admin.ModelAdmin):
    list_display=['Navname','url','created_at','updated_at']
admin.site.register(NavItem,navItemAdmin)

class postAdmin(admin.ModelAdmin):
    list_display=['name','slug','category','img','des','author','is_show','status','created_at','updated_at']
admin.site.register(Post,postAdmin)
<<<<<<< HEAD
>>>>>>> a51b610 (categories crud operation)
=======
class CommentModel(admin.ModelAdmin):
    list_display=['user','post','comments','created_at','updated_at']
admin.site.register(Comment,CommentModel)    
>>>>>>> a6a901d (added blog)
