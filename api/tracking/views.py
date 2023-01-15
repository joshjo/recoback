from rest_framework import mixins, permissions, viewsets

from apps.tracking.models import District, Journey

from api.tracking.serializers import DistrictSerializer, JourneySerializer
from api.permissions import IsDriverAuthenticated


class DistrictViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = [permissions.IsAuthenticated]


class JourneyViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer
    permission_classes = [IsDriverAuthenticated]

    def perform_create(self, serializer):
        serializer.save(driver=self.request.user.driver)
