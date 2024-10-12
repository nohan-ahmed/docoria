import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        print('connected...')

        # Check if the user is authenticated
        if not self.user or self.user.is_anonymous:
            await self.close()  # Close the connection if the user is not authenticated
        else:
            # Always set self.group_name, even if not authenticated, to avoid AttributeError
            self.group_name = f"user_{self.user.id}"

            # Join the user's group if authenticated
            await self.channel_layer.group_add(self.group_name, self.channel_name)
            await self.accept()

    async def disconnect(self, close_code):
        print('disconnected...')
        # Ensure group_name is set before trying to leave the group
        if hasattr(self, 'group_name'):
            await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        # Handle incoming messages from WebSocket
        data = json.loads(text_data)

    async def send_notification(self, event):
        # Send notification to WebSocket client
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
