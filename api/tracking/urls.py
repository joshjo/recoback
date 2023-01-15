from rest_framework import routers
from api.tracking import views


app_name = "tracking"

router = routers.DefaultRouter()

router.register("districts", views.DistrictViewSet, basename="districts")
router.register("journeys", views.JourneyViewSet, basename="journeys")

urlpatterns = router.urls
