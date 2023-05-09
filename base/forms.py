from django.forms import ModelForm
from .models import Room, Pool
from django import forms

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

class PoolForm(ModelForm):
    class Meta:
        model = Pool
        fields = '__all__'

        # CHOICES = [
        # ('1', 'Отвратительно'),
        # ('2', 'Плохо'),
        # ('3', 'Нормально'),
        # ('4', 'Отлично'),
        # ('5', 'Восхитительно'),
        # ]

        # content = forms.ChoiceField(
        #     widget=forms.RadioSelect,
        #     choices=CHOICES
        # )

        labels = {
        "design": "Дизайн",
        "functionality": "Функционал",
        "creativity": "Креативность",
        "content": "Наполнение",
        "other": "Другое",
        "uname": "Ваше имя"
        }   