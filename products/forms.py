from django import forms

from .models import Product
# class ProductForm(forms.Form):
#     title = forms.CharField()

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title', 'content'
        ]
    def clean_title(self):
        data = self.cleaned_data.get('title')
        if len(data) < 4:
            raise forms.ValidateError("This is not long enough")
        
        return data