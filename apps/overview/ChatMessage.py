import json 
from bson import json_util

class ChatMessage():
    chatName = ""
    chatId = 0;
    messages = {} 

    def __init__(self, chatName, chatId, messages):
        self.chatName = chatName
        self.chatId = chatId
        self.messages = messages
    
    def to_json(self):
        return {
            "chatName": self.chatName,
            "chatId": self.chatId,
            "messages": [json.dumps(message.to_json(), default=json_util.default) for message in self.messages],
            }
