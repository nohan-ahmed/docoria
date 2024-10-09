import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        self.group_name = f"user_{self.user.id}"  # Unique group for each user

        # Join user group
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        print(f'accepted: {self.user}')
        await self.accept()

    async def disconnect(self, close_code):
        # Leave user group
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)

    async def send_notification(self, event):
        notification = event['notification']
        await self.send(text_data=json.dumps({
            'notification': notification
        }))
