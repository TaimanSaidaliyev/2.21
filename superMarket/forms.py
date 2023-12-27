from django import forms
from superMarket.models import Product


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'price', 'quantity', 'photo')
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'description': forms.Textarea(attrs={"class": "form-control"}),
            'category': forms.Select(attrs={"class": "form-control"}),
            'price': forms.NumberInput(attrs={"class": "form-control"}),
            'quantity': forms.NumberInput(attrs={"class": "form-control"}),
            'photo': forms.FileInput(attrs={"class": "form-control"})
        }