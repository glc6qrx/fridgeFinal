from django import forms

class ItemForm(forms.Form):
    item_name = forms.CharField(label='Item name', max_length=100)