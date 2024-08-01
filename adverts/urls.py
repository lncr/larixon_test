from django.urls import path

from adverts.views import AdvertListView, AdvertDetailView

urlpatterns = [
    path('advert-list/', AdvertListView.as_view(), name='advert-list'),
    path('advert/<pk:int>/', AdvertDetailView.as_view(), name='advert-detail'),
]
