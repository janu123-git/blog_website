<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"doc/index.html")
=======
from django.shortcuts import render,redirect,HttpResponse
from . models import NavItem,Post,Comment
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import authenticate
from django.contrib import auth
# from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    # fetching all nav items 
    navitem=NavItem.objects.all()
    # filter items from post 
    feature_item=Post.objects.filter(is_show=True,status='feature')
    recent_item=Post.objects.filter(is_show=True,status='Recent')

    data={
        'navitem':navitem,
        'featureitem':feature_item,
        'recentitem':recent_item
    }
    return render(request,"doc/index.html",data)
def showcategory(request,id):
    navitem=NavItem.objects.all()
    catitem=Post.objects.filter(category=id)
    # catid=NavItem.objects.get(pk=id)
    data={
         'navitem':navitem,
         'catitem':catitem
        #  'catid':catid
    }
 
    return render(request,"doc/category.html",data)
def showdetail(request,slug):
    postshow=Post.objects.get(slug=slug)
    comments=Comment.objects.filter(post=postshow)
    comments_count=comments.count()
    context={
        'postshow':postshow,
        'comments':comments,
        'comments_count':comments_count
    }
    return render(request,"doc/showdetails.html",context)
def feature_post(request):
   featureitem=Post.objects.filter(status='feature',is_show=True)
   return render(request,"doc/featuepost.html",{'featureitem':featureitem})
def recent_post(request):
   recentpost=Post.objects.filter(status='Recent',is_show=True)
   return render(request,'doc/recentpost.html',{'recentpost':recentpost})
def searchitem(request):
    if request.method=="GET":
        search=request.GET.get("search")
        search_item=Post.objects.filter(name__icontains=search)
    # print(search_item)
    context={
        'items':search_item
    }
    return render(request,"doc/searchitem.html",context)

def register(request):
    if request.method=="POST":
       form=CustomUserCreationForm(request.POST)
       if form.is_valid():
           form.save()
    else:
        form=CustomUserCreationForm()
    context={
        'form':form
    }
    return render(request,"doc/register.html",context)
def login(request):
   if request.method=="POST":
      form=AuthenticationForm(request, request.POST)
      print(form)
      if form.is_valid():
         username=form.cleaned_data['username']
         password=form.cleaned_data['password']
         user=auth.authenticate(username=username,password=password)
         if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
      #    form.save()
        #  return redirect('dashboard')
   else:
    form=AuthenticationForm()
   context={
      'form':form
   }
   return render(request,"doc/login.html",context)
def logout_view(request):
    auth.logout(request)
    return HttpResponse("logout successfully")
>>>>>>> a51b610 (categories crud operation)
