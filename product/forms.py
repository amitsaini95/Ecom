from django.forms import ModelForm
from .models import *
class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields='__all__'
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
class CheckoutForm(ModelForm):
    class Meta:
        model=ShippingAddress
        fields='__all__'
    def __init__(self, *args, **kwargs):
        super(CheckoutForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
class EditForm(ModelForm):
    class Meta:
        model=Product
        fields='__all__'
    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'