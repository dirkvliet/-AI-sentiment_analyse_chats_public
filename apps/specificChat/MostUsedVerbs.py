from models.mongoDB.ChatCRUD import ChatCRUD
from models.mongoDB.MessageCRUD import MessageCRUD
from models.mongoDB.MessagesCRUD import MessagesCRUD
from models.mongoDB.SentimentMessagesCRUD import SentimentMessagesCRUD
from models.mongoDB.UserCRUD import UserCRUD
from apps.specificChat.SentimentOptions import SentimentOptions
from datetime import timedelta
import json 
from bson import json_util
from models.mongoDB.SyncDBCRUD import SyncDBCRUD

class MostUsedVerbs:

    def __init__(self):
        self.messagesrepo = MessagesCRUD()
        self.sentimentmessages = SentimentMessagesCRUD()
        self.chatrepo = ChatCRUD()
        self.syncDBRepo = SyncDBCRUD()
        self.userrepo = UserCRUD()

    def getData(self, timerange, chats, sentiments): 

        if not chats:
            chats = self.chatrepo.getAll()

        if not sentiments: 
            sentiments = [SentimentOptions(sentimentId = 0, sentiment = 'All', option = True)]

        latestDBUpdate = self.syncDBRepo.getLatest()
        syncdate = latestDBUpdate.timeStamp

        mostusedverbs = []

        if int(sentiments[0].sentimentId) == 0:
            for chat in chats:
                for mverbs in self.messagesrepo.getMostUsedVerbsDescBetweenTimestampsAndByChatId(syncdate - timedelta(hours = timerange), syncdate, chat.chatId):
                    mostusedverbs.append(mverbs)
        else:
            for chat in chats:
                for mverbs in self.sentimentmessages.getMostUsedVerbsDescBetweenTimestampsByChatIdAndPrediction(syncdate - timedelta(hours = timerange), syncdate ,chat.chatId, sentiments[0].sentimentId):
                    mostusedverbs.append(mverbs)

        mostusedverbs = sorted(mostusedverbs, key=lambda x: x[0], reverse=True)
        data = []
        labels = []
        count = 0
        for verbs in mostusedverbs:
            if labels.count(verbs[1]) > 0:
                index = labels.index(verbs[1])
                data[index] =  data[index] + verbs[0]
            else:
                labels.append(verbs[1])
                data.append(verbs[0])
                count += 1

            if count > 20:
                break



        jsondata = {"labels": [json.dumps(label, default=json_util.default) for label in labels],
             "data": [json.dumps(record, default=json_util.default) for record in data]
           }   
        return (json.dumps(jsondata, default=json_util.default)) 

