import json

from channels.generic.websocket import AsyncWebsocketConsumer
from apps.tracking.models import Journey


class TrackingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        journey_id = self.scope["url_route"]["kwargs"]["journey_id"]
        self.journey = (
            Journey.objects.select_related("truck__district")
                .filter(id=journey_id)
                .first()
        )
        self.district = self.journey.truck.district
        self.room_group_name = f"live_{self.district.id}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["latlong"]

        # PENDING: Save the data in a datastore

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "update_location", "latlong": message}
        )

    # Receive message from room group
    async def update_location(self, event):

        # Retrieve all the truck positions from the selected district
        latlong = event["latlong"]


        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": latlong}))


class LiveConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        district_id = self.scope["url_route"]["kwargs"]["district_id"]
        self.room_group_name = f"live_{district_id}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        pass
        # text_data_json = json.loads(text_data)
        # message = text_data_json["message"]

        # # Send message to room group
        # await self.channel_layer.group_send(
        #     self.room_group_name, {"type": "chat_message", "message": message}
        # )

