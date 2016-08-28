from django import forms
from pagedown.widgets import PagedownWidget
from .models import Post, User

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget)
    publish = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Post
        fields = [
        "title",
        "image",
        "content",
        "draft",
        "publish",
        ]
        labels={
        "title":"Titre",
        "image": "Image",
        "content": "Contenu",
        "draft":"Brouillon",
        "publish":"Publication"
        }
        widgets={
        "publish": forms.DateInput(attrs={"placeholder":"Aujourd'hui"},)
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels={
        "username":"Pseudo",
        "first_name":"Prenom",
        "last_name":"Nom"
        }
