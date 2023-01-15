from models.mongoDB.ChatCRUD import ChatCRUD
from models.mongoDB.MessageCRUD import MessageCRUD
from models.mongoDB.MessagesCRUD import MessagesCRUD
from models.mongoDB.SentimentMessagesCRUD import SentimentMessagesCRUD
from models.mongoDB.UserCRUD import UserCRUD
from datetime import timedelta
import json 
from bson import json_util
from models.mongoDB.SyncDBCRUD import SyncDBCRUD
from apps.specificChat.SentimentOptions import SentimentOptions

class MostUsedLocations:

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

        mostusedlocations = []
        if int(sentiments[0].sentimentId) == 0:
            print(chats)
            for chat in chats:
                for mverbs in self.messagesrepo.getMostUsedLocationsDescBetweenTimestampsAndByChatId(syncdate - timedelta(hours = timerange), syncdate, chat.chatId):
                    mostusedlocations.append(mverbs)
        else:
            for chat in chats:
                for mverbs in self.sentimentmessages.getMostUsedPlacesDescBetweenTimestampsByChatIdAndPrediction(syncdate - timedelta(hours = timerange), syncdate ,chat.chatId, sentiments[0].sentimentId):
                    mostusedlocations.append(mverbs)


        mostusedlocations = sorted(mostusedlocations, key=lambda x: x[0], reverse=True)
        data = []
        labels = []
        count = 0
        for location in mostusedlocations:
            if labels.count(location[1]) > 0:
                index = labels.index(location[1])
                data[index] =  data[index] + location[0]
            else:
                labels.append(location[1])
                data.append(location[0])
                count += 1

            if count > 20:
                break

        jsondata = {"labels": [json.dumps(label, default=json_util.default) for label in labels],
             "data": [json.dumps(record, default=json_util.default) for record in data]
           }   
        return (json.dumps(jsondata, default=json_util.default)) 

