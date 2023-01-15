from apps.specificChat.MostUsedCombination import MostUsedCombination
from models.mongoDB.ChatCRUD import ChatCRUD
from models.mongoDB.MessagesCRUD import MessagesCRUD
from models.mongoDB.SentimentMessagesCRUD import SentimentMessagesCRUD
from models.mongoDB.UserCRUD import UserCRUD
from datetime import timedelta
import json 
from bson import json_util
from apps.specificChat.SentimentOptions import SentimentOptions
from models.mongoDB.SyncDBCRUD import SyncDBCRUD

class MostUsedCombinationOfWords:

    def __init__(self):
        self.messagesrepo = MessagesCRUD()
        self.sentimentmessages = SentimentMessagesCRUD()
        self.chatrepo = ChatCRUD()
        self.syncDBRepo = SyncDBCRUD()
        self.userrepo = UserCRUD()

    def getData(self, timerange, chats, sentiments):

        if not chats:
            chats = self.chatrepo.getAll

        if not sentiments: 
            sentiments = [SentimentOptions(sentimentId = 0, sentiment = 'All', option = True)]

        latestDBUpdate = self.syncDBRepo.getLatest()
        syncdate = latestDBUpdate.timeStamp

        messages = self.messagesrepo.getMessagesBetweenTimestampsAndByChatId(syncdate - timedelta(hours=timerange),syncdate, chats[0].chatId)
        dates = [message for message in messages]

        mostusedWords = []
        chat = chats[0]
        count = 0 

        
        if int(sentiments[0].sentimentId) == 0:
            for mwords in self.messagesrepo.getMostWordsDescBetweenTimestampsAndByChatId(syncdate - timedelta(hours = timerange), syncdate ,chat.chatId):
                mostusedWords.append(MostUsedCombination(dates[count].date.strftime('%H:00'), mwords))
                count += 1
        else:            
            for mwords in self.sentimentmessages.getMostWordsDescBetweenTimestampsByChatIdAndPrediction(syncdate - timedelta(hours = timerange), syncdate ,chat.chatId, sentiments[0].sentimentId):
                mostusedWords.append(MostUsedCombination(dates[count].date.strftime('%H:00'), mwords))
                count += 1


        data = {"data": [json.dumps(mostused.to_json(), default=json_util.default) for mostused in mostusedWords]}
        return (json.dumps(data, default=json_util.default))

