from django import forms

from .models import *
from django.core.exceptions import ValidationError
#форма не связанная с моделью
#улучшение формы через атрибут label
#class AddPostForms(forms.Form):
    #title = forms.CharField(max_length=255, label="Заголовок")
    #slug = forms.SlugField(max_length=255, label="URL")
    #content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Контент")
    #is_published = forms.BooleanField(label="Публикация", required=False, initial=True)
    #cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категория", empty_label="Категория не выбрана")


#категория не выбранна
class AddPostForm(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'], empty_label = "Категория не выбранна"





#класс связанный с Model
class AddPostForm(forms.ModelForm):
    class Meta:
        model = Women
        #использование всех полей модели
        #fields ='__all__'
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

#валидация заголовка (начинается с clean_)
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длинна превышает 200 символов')
        return title