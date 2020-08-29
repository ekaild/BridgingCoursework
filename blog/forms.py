from django import forms

from .models import Post, Traits

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class TraitsForm(forms.ModelForm):

    class Meta:
        model = Traits
        fields = ('title', 'text',)

