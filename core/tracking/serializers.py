from rest_framework import serializers


class LocationSerializer(serializers.Serializer):
    journey_id = serializers.UUIDField()
    driver_id = serializers.UUIDField()
    lat = serializers.FloatField()
    lng = serializers.FloatField()
    datetime = serializers.DateTimeField()
