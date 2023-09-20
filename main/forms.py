from django import forms
from main.models import Product, Version

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
class ProductForm(StyleFormMixin,forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        clean_data = self.cleaned_data['name'].lower()
        print(clean_data)
        for forbidden_word in FORBIDDEN_WORDS:
            if forbidden_word in clean_data.split():
                raise forms.ValidationError('Вы ввели запрещенное слово(введите нормальное имя продукта)')
        return clean_data

    def clean_discription(self):
        clean_data = self.cleaned_data['discription'].lower()
        for forbidden_word in FORBIDDEN_WORDS:
            if forbidden_word in clean_data.split():
                raise forms.ValidationError('Вы ввели запрещенное слово(введите нормальное описание продукта)')
        return clean_data

class VersionForm(StyleFormMixin,forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

