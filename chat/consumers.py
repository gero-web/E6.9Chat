import json
from channels.generic.websocket import AsyncConsumer
from .models import History, RoomChat
from asgiref.sync import sync_to_async

class ChatRoomConsumer(AsyncConsumer):
    
    async def websocket_connect(self,event):
        self.chat_box_name = self.scope["url_route"]["kwargs"]["chat_box_name"]
        room =  await sync_to_async(RoomChat.objects.get_or_create)(name_room=self.chat_box_name)
                
        self.group_name = "chat_%s" % self.chat_box_name
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.send({
            'type':'websocket.accept'
        })
        msg_lst = []
       
        async for room in History.objects.filter(room__name_room= self.chat_box_name ).prefetch_related("user"):
            msg_lst.append( { "message": room.message, "username": room.user.username })
        print( msg_lst)
        await self.send(
            {
            'type':'websocket.send',
            "text":json.dumps(msg_lst)
            
        })
        
        
    async def websocket_disconnect(self, event):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        
    async def websocket_receive(self, event):
        text_data_json = json.loads(event['text'])
        
        message = text_data_json["message"]
        username = text_data_json["username"]
        
        await self.channel_layer.group_send(
            self.group_name,
            {
              "type": "chatbox_message",
               "text":{
                   
                "message": message ,
                "username": username,
               }
            },
        )
        
    # Receive message from room group.
    async def chatbox_message(self, event):
        
        #event = json.loads(event['text'])
        message = event["text"]["message"]
        username = event["text"]["username"]
        
        #send message and username of sender websocker
        room =  await sync_to_async(RoomChat.objects.get)(name_room=self.chat_box_name)
        history = History(message=message, room=room)
        await sync_to_async(history.save)()
        await self.send(
            {
            'type':'websocket.send',
            "text":json.dumps({
                "message": message,
                "username": username,
            })
            
        })
        
      
