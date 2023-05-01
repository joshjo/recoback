from rest_framework import serializers


class CoordsSerializer(serializers.Serialiezer):
    speed = serializers.FloatField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    accuracy = serializers.IntegerField()
    heading = serializers.FloatField()
    altitude = serializers.FloatField()
    altitudeAccuracy = serializers.IntegerField()


class UpdateLocationSerializer(serializers.Serializer):
    coords = CoordsSerializer()
    timestamp = serializers.IntegerField()
