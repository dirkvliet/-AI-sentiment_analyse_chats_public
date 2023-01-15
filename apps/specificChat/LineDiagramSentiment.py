from models.mongoDB.ChatCRUD import ChatCRUD
from models.mongoDB.SentimentMessagesCRUD import SentimentMessagesCRUD
from apps.overview.SentimentData import SentimentData
from datetime import timedelta
import json 
from bson import json_util
from models.mongoDB.SyncDBCRUD import SyncDBCRUD

class LineDiagramSentiment:

    def __init__(self):
        self.sentimentMessagesrepo = SentimentMessagesCRUD()
        self.chatrepo = ChatCRUD()
        self.syncDBRepo = SyncDBCRUD()

    def getData(self, timerange, chats): 
        positiefcount = 0
        negatiefcount = 0
        neutralcount = 0

        if not chats:
            chats = self.chatrepo.getAll()
        latestDBUpdate = self.syncDBRepo.getLatest()
        syncdate = latestDBUpdate.timeStamp

        for chat in chats:
            for prediction in range(1,4):
                sentimentMessages = self.sentimentMessagesrepo.getSentimentMessagesBetweenTimestampsByChatIdAndPrediction(start = syncdate - timedelta(hours = timerange), end = syncdate, chatId=chat.chatId, prediction = prediction)
                for sentimentmessage in sentimentMessages:
                    if prediction  == 1: 
                        negatiefcount += sentimentmessage.number
                    elif prediction ==  2: 
                        neutralcount += sentimentmessage.number       
                    elif prediction == 3:
                        positiefcount += sentimentmessage.number 
        totalMessageCount = negatiefcount + neutralcount + positiefcount

        sentimentdata = SentimentData(messagesCount = totalMessageCount, positiveCount = positiefcount, neutralCount = neutralcount, negativeCount = negatiefcount, 
                                      positiveCountPrecent = (positiefcount / totalMessageCount) * 100 if positiefcount > 0 else 0.0,  negativeCountPrecent = (negatiefcount / totalMessageCount) * 100  if negatiefcount > 0 else 0.0,  neutralCountPrecent = (neutralcount / totalMessageCount) * 100  if neutralcount > 0 else 0.0)

        data = {"labels": sentimentdata.labels_to_json(),
           "data": sentimentdata.to_json()}   
        return (json.dumps(data, default=json_util.default)) 

