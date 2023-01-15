from run import Chat, Message, SentimentMessages, Messages
from models.mongoDB.ChatCRUD import ChatCRUD
from models.mongoDB.MessageCRUD import MessageCRUD
from models.mongoDB.SentimentMessagesCRUD import SentimentMessagesCRUD
from models.mongoDB.MessagesCRUD import MessagesCRUD
from models.mongoDB.UserCRUD import UserCRUD
from FileImport.ChatExportTelegram.TeleGramApi import TelegramApi
from ML_DataCleaning.DataCleaner import DataCleaner
from ML_DataCleaning.SentimentModel import SentimentModel
from ML_DataCleaning.NERModel import NerModel
from datetime import datetime, timedelta
from ML_DataCleaning.N_GramGenerator import N_GramGenerator 
import pandas as pd
from models.mongoDB.SyncDBCRUD import SyncDBCRUD

class SyncTelegramToDB:

    def __init__(self):
        self.api = TelegramApi()
        self.chatrepo = ChatCRUD()
        self.messagerepo = MessageCRUD()
        self.userrepo = UserCRUD()
        self.sentimentmessagerepo = SentimentMessagesCRUD()
        self.messagesrepo = MessagesCRUD()
        self.datacleaner = DataCleaner()
        self.model = SentimentModel()
        self.nerModel = NerModel()
        
        self.model.loadExsistingModel('./models/sentiment_analyse.pkl')

    def updateChats(self):
        """
        update chats this methods reads all chats where user is member of and sync it to mongoDB
        """
        chats = self.api.get_dialogs()
        print(chats)
        for count in range(0,len(chats)):
            if(chats[count].name != ''):
                chat = Chat(chatId=chats[count].id,  name=chats[count].name)
                print(chat.to_json())
                self.chatrepo.add(chat)
    
    def updateMessageFromOffsetDate(self, offsetDate, chatId):
        messages = self.api.get_messages_from_offsetdate(offsetDate, chatId)
        dataframe = self.api.messageResponseToDataFrame(messages)
        table = self.datacleaner.dropmissingMessages(self.datacleaner.cleanDataFrame(dataframe))
 
        if not table.empty:
            if table['date'].count() > 0:
                table = self.model.predictDataFrame(table)
   
        for index, record in table.iterrows(): 
            message = Message(messageId=record['id'], message = record['message'], date=record['date'], 
                                chatId = chatId, prediction = record['prediction'], userId = record['userId'])
            self.messagerepo.add(message)

    def updateSentimentMessagesFromOffsetDate(self, offsetDate, chatId):       
        lowestDate = offsetDate.replace(minute=0, second=0)
        higestDate = datetime.now().replace(minute=59, second=59)
        time_range =  pd.date_range(lowestDate, higestDate, freq='H')
        nGramGenerator =  N_GramGenerator()

        for prediction in range(1,4):
            for timestamp in time_range:
                messages = self.messagerepo.getMessagesBetweenTimestampsByPredictionAndByChatId(timestamp.replace(minute=0, second=0, microsecond = 0), timestamp.replace(minute=59, second=59, microsecond = 999), prediction, chatId)
                dfN = pd.DataFrame(columns=['messageId', 'message'])
                for count in range(0,len(messages)):
                     dfN.loc[len(dfN.messageId)] = [messages[count].messageId, messages[count].message]
                mostcommoncombinations = nGramGenerator.getCountOfNgramCombinationsDescOrder(dfN, 3)
                mostusedcombinationofwords = list()
                count = 0 
                if len(mostcommoncombinations) > 0: 
                    for commoncombination in mostcommoncombinations[0]:
                        mostusedcombinationofwords.append(commoncombination)
                        count += 1
                        if(count >= 5):
                            break

                #add entities location verbs
                locations = self.nerModel.getlocations(dfN)
                locations = self.datacleaner.getOrderedDescCombinations(locations)
                lenoflocationlist = len(locations) if len(locations) < 5 else 5
                mostusedlocations = list()
                if lenoflocationlist > 0:
                    mostusedlocations = locations[0: lenoflocationlist]


                entities = self.nerModel.getentities(dfN)
                entities = self.datacleaner.getOrderedDescCombinations(entities)
                lenofentitylist = len(entities) if len(entities) < 5 else 5
                mostusedentities = list()
                if lenofentitylist > 0:
                    mostusedentities = entities[0: lenofentitylist]


                verbs = self.nerModel.getverbs(dfN)
                verbs = self.datacleaner.getOrderedDescCombinations(verbs)
                lenofverblist = len(verbs) if len(verbs) < 5 else 5
                mostusedverbs = list()
                if lenofverblist > 0:
                    mostusedverbs = verbs[0: lenofverblist]
                    
                sentimentMessage = SentimentMessages(sentiment = prediction, number = len(messages), chatId = chatId, date = timestamp, mostUsedCombinationOfWords = mostusedcombinationofwords, mostUsedVerb = mostusedverbs, mostUsedPlaces = mostusedlocations, mostUsedEntities = mostusedentities)
                self.sentimentmessagerepo.add(sentimentMessage)

    def updateMessagesFromOffsetDate(self, offsetDate, chatId):       
        lowestDate = offsetDate.replace(minute=0, second=0)
        higestDate = datetime.now().replace(minute=59, second=59)
        time_range =  pd.date_range(lowestDate, higestDate, freq='H')
        nGramGenerator =  N_GramGenerator()

        for timestamp in time_range:
            print(timestamp)
            messages = self.messagerepo.getMessagesBetweenTimestampsAndByChatId(timestamp.replace(minute=0, second=0, microsecond = 0), timestamp.replace(minute=59, second=59, microsecond = 999), chatId)
            dfN = pd.DataFrame(columns=['messageId', 'message'])
            for count in range(0,len(messages)):
                    dfN.loc[len(dfN.messageId)] = [messages[count].messageId, messages[count].message]  
            mostcommoncombinations = nGramGenerator.getCountOfNgramCombinationsDescOrder(dfN, 3)
            mostusedcombinationofwords = list()
            count = 0 
            if len(mostcommoncombinations) > 0: 
                for commoncombination in mostcommoncombinations[0]:
                    mostusedcombinationofwords.append(commoncombination)
                    count += 1
                    if(count >= 5):
                        break
            #add entities location verbs
            locations = self.nerModel.getlocations(dfN)
            locations = self.datacleaner.getOrderedDescCombinations(locations)
            lenoflocationlist = len(locations) if len(locations) < 5 else 5
            mostusedlocations = list()
            if lenoflocationlist > 0:
                mostusedlocations = locations[0: lenoflocationlist]


            entities = self.nerModel.getentities(dfN)
            entities = self.datacleaner.getOrderedDescCombinations(entities)
            lenofentitylist = len(entities) if len(entities) < 5 else 5
            mostusedentities = list()
            if lenofentitylist > 0:
                mostusedentities = entities[0: lenofentitylist]


            verbs = self.nerModel.getverbs(dfN)
            verbs = self.datacleaner.getOrderedDescCombinations(verbs)
            lenofverblist = len(verbs) if len(verbs) < 5 else 5
            mostusedverbs = list()
            if lenofverblist > 0:
                mostusedverbs = verbs[0: lenofverblist]
                    
            message = Messages(number = len(messages), chatId = chatId, date = timestamp, mostUsedCombinationOfWords = mostusedcombinationofwords, mostUsedVerb = mostusedverbs, mostUsedPlaces = mostusedlocations, mostUsedEntities = mostusedentities)
            self.messagesrepo.add(message)
    

    def updateUsers(self):
        users = self.api.getUserbyId(self.messagerepo.getAllChatUsers())
        for user in users:
            self.userrepo.add(user)

    def syncToDB(self):
        syncDBRepo = SyncDBCRUD()
        latestDBUpdate = syncDBRepo.getLatest()
        latestDBUpdate.actualObject = "update chats"
        syncDBRepo.update(latestDBUpdate);
        self.updateChats()
        chats = self.chatrepo.getAll()
        syncdate = datetime.now()
        for count in range(0,len(chats)):
            latestDBUpdate = syncDBRepo.getLatest()
            latestDBUpdate.actualObject = "update message from chat " + chats[count].name
            print( latestDBUpdate.actualObject)
            syncDBRepo.update(latestDBUpdate);
            self.updateMessageFromOffsetDate(syncdate - timedelta(days = 1), chatId=chats[count].chatId)
            latestDBUpdate = syncDBRepo.getLatest()
            latestDBUpdate.actualObject = "generate sentiment data from chat " + chats[count].name
            syncDBRepo.update(latestDBUpdate);
            self.updateSentimentMessagesFromOffsetDate(syncdate- timedelta(days = 1), chatId=chats[count].chatId)
            latestDBUpdate = syncDBRepo.getLatest()
            latestDBUpdate.actualObject = "generate messages data from chat " + chats[count].name
            syncDBRepo.update(latestDBUpdate);
            self.updateMessagesFromOffsetDate(syncdate - timedelta(days = 1), chatId=chats[count].chatId)
            latestDBUpdate = syncDBRepo.getLatest()
            latestDBUpdate.actualObject = "chat " +  chats[count].name + " completed"
            syncDBRepo.update(latestDBUpdate);
        latestDBUpdate = syncDBRepo.getLatest()
        latestDBUpdate.actualObject = "update users"
        syncDBRepo.update(latestDBUpdate);
        self.updateUsers()
        latestDBUpdate = syncDBRepo.getLatest()
        latestDBUpdate.running = False
        latestDBUpdate.actualObject = "database synchronisatie completed"
        syncDBRepo.update(latestDBUpdate);

   