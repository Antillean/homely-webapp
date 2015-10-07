# Serializers define the API representation.
from rest_framework import serializers

from homely.models import Charity, Receiver, Giver, Donation

class CharitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Charity
        # fields = ('name')

class ReceiverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Receiver
        fields = ('beacon_id', 'name', 'photo', 'charity', 'info', 'amount_received', 'amount_targeted')
        read_only_fields = ('amount_remaining')

class GiverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Giver
        fields = ('facebook_id', 'name', 'photo', 'amount_given')

class DonationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Donation
        fields = ('giver', 'receiver', 'amount', 'payment_token')
