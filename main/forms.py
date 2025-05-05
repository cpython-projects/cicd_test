from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):

    def clean_name(self):
        name = self.cleaned_data['name']
        return name.title()
    class Meta:
        model = Reservation
        fields = (
            'name',
            'email',
            'phone',
            'date',
            'time',
            'guests_number',
            'message'
        )

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': 'Your Name',
                'data-rule': 'minlen:4',
                'data-msg': 'Please enter at least 4 chars'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'class': 'form-control'}),
            'guests_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }