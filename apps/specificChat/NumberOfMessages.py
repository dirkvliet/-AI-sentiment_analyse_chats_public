import json 
from bson import json_util

class NumberOfMessages():
    chatName = ""
    chatId = 0;
    messages = {} 
    precentOfTotal = 0

    def __init__(self, chatName, chatId, messages, precentOfTotal = 0):
        self.chatName = chatName
        self.chatId = chatId
        self.messages = messages
        self.precentOfTotal = precentOfTotal
    
    def to_json(self):
        return {
            "chatName": self.chatName,
            "chatId": self.chatId,
            "messages": self.messages,
            "precentOfTotal": self.precentOfTotal,
            }
