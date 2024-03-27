from django import forms
from.models import ProductCustomization

class SearchForm(forms.Form):
    query = forms.CharField(label = '', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))


class CustomizationForm(forms.ModelForm):
    class Meta:
        model = ProductCustomization
        fields = ['nighty_length', 'sleeve_type', 'feeding_type', 'zip_type']
        widgets = {
            'nighty_length': forms.Select(choices = ProductCustomization.Nighty_Length_choices, attrs = {'class': 'form-control'}),
            'sleeve_type' : forms.Select(choices = ProductCustomization.Sleeve_Type_Choices, attrs = {'class': 'form-control'}),
            'feeding_type': forms.Select(choices = ProductCustomization.Feeding_Type_Choices, attrs = {'class': 'form-control'}),
            'zip_type': forms.Select(choices = ProductCustomization.Zip_Type_Choices, attrs = {'class': 'form-control'}),
        }