from django.urls import include, path


urlpatterns = [
    path("auth/", include("api.auth.urls")),
    path("tracking/", include("api.tracking.urls")),
]
