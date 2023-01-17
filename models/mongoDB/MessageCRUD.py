import run
from models.SentimentUser import SentimentUser


class MessageCRUD():

#    def __init__(self):
        #init\

    def getById(self, messageId):
        """
        function to get message by his id return None when it not found
        parameter: messageId 
        return Message object or None
        """
        if not messageId: 
            raise Exception("messageId not given")
            return 

        message = run.Message.objects(messageId=messageId).first()
        if not message:
            return None
        else:
            return message

    def getMessagesBetweenTimestamps(self, start, end):
        """
        function to get message between timestamps
        parameter: start-date and end-date as datetime object
        return Message objects or None
        """
        if not start: 
            raise Exception("start not given")
            return 
        if not end: 
            raise Exception("end not given")
            return 
        
        messages = run.Message.objects(date__gte=start, date__lte=end)
        return messages

    def getMessagesBetweenTimestampsAndByChatId(self, start, end, chatId):
        """
        function to get message between timestamps and chatId
        parameter: chatid, start-date and end-date as datetime object
        return Message objects or None
        """
        if not start: 
            raise Exception("start not given")
            return 
        if not end: 
            raise Exception("end not given")
            return 
        if not chatId: 
            raise Exception("chatId not given")
            return 
        
        messages = run.Message.objects(date__gte=start, date__lte=end, chatId=chatId)
        return messages

    def getByChatId(self,chatId):
        """
        function to get message by chatid
        parameter: chatid
        return Message objects or None
        """
        if not chatId: 
            raise Exception("chatId not given")
            return 
        
        messages = run.Message.objects(chatId = chatId)
        return messages

    def getMessagesBetweenTimestampsAndByPrediction(self, start, end, prediction):
        """
        function to get message between timestamp and by prediction
        parameter: prediction, start-date and end-date as datetime object
        return Message objects or None
        """
        if not start: 
            raise Exception("start not given")
            return 
        if not end: 
            raise Exception("end not given")
            return 
        if not prediction: 
            raise Exception("prediction not given")
            return 
        
        messages = run.Message.objects(date__gte=start, date__lte=end, prediction=prediction)
        return messages

    def getCountUsersByDateAndSentiment(self, start, end, sentiment):
        """

        """
        if not start: 
            raise Exception("start not given")
            return 
        if not end: 
            raise Exception("end not given")
            return 
        if sentiment == 0 : 
            raise Exception("sentiment not given")
            return 
        
        userlist = []
        userIds = [x.userId for x in list(run.Message.objects(prediction = sentiment))]
        userIds = list(set(userIds))
        for userId in userIds:  
            num = run.Message.objects(prediction = sentiment, userId = userId).count()
            sentimentUser =  SentimentUser(num = num, userId = userId, sentiment = sentiment, userName = "")
            userlist.append(sentimentUser)
        return sorted(userlist, key=lambda x: x.num, reverse=True)

    def getAllChatUsers(self):
        """
        get all userids wich posted message's
        return a list of userids
        """
        userIds = [x.userId for x in list(run.Message.objects())]
        userIds = list(set(userIds))
        return userIds


    def getMessagesBetweenTimestampsByPredictionAndByChatId(self, start, end, prediction, chatId):
        """
        function to get message between timestamp by prediction and chatId
        parameter: chatid, prediction, start-date and end-date as datetime object
        return Message objects or None
        """
        if not start: 
            raise Exception("start not given")
            return 
        if not end: 
            raise Exception("end not given")
            return 
        if not prediction: 
            raise Exception("prediction not given")
            return
        if not chatId: 
            raise Exception("chatId not given")
            return 
        
        messages = run.Message.objects(date__gte=start, date__lte=end, prediction=prediction, chatId=chatId)
        return messages

    def getByPrediction(self, prediction):
        """
        function to get message by prediction
        parameter: prediction
        return Message objects or None
        """
        if not prediction: 
            raise Exception("prediction not given")
            return 
        messages = run.Message.objects(prediction = prediction)
        return messages


    def getAll(self):
        messages = run.Message.objects()
        return messages
     

    def add(self, message):
        if not message: 
            raise Exception("no message given")
            return 
        if message.messageId == 0: 
            raise Exception("message has no messageId")
            return 
        if message.chatId == 0: 
            raise Exception("message has no chatId")
            return 
        if message.message == "": 
            raise Exception("message has no message")
            return 
        if not message.date: 
            raise Exception("message has no date")
            return 
        if message.prediction == 0: 
            raise Exception("message has no prediction")
            return 
        if message.userId == 0: 
            raise Exception("message has no userId")
            return 


        messagecheck = run.Message.objects(messageId=message.messageId).first()
        if messagecheck:
            return
           # message._id = messagecheck._id
          #  return self.update(message)

        message.save()
        return message

    def update(self, message):
        if not message: 
            raise Exception("no message given")
            return 
        if message.messageId == 0: 
            raise Exception("message has no messageId")
            return 
        if message.chatId == 0: 
            raise Exception("message has no chatId")
            return 
        if message.message == "": 
            raise Exception("message has no message")
            return 
        if not message.date: 
            raise Exception("message has no date")
            return 
        if message.prediction == 0: 
            raise Exception("message has no prediction")
            return 
        if message.userId == 0: 
            raise Exception("message has no userId")
            return 

        messageCheck = run.Message.objects(messageId=message.messageId).first()
        #chat doesn't exsist
        if not messageCheck:
            return
        else:
            print(message.to_json())
            message.update(set__message=message.message,  set__chatId=message.chatId, set__date=message.date, set__prediction=message.prediction, set__userId=message.userId)
        return message

    def delete(self, message):
        if not message: 
            raise Exception("no message given")
            return 
        if not message.messageId: 
            raise Exception("message has no messageId")
            return 

        message = run.Message.objects(messageId=message.messageId).first()
        if not message:
            return
        else:
            message.delete()
        return message

