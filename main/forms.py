from django import forms


class NewShopAddressForm(forms.Form):
    address = forms.CharField(max_length=200)
    x_coord = forms.FloatField(min_value=1, required=True)
    y_coord = forms.FloatField(min_value=1, required=True)