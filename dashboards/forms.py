from django import forms
from blogapp.models import NavItem
class CategoryForm(forms.ModelForm):
    class Meta:
        model=NavItem
        fields="__all__"
        