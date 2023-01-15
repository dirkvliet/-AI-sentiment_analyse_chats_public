import json 
from bson import json_util

class ChatMessage():
    chatName = ""
    chatId = 0;
    messages = {} 
    selected = False

    def __init__(self, chatName, chatId, messages, selected = False):
        self.chatName = chatName
        self.chatId = chatId
        self.messages = messages
        self.selected = selected
    
    def to_json(self):
        return {
            "chatName": self.chatName,
            "chatId": self.chatId,
            "messages": [json.dumps(message.to_json(), default=json_util.default) for message in self.messages],
            "selected": self.selected
            }
