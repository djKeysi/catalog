from django import forms
from re import search
from main.models import Product, Version

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        clean_data = self.cleaned_data['name']
        print(clean_data)
        for forbidden_word in FORBIDDEN_WORDS:
            if forbidden_word in clean_data.split():
                raise forms.ValidationError('Вы ввели запрещенное слово(введите нормальное имя продукта)')
        return clean_data

    def clean_discription(self):
        clean_data = self.cleaned_data['discription']
        for forbidden_word in FORBIDDEN_WORDS:
            if forbidden_word in clean_data.split():
                raise forms.ValidationError('Вы ввели запрещенное слово(введите нормальное имя продукта)')
        return clean_data

class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

