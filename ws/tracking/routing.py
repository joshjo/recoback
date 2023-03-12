from django.urls import re_path

from ws.tracking import consumers

url_patterns = [
    # re_path(r"ws/tracking/(?P<journey_id>[\w\-]+)/$", consumers.TrackingConsumer.as_asgi()),
    re_path(r"ws/live/(?P<district_id>[\w\-]+)/$", consumers.LiveConsumer.as_asgi()),
]
