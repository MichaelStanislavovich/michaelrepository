'''from django import forms

class AdvertisementForms(forms.Form):
    title=forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class':'forms-control forms-control-lg'}))
    description=forms.CharField(widget=forms.Textarea(attrs={'class':'forms-control forms-control-lg'}))
    price=forms.DecimalField(widget=forms.NumberInput(attrs={'class':'forms-control forms-control-lg'}))
    auction=forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    image=forms.ImageField(widget=forms.FileInput(attrs={'class':'forms-control forms-control-lg'}))'''


from django.core.exceptions import ValidationError
from django import forms

from .models import Advertisement


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ("title", "description", "image", "price", "auction")
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-lg'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control form-control-lg'}),
            'image': forms.FileInput(attrs={
                'class': 'form-control form-control-lg'}),
            'price': forms.NumberInput(attrs={
                'class': 'form-control form-control-lg'}),
            'auction': forms.CheckboxInput(attrs={
                'class': 'form-check-input'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.startswith('?'):
            raise ValidationError('Заголовок не может начинаться с вопросительного знака.')
        return title