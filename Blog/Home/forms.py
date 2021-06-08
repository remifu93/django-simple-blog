from django import forms
from django.forms import widgets
from .models import Comment

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['title', 'content']
        labels = {
            'title': '',
            'content': '',
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Titulo del mensaje',
                    'class': 'form-control'
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'placeholder': 'Escribe aqui tu comentario...',
                    'class': 'form-control',
                    'rows': 4
                }
            )
        }