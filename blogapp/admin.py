from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from .models import NavItem,Post
# Register your models here.
class navItemAdmin(admin.ModelAdmin):
    list_display=['Navname','url','created_at','updated_at']
admin.site.register(NavItem,navItemAdmin)

class postAdmin(admin.ModelAdmin):
    list_display=['name','slug','category','img','des','author','is_show','status','created_at','updated_at']
admin.site.register(Post,postAdmin)
>>>>>>> a51b610 (categories crud operation)
