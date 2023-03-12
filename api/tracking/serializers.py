from django.utils import timezone

from rest_framework import serializers

from core.tracking.utils import push_location
from core.tracking.serializers import LocationSerializer

from apps.tracking.models import District, Journey


class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District


class JourneySerializer(serializers.ModelSerializer):

    class Meta:
        model = Journey
        fields = "__all__"
        read_only_fields = ("id", "driver", "start_at", "end_at")

    def push_to_store(self):
        if not self.instance:
            return
        journey_id = self.instance.id
        path = self.instance.path
        district_id = path.district.id
        raw_body = {
            "journey_id": journey_id,
            "driver_id": self.instance.driver_id,
            "district_id": district_id,
            "datetime": timezone.now(),
        }
        if path.polygon:
            raw_body.update({
                "lat": path.polygon[0][1],
                "lng": path.polygon[0][0],
            })
        body = LocationSerializer(raw_body)
        import ipdb; ipdb.set_trace()
        push_location(
            district_id,
            self.instance.id,
            body.data,
        )
