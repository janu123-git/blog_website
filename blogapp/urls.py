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
    path('feature_post/',views.feature_post,name="feature_post"),
     path('recent_post/',views.recent_post,name="recent_post"),
    path('search/',views.searchitem,name="searchitem"),
    # form function 
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('logout_view/',views.logout_view,name="logout_view"),
    # path('dashboard/',views.dashboard,name="dashboard")
>>>>>>> a51b610 (categories crud operation)
]