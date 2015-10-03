# ViewSets define the view behavior.
from rest_framework import viewsets, filters

from homely.models import Receiver, Giver, Donation
from homely.rest.serializers import *

class ReceiverViewSet(viewsets.ModelViewSet):
    queryset = Receiver.objects.all()
    serializer_class = ReceiverSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('beacon_id','name', 'photo')

class GiverViewSet(viewsets.ModelViewSet):
    queryset = Giver.objects.all()
    serializer_class = GiverSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('facebook_id','name', 'photo')

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('giver', 'receiver', 'amount', 'payment_token')
