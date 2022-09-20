import json

from channels.generic.websocket import AsyncWebsocketConsumer


class JobStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        

        
        self.group_name = f"job-posting"

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def propagate_status(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps(message))
