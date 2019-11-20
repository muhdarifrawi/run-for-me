from django import forms

from .models import orders


class addRequestForm(forms.ModelForm):
    
    sku = forms.CharField()
    bid = forms.CharField(widget=forms.Textarea)
    cost = forms.IntegerField()
    image = forms.ImageField(required=False)
    # post_date = forms.DateTimeField()
    due_date = forms.DateTimeField(widget=forms.SelectDateWidget)
    
    class Meta:
        model = orders
        fields = ['sku','bid','cost','image','due_date']