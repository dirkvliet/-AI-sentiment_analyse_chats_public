from models.mongoDB.ChatCRUD import ChatCRUD
from models.mongoDB.MessagesCRUD import MessagesCRUD
from apps.overview.NumberOfMessages import NumberOfMessages
from datetime import timedelta
import json 
from bson import json_util
from models.mongoDB.SyncDBCRUD import SyncDBCRUD


class TableMessagesByChat:

    def __init__(self):
        self.syncDBRepo = SyncDBCRUD()
        self.messagesrepo = MessagesCRUD()
        self.chatrepo = ChatCRUD()

    def getData(self, timerange, chats): 
        chatmessagelist = []
        if not chats:
            chats = self.chatrepo.getAll()

        latestDBUpdate = self.syncDBRepo.getLatest()
        syncdate = latestDBUpdate.timeStamp

        messagesAllChats = self.messagesrepo.getMessagesBetweenTimestamps(syncdate - timedelta(hours = timerange), syncdate)
        messagesTotalAllChats = sum([x.number for x in messagesAllChats])
        for chat in chats:
            messages = self.messagesrepo.getMessagesBetweenTimestampsAndByChatId(syncdate - timedelta(hours = timerange), syncdate, chat.chatId)
            totalmessages = sum([x.number for x in messages])
            chatmessagelist.append(NumberOfMessages(chatName = chat.name, chatId=chat.chatId, messages=totalmessages, precentOfTotal = round((totalmessages / messagesTotalAllChats) * 100, 2)))
       
        data = {"labels": [json.dumps(message.date_to_json(), default=json_util.default) for message in messages],
            "data": [json.dumps(chatmessage.to_json(), default=json_util.default) for chatmessage in chatmessagelist]
                }     
        return (json.dumps(data, default=json_util.default)) 

