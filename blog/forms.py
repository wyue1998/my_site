from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
        labels = {
            'username': 'Your Name',
            'user_email': 'Your Email',
            'text': 'Your Comment',
        }
        errors = {
            'username': {
                'required': 'Please enter your name',
            },
            'user_email': {
                'required': 'Please enter your email',
            },
            'text': {
                'required': 'Please enter your comment',
            },
        }