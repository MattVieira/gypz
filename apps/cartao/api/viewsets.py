from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apps.cartao.api.serializers import CardSerializers
from apps.cartao.models import CardCreate
import numpy as np

class CardViewSet(ModelViewSet):
    serializer_class = CardSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return CardCreate.objects.all()

    def list(self, request, *args, **kwargs):
        return super(CardViewSet, self).list(request, *args, **kwargs)


    def create(self, request, *args, **kwargs):
        return super(CardViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(CardViewSet, self).destroy(request, *args, **kwargs)