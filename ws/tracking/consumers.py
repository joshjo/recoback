import json
from urllib.parse import parse_qs

from django.contrib.auth.models import User

from channels.generic.websocket import AsyncWebsocketConsumer
from apps.tracking.models import District, Driver, Journey


# class TrackingConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         journey_id = self.scope["url_route"]["kwargs"]["journey_id"]
#         self.journey = (
#             Journey.objects.select_related("truck__district")
#                 .filter(id=journey_id)
#                 .first()
#         )
#         self.district = self.journey.truck.district
#         self.room_group_name = f"live_{self.district.id}"

#         # Join room group
#         await self.channel_layer.group_add(self.room_group_name, self.channel_name)
#         await self.accept()

#     async def disconnect(self, close_code):
#         # Leave room group
#         await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

#     # Receive message from WebSocket
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["latlong"]

#         # PENDING: Save the data in a datastore

#         # Send message to room group
#         await self.channel_layer.group_send(
#             self.room_group_name, {"type": "update_location", "latlong": message}
#         )

#     # Receive message from room group
#     async def update_location(self, event):

#         # Retrieve all the truck positions from the selected district
#         latlong = event["latlong"]


#         # Send message to WebSocket
#         await self.send(text_data=json.dumps({"message": latlong}))


class LiveConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        district_id = self.scope["url_route"]["kwargs"]["district_id"]
        self.user = self.scope["user"]

        self.driver = await Driver.objects.filter(user=self.user).afirst()
        self.is_driver = self.driver is not None

        self.room_group_name = f"live_{district_id}"
        self.district = await District.objects.filter(id=district_id).afirst()
        self.journey = None
        if self.user.is_authenticated and self.district:
            query_str = parse_qs(self.scope["query_string"].decode("ascii"))
            journey_id = query_str.get("journey_id", "")
            print("rj", journey_id)
            if query_str and self.driver and journey_id:
                self.journey = await Journey.objects.filter(
                    id=journey_id[0],
                    driver=self.driver,
                    end_at__isnull=True,
                ).afirst()
            # Join room group
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        print("---> self.driver", str(self.driver.id))
        print("---> self.journey", str(self.journey.id))
        if self.is_driver and self.journey:
            json_data = json.loads(text_data)
            body = json_data.get("data")
            body["driver_id"] = str(self.driver.id)
            await self.channel_layer.group_send(
                self.room_group_name, {
                    "type": "update_location",
                    "message": body,
                }
            )
        elif self.driver and not self.journey:
            await self.send(text_data=json.dumps({"error": {
                "message": "Invalid journey",
                "code": 400
            }}))
        else:
            await self.send(text_data=json.dumps({"error": {
                "message": "Not Allowed",
                "code": 403
            }}))

    async def update_location(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps(message))
