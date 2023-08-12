from .models import New
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class NewForm(ModelForm):
    class Meta:
        model = New
        fields = ['title', 'full_text', 'anons', 'date', 'image']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текси статьи'
            }),
            "image": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Фото'
            })
        }