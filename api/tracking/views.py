from rest_framework import permissions, viewsets

from apps.tracking.models import District

from api.tracking.serializers import DistrictSerializer


class DistrictViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = [permissions.IsAuthenticated]
