import json
import redis

from django.conf import settings


def get_config():
    tracking_settings = getattr(settings, "TRACKING", {})
    return tracking_settings.get("CONFIG", {})

config = get_config()

client = redis.from_url(config.get("redis"))


def _format_key(district_id: str):
    return f"district:{district_id}"


def push_location(district_id: str, journey_id: str, json_body: dict) -> int:
    fdistrict = _format_key(district_id)
    return client.hset(fdistrict, journey_id, json.dumps(json_body))


async def get_location_by_district(district_id: str) -> list[dict]:
    map_district = await client.hgetall(district_id)
    return [json.loads(i) for i in map_district.values]


async def remove_location(district_id: str, journey_id: str) -> int:
    fdistrict = _format_key(district_id)
    return await client.hdel(fdistrict, journey_id)
