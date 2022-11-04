from django import forms
from . models import listing,Bid

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ('start',)

        
class ListingForm(forms.ModelForm):
    class Meta:
        model = listing
        exclude = ('date','active','User')
        widgets = {
            'category': forms.Select(attrs = {'class' : 'con form-control'}),
            'price': forms.NumberInput (attrs = {'class' : 'form-control'})

        }
       