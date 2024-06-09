from rest_framework import serializers
from supplier.models import Supplier
from goods.serializers import ProductSerializer


class SupplierSerializer(serializers.ModelSerializer):
    '''
    Сериализатор модели Supplier(Поставщик).
    '''

    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    product = ProductSerializer(many=True, required=False)
    supplier = serializers.SlugRelatedField(slug_field='title', queryset=Supplier.objects.all())

    class Meta:
        model = Supplier
        fields = '__all__'
