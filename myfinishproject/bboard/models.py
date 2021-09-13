from django.db import models
from django.core.validators import RegexValidator
import requests
from bs4 import BeautifulSoup
from django.core.validators import MaxValueValidator, MinValueValidator




class Bb(models.Model):


    title = models.CharField(max_length=50, verbose_name='Товар', help_text='Введите название товара')


    content = models.TextField(null=True, blank=True, verbose_name='Описание', help_text='Краткое описание товара')
    price = models.FloatField(null=True,default=1, blank=False, verbose_name='Цена',
                              help_text='Введице цену товара в рублях',
                              validators = [MinValueValidator(1.0),
                                            MaxValueValidator(100000)])

    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Номер телефона должен быть в формате: '+999999999'. Максимум 15 цифр.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name='Телефон')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')


    def price_dollar(self):
        url = 'https://banki24.by/grodno/kurs'
        source = requests.get(url)
        main_text = source.text

        soup = BeautifulSoup(main_text)
        table = soup.find('table', {'class': 'table'})
        td = table.find('tr', {'class': 'static'})
        td = td.text
        td = td[:9]
        conv = td[2]+'.'+td[4:6]
        conv = float(conv)
        doll = self.price/conv
        doll = round(doll, 2)

        return str('Цена в долларах: '+ str(doll) +' $.')




    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявлениe'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
