from django import forms 
from .models import category,unit,item,Supplier,order,Employee


class TestForm (forms .CharField):
    name = forms.CharField()

class categoryFrom(forms.ModelForm):
    class Meta:
        model = category
        fields = '__all__'


class unitFrom(forms.ModelForm):
    class Meta:
        model = unit
        fields = '__all__'

class itemForm(forms.ModelForm):
    class Meta:
        model = item
        fields  = '__all__'

class SupplierFrom(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'   


class orderFrom(forms.ModelForm):
    class Meta:
        model = order
        fields = '__all__'   

class EmployeeFrom(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'