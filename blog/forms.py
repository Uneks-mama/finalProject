from .models import Comment, Contactus
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class ContactusForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = ('name', 'email', 'body')