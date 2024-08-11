import django_filters 
from .models import category,item

class categoryFilter(django_filters.FilterSet):
    class Meta:
        model = category
        fields = '__all__'

class itemFilter(django_filters.FilterSet):
    class Meta:
        model = item
        fields = ['name','category','unit']