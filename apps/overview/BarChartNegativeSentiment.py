from models.mongoDB.ChatCRUD import ChatCRUD
from models.mongoDB.MessageCRUD import MessageCRUD
from models.mongoDB.UserCRUD import UserCRUD
from datetime import timedelta
import json 
from bson import json_util
from models.mongoDB.SyncDBCRUD import SyncDBCRUD

class BarChartNegativeSentiment:

    def __init__(self):
        self.messagerepo = MessageCRUD()
        self.chatrepo = ChatCRUD()
        self.syncDBRepo = SyncDBCRUD()
        self.userrepo = UserCRUD()

    def getData(self, timerange, chats): 
        if not chats:
            chats = self.chatrepo.getAll()

        latestDBUpdate = self.syncDBRepo.getLatest()
        syncdate = latestDBUpdate.timeStamp
        users = self.messagerepo.getCountUsersByDateAndSentiment(syncdate - timedelta(hours = timerange), syncdate, 1)
        #chat filter can't work because user can be in more than one chat
        #filter(lambda x: filter(lambda y: y.chatId == x.chatId, chats), users)
        labels = []
        for user in range(0, (len(users) if len(users) < 5 else 5)):
            #get users username and add to list
            print(self.userrepo.getById(users[user].userId))
            labels.append(self.userrepo.getById(users[user].userId)[0].name)
        negativemessages = sum([x.num for x in users])
        data = {"labels": json.dumps(labels, default=json_util.default),
             "data": [json.dumps(user.to_json(), default=json_util.default) for user in users],
             "totalnegativemessages": negativemessages}   
        return (json.dumps(data, default=json_util.default)) 

