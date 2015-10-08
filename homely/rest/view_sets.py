# ViewSets define the view behavior.
from rest_framework import viewsets, filters

from homely.models import *
from homely.rest.serializers import *

class CharityViewSet(viewsets.ModelViewSet):
    queryset = Charity.objects.all()
    serializer_class = CharitySerializer

    filter_backends = (filters.DjangoFilterBackend,)
    # filter_fields = ('name')

class ReceiverViewSet(viewsets.ModelViewSet):
    queryset = Receiver.objects.all()
    serializer_class = ReceiverSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('beacon_id', 'name', 'charity')
    lookup_field = 'beacon_id'

class GiverViewSet(viewsets.ModelViewSet):
    queryset = Giver.objects.all()
    serializer_class = GiverSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('facebook_id', 'name')
    lookup_field = 'facebook_id'

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('giver', 'receiver', 'amount', 'payment_token')
    lookup_field = 'payment_token'
