# ViewSets define the view behavior.
from rest_framework import viewsets

from homely.models import Receiver, Donation
from homely.rest.serializers import *

class ReceiverViewSet(viewsets.ModelViewSet):
    queryset = Receiver.objects.all()
    serializer_class = ReceiverSerializer

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
