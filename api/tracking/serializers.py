from rest_framework import serializers

from apps.tracking.models import District, Journey


class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District


class JourneySerializer(serializers.ModelSerializer):

    class Meta:
        model = Journey
        fields = "__all__"
        read_only_fields = ("id", "driver", "start_at", "end_at")
