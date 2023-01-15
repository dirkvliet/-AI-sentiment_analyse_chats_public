from models.mongoDB.ChatCRUD import ChatCRUD
from models.mongoDB.MessagesCRUD import MessagesCRUD
from apps.specificChat.ChatMessage import ChatMessage
from datetime import timedelta
import json 
from bson import json_util
from models.mongoDB.SyncDBCRUD import SyncDBCRUD


class Chats:

    def __init__(self):
        self.messagesrepo = MessagesCRUD()
        self.chatrepo = ChatCRUD()
        self.syncDBRepo = SyncDBCRUD()

    def getData(self, timerange, chats): 
        chatlist = []
        if not chats:
            chats = self.chatrepo.getAll()

        latestDBUpdate = self.syncDBRepo.getLatest()
        syncdate = latestDBUpdate.timeStamp
        count = 0 
        for chat in chats:
            chatlist.append(ChatMessage(chatName = chat.name, chatId=chat.chatId, messages = [], selected = (True if count < 1 else False )))
            count += 1
       
        data = { "data": [json.dumps(chatmessage.to_json(), default=json_util.default) for chatmessage in chatlist] }     
        return (json.dumps(data, default=json_util.default)) 

