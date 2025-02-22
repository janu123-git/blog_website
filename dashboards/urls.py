from django.urls import path
from . import views
urlpatterns = [
   path('dashboard/',views.dashboard,name="dashboard"),
   path('categories/',views.categories,name="categories"),
   path('posts/',views.posts,name='posts'),
   path('addcategory',views.add_category,name="add_category"),
   path('edit_category/<int:id>/',views.edit_cat,name="edit_cat"),
   path('delete_category/<int:id>/',views.delete_cat,name="delete_cat")
]