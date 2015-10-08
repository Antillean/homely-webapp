# Serializers define the API representation.
from rest_framework import serializers

from homely.models import Charity, Receiver, Giver, Donation

class CharitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Charity
        # fields = ('name')

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

class ReceiverSerializer(serializers.HyperlinkedModelSerializer):
    amount_remaining = serializers.DecimalField(max_digits=8, decimal_places=2, read_only=True)
    donations = DonationSerializer(read_only=True, many=True)

    givers = serializers.HyperlinkedRelatedField(
        view_name='giver-detail',
        lookup_field='facebook_id',
        many=True,
        read_only=True
    )

    class Meta:
        model = Receiver
        extra_kwargs = {
            'url': {'lookup_field': 'beacon_id'}
        }

class GiverSerializer(serializers.HyperlinkedModelSerializer):
    donations = DonationSerializer(read_only=True, many=True)

    receivers = serializers.HyperlinkedRelatedField(
        view_name='receiver-detail',
        lookup_field='beacon_id',
        many=True,
        read_only=True
    )

    class Meta:
        model = Giver
        extra_kwargs = {
            'url': {'lookup_field': 'facebook_id'}
        }
