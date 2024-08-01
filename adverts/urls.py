from django.urls import path

from adverts.views import AdvertListView, AdvertDetailView

urlpatterns = [
    path('advert-list/', AdvertListView.as_view({'get': 'list'}), name='advert-list'),
    path('advert/<int:pk>/', AdvertDetailView.as_view({'get': 'retrieve'}), name='advert-detail'),
]
