# Serializers define the API representation.
from rest_framework import serializers

from homely.models import Charity, Receiver, Giver, Donation

class CharitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Charity
        # fields = ('name')

class ReceiverSerializer(serializers.HyperlinkedModelSerializer):
    # charity = CharitySerializer()

    class Meta:
        model = Receiver
        extra_kwargs = {
            'url': {'lookup_field': 'beacon_id'}
        }

class GiverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Giver
        extra_kwargs = {
            'url': {'lookup_field': 'facebook_id'}
        }

class DonationSerializer(serializers.HyperlinkedModelSerializer):
    # receiver = ReceiverSerializer()
    # giver = GiverSerializer()

    class Meta:
        model = Donation
        extra_kwargs = {
            'url': {'lookup_field': 'payment_token'},
            'receiver': {'lookup_field': 'beacon_id'},
            'giver': {'lookup_field': 'facebook_id'}
        }
