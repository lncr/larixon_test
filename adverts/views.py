from django.db import transaction
from django.db.models import F
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from adverts.models import Advert
from adverts.serializers import AdvertSerializer


class AdvertListView(GenericViewSet, ListModelMixin):
    queryset = Advert.objects.select_related('city', 'category').all()
    serializer_class = AdvertSerializer


class AdvertDetailView(GenericViewSet, RetrieveModelMixin):
    queryset = Advert.objects.select_related('city', 'category').all()
    serializer_class = AdvertSerializer
    lookup_field = 'pk'

    def get(self, request, pk=None):
        with transaction.atomic():
            Advert.objects.filter(pk=pk).update(views=F('views') + 1)
            advert = self.get_object()
        serializer = self.get_serializer(advert)
        return Response(serializer.data)
