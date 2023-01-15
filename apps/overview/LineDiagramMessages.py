from models.mongoDB.ChatCRUD import ChatCRUD
from models.mongoDB.MessagesCRUD import MessagesCRUD
from apps.overview.ChatMessage import ChatMessage
from datetime import timedelta
import json 
from bson import json_util
from models.mongoDB.SyncDBCRUD import SyncDBCRUD


class LineDiagramMessages:

    def __init__(self):
        self.messagesrepo = MessagesCRUD()
        self.chatrepo = ChatCRUD()
        self.syncDBRepo = SyncDBCRUD()

    def getData(self, timerange, chats): 
        chatmessagelist = []
        if not chats:
            chats = self.chatrepo.getAll()

        latestDBUpdate = self.syncDBRepo.getLatest()
        syncdate = latestDBUpdate.timeStamp

        for chat in chats:
            messages = self.messagesrepo.getMessagesBetweenTimestampsAndByChatId(syncdate - timedelta(hours = timerange), syncdate, chat.chatId)
            chatmessagelist.append(ChatMessage(chatName = chat.name, chatId=chat.chatId, messages=messages))
       
        data = {"labels": [json.dumps(message.date_to_json(), default=json_util.default) for message in messages],
            "data": [json.dumps(chatmessage.to_json(), default=json_util.default) for chatmessage in chatmessagelist]
                }     
        return (json.dumps(data, default=json_util.default)) 

