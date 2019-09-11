from rest_framework.routers import DefaultRouter
from apps.cartao.api.viewsets import CardViewSet


router_card = DefaultRouter()
router_card.register(r'card', CardViewSet, base_name='CardCreate')
