import django_filters
from supplyers.models import Supplier


class SupplierFilter(django_filters.FilterSet):
    '''
    Джанго-фильтр по полю город
    '''
    city = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Supplier
        fields = ['city']
