from rest_framework import serializers

from apps.tracking.models import District


class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District
