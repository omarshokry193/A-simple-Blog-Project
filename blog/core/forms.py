from django import forms
from .models import *

choices = Category.objects.all().values_list("name","name")
choice_list = []

for item in choices:
    choice_list.append(item)
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','snippet','category','author','body')
        widgets = {
            'title':      forms.TextInput(attrs={'class':'form-control'}),
            'snippet':    forms.TextInput(attrs={'class':'form-control'}),
            'category':   forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'author':     forms.TextInput(attrs={'value':'','id':'username','type':'hidden'}),
            'body':       forms.Textarea(attrs={'class':'form-control'}),
            
            
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','snippet','body')
        widgets = {
            'title':      forms.TextInput(attrs={'class':'form-control'}),
            'body':       forms.Textarea(attrs={'class':'form-control'}),
            'snippet':forms.TextInput(attrs={'class':'form-control'}),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','comment')
        widgets = {
            'name':      forms.TextInput(attrs={'value':'','id':'name','type':'hidden'}),
            'comment':       forms.Textarea(attrs={'class':'form-control'}),
        }