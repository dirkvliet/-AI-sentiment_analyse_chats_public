from models.mongoDB.ChatCRUD import ChatCRUD
from models.mongoDB.SentimentMessagesCRUD import SentimentMessagesCRUD
from models.mongoDB.MessagesCRUD import MessagesCRUD
from apps.specificChat.ChatMessage import ChatMessage
from datetime import timedelta
import json 
from bson import json_util
from models.mongoDB.SyncDBCRUD import SyncDBCRUD


class LineDiagramSentimentMessages:

    def __init__(self):
        self.sentimentmessagesrepo = SentimentMessagesCRUD()
        self.messagesrepo = MessagesCRUD()
        self.chatrepo = ChatCRUD()
        self.syncDBRepo = SyncDBCRUD()

    def getData(self, timerange, chats, prediction =  0): 
        chatmessagelist = []
        if not chats:
            chats = self.chatrepo.getAll()

        latestDBUpdate = self.syncDBRepo.getLatest()
        syncdate = latestDBUpdate.timeStamp
        sentiment = ['All', 'Negative', 'Neutral', 'Positive']
         
        for chat in chats:
            if prediction == 0: 
                for predicted in range(1,4):
                    messages = self.sentimentmessagesrepo.getSentimentMessagesBetweenTimestampsByChatIdAndPrediction(syncdate - timedelta(hours = timerange), syncdate, chat.chatId, predicted)
                    chatmessagelist.append(ChatMessage(chatName = sentiment[predicted], chatId=predicted, messages=messages))

            messages = self.messagesrepo.getMessagesBetweenTimestampsAndByChatId(syncdate - timedelta(hours = timerange), syncdate, chat.chatId)
            chatmessagelist.append(ChatMessage(chatName = sentiment[prediction], chatId=prediction, messages=messages))

       
        data = {"labels": [json.dumps(message.date_to_json(), default=json_util.default) for message in messages],
            "data": [json.dumps(chatmessage.to_json(), default=json_util.default) for chatmessage in chatmessagelist]
                }     
        return (json.dumps(data, default=json_util.default)) 

