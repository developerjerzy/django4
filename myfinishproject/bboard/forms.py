from django.forms import ModelForm
from  .models import Bb


class BbForm(ModelForm):
    """Класс описывает поля формы"""
    class Meta:
        model = Bb
        fields = ('title','content', 'price','phone', 'rubric')

