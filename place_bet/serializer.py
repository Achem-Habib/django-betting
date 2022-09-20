from rest_framework import serializers

from .models import PlaceBet


class PlaceBetSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlaceBet
        fields = "__all__"

