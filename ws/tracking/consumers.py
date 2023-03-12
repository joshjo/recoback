import json
from urllib.parse import parse_qs

from channels.generic.websocket import AsyncWebsocketConsumer
from apps.tracking.models import District, Journey


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
        self.user = self.scope["user"]
        self.room_group_name = f"live_{district_id}"
        self.district = await District.objects.filter(id=district_id).afirst()
        self.journey = None
        if self.user.is_authenticated and self.district:
            query_str = parse_qs(self.scope["query_string"].decode("ascii"))
            journey_id = query_str.get("journey_id", "")
            if query_str and journey_id:
                self.journey = await Journey.objects.filter(id=journey_id[0]).afirst()
            # Join room group
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        print("text_data", text_data)
        print("---> self.journey", self.journey)
        # text_data_json = json.loads(text_data)
        # message = text_data_json["message"]

        # # Send message to room group
        # await self.channel_layer.group_send(
        #     self.room_group_name, {"type": "chat_message", "message": message}
        # )

