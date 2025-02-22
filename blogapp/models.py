from django.db import models
<<<<<<< HEAD

# Create your models here.
=======
from django.contrib.auth.models import User
from autoslug import AutoSlugField
# Create your models here.
class NavItem(models.Model):
    Navname=models.CharField(max_length=100,unique=True,null=False)
    url=models.CharField(max_length=100,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Navname
status_choice=(
    ('feature','Feature'),
    ('Recent','Recent')
)    
class Post(models.Model):
    name=models.CharField(max_length=100)
    slug = AutoSlugField(populate_from=('name'), unique=True, max_length=255, null=True)
    category=models.ForeignKey(NavItem,on_delete=models.CASCADE)
    img=models.ImageField(upload_to='upload/')
    des=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    is_show=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=100,choices=status_choice,default='feature')
    updated_at=models.DateTimeField(auto_now=True)

>>>>>>> a51b610 (categories crud operation)
