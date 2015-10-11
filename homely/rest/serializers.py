# Serializers define the API representation.
from rest_framework import ISO_8601
from rest_framework import serializers

from homely.models import Charity, Receiver, Giver, Donation

class CharitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Charity

        extra_kwargs = {
            'created': {'read_only': True},
            'updated': {'read_only': True}
        }


class ReceiverSerializer(serializers.HyperlinkedModelSerializer):
    amount_remaining = serializers.DecimalField(max_digits=8, decimal_places=2, read_only=True)
    target_percentage = serializers.DecimalField(max_digits=3, decimal_places=2, read_only=True)
    charity = serializers.CharField(read_only=True)
    # donations = DonationSerializer(read_only=True, many=True)
    # donations = serializers.HyperlinkedRelatedField(
    #     view_name='donation-detail',
    #     lookup_field='payment_token',
    #     many=True,
    #     read_only=True
    # )

    # givers = serializers.HyperlinkedRelatedField(
    #     view_name='giver-detail',
    #     lookup_field='facebook_id',
    #     many=True,
    #     read_only=True
    # )

    class Meta:
        model = Receiver
        extra_kwargs = {
            'created': {'read_only': True},
            'updated': {'read_only': True},
            'url': {'lookup_field': 'beacon_id'}
        }

class GiverSerializer(serializers.HyperlinkedModelSerializer):
    # donations = DonationSerializer(read_only=True, many=True)
    donations = serializers.HyperlinkedRelatedField(
        view_name='donation-detail',
        lookup_field='payment_token',
        many=True,
        read_only=True
    )

    receivers = serializers.HyperlinkedRelatedField(
        view_name='receiver-detail',
        lookup_field='beacon_id',
        many=True,
        read_only=True
    )

    class Meta:
        model = Giver
        extra_kwargs = {
            'created': {'read_only': True},
            'updated': {'read_only': True},
            'url': {'lookup_field': 'facebook_id'}
        }

class DonationLinkSerializer(serializers.HyperlinkedModelSerializer):
    donation_date = serializers.DateField(format="%d %b %Y", input_formats=(ISO_8601,""))

    class Meta:
        model = Donation
        extra_kwargs = {
            'created': {'read_only': True},
            'updated': {'read_only': True},
            'url': {'lookup_field': 'payment_token'},
            'receiver': {'lookup_field': 'beacon_id'},
            'giver': {'lookup_field': 'facebook_id'}
        }

class DonationFullSerializer(DonationLinkSerializer):
    ## Use full serialisers for receiver and giver.
    receiver = ReceiverSerializer()
    giver = GiverSerializer()

    class Meta(DonationLinkSerializer.Meta):
        pass
