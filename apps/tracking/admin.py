from django.contrib import admin
from leaflet.admin import LeafletGeoAdminMixin

from apps.tracking.models import (
    Driver,
    District,
    Journey,
    House,
    Path,
    Truck,
)


@admin.register(Driver)
class DriverModelAdmin(admin.ModelAdmin):
    pass


@admin.register(District)
class DistrictModelAdmin(LeafletGeoAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Truck)
class TruckModelAdmin(admin.ModelAdmin):
    pass


@admin.register(House)
class HouseModelAdmin(LeafletGeoAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Path)
class PathAdmin(LeafletGeoAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Journey)
class JourneyAdmin(admin.ModelAdmin):
    pass
