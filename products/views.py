from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from products.models import Product
from users.models import User
from products.permissions import IsAdmin, IsOwner
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    '''Product ViewSet'''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        '''
        Права доступа.
        Неавторизированный пользователь может:
        - видеть список продуктов.

        Авторизированный (IsAuthenticated) пользователь (IsOwner) может:
        - видеть список продуктов,
        - видеть один продукт (детально),
        - создавать продукты,
        - редактировать свои продукты,
        - удалять свои продукты.

        Авторизированный (IsAuthenticated) пользователь (IsAdmin) может:
        - видеть список продуктов,
        - видеть один продукт (детально),
        - создавать продукт,
        - редактировать свои и чужие продукты,
        - удалять свои и чужие продукты.
        '''

        if self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsOwner | IsAdmin]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        '''
        Создание продукта и установление автора.
        '''
        product = serializer.save()
        product.author = get_object_or_404(User, id=self.request.user.id)
        product.save()
