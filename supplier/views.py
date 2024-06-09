from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from users.models import User
from supplier.models import Supplier
from goods.permissions import IsAdmin, IsOwner
from supplier.serializers import SupplierSerializer
from supplier.filters import SupplierFilter
from django_filters.rest_framework import DjangoFilterBackend


class SupplierViewSet(viewsets.ModelViewSet):
    '''Supplier ViewSet'''
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SupplierFilter

    def get_permissions(self):
        '''
        Права доступа.
        Неавторизированный пользователь может:
        - видеть список поставщиков.

        Авторизированный (IsAuthenticated) пользователь (IsOwner) может:
        - видеть список поставщиков,
        - видеть одного поставщика (детально),
        - создавать поставщиков,
        - редактировать свои поставщиков,
        - удалять своих поставщиков.

        Авторизированный (IsAuthenticated) пользователь (IsAdmin) может:
        - видеть список поставщиков,
        - видеть одного поставщика (детально),
        - создавать поставщиков,
        - редактировать своих и чужих поставщиков,
        - удалять своих и чужих поставщиков.
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
        supplier = serializer.save()
        supplier.author = get_object_or_404(User, id=self.request.user.id)
        supplier.save()
