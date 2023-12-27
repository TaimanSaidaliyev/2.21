from django import forms
from Posts.models import Post


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'author')
        error_messages = None
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control"}),
            'author': forms.Select(attrs={"class":"form-control"}),
        }