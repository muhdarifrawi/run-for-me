from django import forms

from .models import orders


class OrderForm(forms.ModelForm):
    

    class Meta:
        model = orders
        fields = ('sku','full_name','full_address','postcode','run_request','image','due_date', 'urgency')
        

class PaymentForm(forms.Form):
    
    MONTH_CHOICES = [(M, M) for M in range(1, 13)]
    YEAR_CHOICES = [(Y, Y) for Y in range(2019,2036)]
    
    credit_card_number = forms.CharField(label='Credit Card Number', required=False)
    cvv = forms.CharField(label='Security Code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)