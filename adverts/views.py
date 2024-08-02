from django.db import transaction
from django.http import Http404
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from adverts.models import Advert
from adverts.serializers import AdvertSerializer


class AdvertListView(GenericViewSet, ListModelMixin):
    queryset = Advert.objects.select_related('city', 'category').all()
    serializer_class = AdvertSerializer


class AdvertDetailView(RetrieveModelMixin, GenericViewSet):
    queryset = Advert.objects.select_related('city', 'category').all()
    serializer_class = AdvertSerializer
    lookup_url_kwarg = 'pk'

    def get_object(self):
        with transaction.atomic():
            advert = self.queryset.filter(pk=self.kwargs['pk']).select_for_update().first()
            if advert:
                advert.views += 1
                advert.save()
                return advert
            else:
                raise Http404(f"Could not find Advert with pk={self.kwargs['pk']}"
