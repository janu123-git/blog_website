from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from blogapp.models import NavItem,Post
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm
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
            return redirect('categories')  # Redirect to another page
     else:
        form = CategoryForm()
     content={
        'form':form
    }
    # return render(request, 'add_category.html', {'form': form}) 
     return render (request,"dashboard/addcategory.html",content)
def posts(request):
    return render(request,"dashboard/Posts.html")
def edit_cat(request,id):
    category=get_object_or_404(NavItem,pk=id)
    print(category)
    if request.method == "POST":
        form=CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('/categories')
    
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

