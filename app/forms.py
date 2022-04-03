
from django import forms
from .models import  Comments, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('content','post','creation_date','author_name')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['upvote']
