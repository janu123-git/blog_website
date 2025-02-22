from django.urls import path
from . import views
<<<<<<< HEAD
urlpatterns = [
 path('',views.index,name="index")
=======
urlpatterns=[
    path('',views.index,name="index"),
    path('category/<int:id>/',views.showcategory,name="show"),
    path('show/<slug:slug>/',views.showdetail,name="showdetail"),
    path('search/',views.searchitem,name="searchitem"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('logout_view/',views.logout_view,name="logout_view"),
    # path('dashboard/',views.dashboard,name="dashboard")
>>>>>>> a51b610 (categories crud operation)
]