from django import forms
from blogapp.models import NavItem,Post
class CategoryForm(forms.ModelForm):
    class Meta:
        model=NavItem
        fields="__all__"

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('name','category','img','des','author','is_show','status')
        widgets = {
            'img': forms.ClearableFileInput(attrs={'required': False}),
        }
        