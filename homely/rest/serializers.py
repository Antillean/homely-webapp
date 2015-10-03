# Serializers define the API representation.
from rest_framework import serializers

from homely.models import Receiver, Donation

class ReceiverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Receiver
        fields = ('name', 'photo')

class DonationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Donation
        fields = ('giver', 'receiver', 'amount', 'payment_token')
