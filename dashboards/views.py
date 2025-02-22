from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib import messages
from blogapp.models import NavItem,Post
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm,PostForm
# Create your views here.
@login_required (login_url='/login/')
def dashboard(request):
    navitem_count=NavItem.objects.all().count()
    post_count=Post.objects.all().count()

    content={
        'navitem_count':navitem_count,
        'post_count':post_count
    }
    return render(request,"dashboard/dashboard.html",content)
def categories(request):
    return render(request,"dashboard/categories.html")
def add_category(request):
     if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('categories/')  # Redirect to another page
     else:
        form = CategoryForm()
     content={
        'form':form
    }
    # return render(request, 'add_category.html', {'form': form}) 
     return render (request,"dashboard/addcategory.html",content)
def posts(request):
    Posts=Post.objects.all()
    data={
        'Posts':Posts
    }
    return render(request,"dashboard/Posts.html",data)
def edit_cat(request,id):
    category=get_object_or_404(NavItem,pk=id)
    print(category)
    if request.method == "POST":
        form=CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('posts/')
        else:
            print(form.errors)
    
    else:
        form=CategoryForm(instance=category)
    content={
        'form':form,
        'category':category
    }
    print(id)
    return render(request,"dashboard/edit_category.html",content)
def delete_cat(request,id):
    category=get_object_or_404(NavItem,pk=id)
    category.delete()
    return redirect('/categories')

def addpost(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()  # Save the form and get the instance
            messages.success(request, "Post created successfully!")
            return redirect('posts')  # Redirect to the 'posts' view
    else:
        form = PostForm()

    # Render the form with any existing errors or initial state
    return render(request, 'dashboard/addpost.html', {'form': form})
def delete_post(request,id):
    deletepost=get_object_or_404(Post,pk=id)
    deletepost.delete()
    return redirect('posts')
def edit_post(request,id):
    posts=get_object_or_404(Post,pk=id)
    # print(category)
    if request.method == "POST":
        form=PostForm(request.POST,instance=posts)
        if form.is_valid():
            form.save()
            return redirect('posts')
        else:
            print(form.errors)
    else:
     form =PostForm(instance=posts)
    data={
        'form':form,
        'posts':posts
    }
    return render(request,"dashboard/editpost.html",data)
    

