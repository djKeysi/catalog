from django import forms

from main.models import Student, Subject

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = 'Some help text for field'  # Выводит текст подсказки, для описания вводимых данных

class StudentForm(StyleFormMixin,forms.ModelForm):


    class Meta:
        model = Student
        #fields = '__all__'
        fields = ('first_name', 'last_name', 'avatar','email',)
        #exclude = ('is_active',)




    def clean_email(self):
        clean_data = self.cleaned_data['email']

        if 'sky.pro' not in clean_data:
            raise forms.ValidationError('Почта должна относится к учебному заведению')

        return clean_data



class SubjectForm(StyleFormMixin,forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'


