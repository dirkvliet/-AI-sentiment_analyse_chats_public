import run


class SentimentMessagesCRUD():

    def getSentimentMessagesBetweenTimestamps(self, start, end):
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
        
        sentimentMessages = run.SentimentMessages.objects(date__gte=start, date__lte=end)
        return sentimentMessages

    def getSentimentMessagesBetweenTimestampsAndPrediction(self, start, end, prediction):
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
        if not prediction: 
            raise Exception("prediction not given")
            return 
        sentimentMessages = run.SentimentMessages.objects(date__gte=start, date__lte=end, prediction=prediction)
        return sentimentMessages

    def getSentimentMessagesBetweenTimestampsAndByChatId(self, start, end, chatId):
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
        
        sentimentMessages = run.SentimentMessages.objects(date__gte=start, date__lte=end, chatId=chatId)
        return sentimentMessages


    def getSentimentMessagesBetweenTimestampsByChatIdAndPrediction(self, start, end, chatId, prediction):
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
        if not prediction: 
            raise Exception("prediction not given")
            return 
        
        sentimentMessages = run.SentimentMessages.objects(date__gte=start, date__lte=end, chatId=chatId, sentiment=prediction)
        return sentimentMessages

        
    def getMostUsedVerbsDescBetweenTimestampsByChatIdAndPrediction(self, start, end, chatId, prediction):
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
        mostusedverbs = []
        messages = run.SentimentMessages.objects(date__gte=start, date__lte=end, chatId=chatId, sentiment = prediction)
                                                                                       
        for message in messages: 
            for verb in message.mostUsedVerb: 
                mostusedverbs.append(verb)

        return sorted(mostusedverbs, key=lambda x: x[0], reverse=True)

    def getmostUsedEntitiesDescBetweenTimestampsByChatIdAndPrediction(self, start, end, chatId, prediction):
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
        mostusedverbs = []
        messages = run.SentimentMessages.objects(date__gte=start, date__lte=end, chatId=chatId, sentiment = prediction)
                                                                                       
        for message in messages: 
            for verb in message.mostUsedEntities: 
                mostusedverbs.append(verb)

        return sorted(mostusedverbs, key=lambda x: x[0], reverse=True)

    def getMostUsedPlacesDescBetweenTimestampsByChatIdAndPrediction(self, start, end, chatId, prediction):
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
        mostusedverbs = []
        messages = run.SentimentMessages.objects(date__gte=start, date__lte=end, chatId=chatId, sentiment = prediction)
                                                                                       
        for message in messages: 
            for verb in message.mostUsedPlaces: 
                mostusedverbs.append(verb)

        return sorted(mostusedverbs, key=lambda x: x[0], reverse=True)


    def getMostWordsDescBetweenTimestampsByChatIdAndPrediction(self, start, end, chatId, prediction):
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
        mostusedwords = []
        messages = run.SentimentMessages.objects(date__gte=start, date__lte=end, chatId=chatId, sentiment = prediction)
        for message in messages:
            mostusedwords.append(message.mostUsedCombinationOfWords)
        return mostusedwords



    def getByChatId(self,chatId):
        """
        function to get message by chatid
        parameter: chatid
        return Message objects or None
        """
        if not chatId: 
            raise Exception("chatId not given")
            return 
        
        sentimentMessages = run.SentimentMessages.objects(chatId = chatId)
        return sentimentMessages

    def getAll(self):
        sentimentMessages = run.SentimentMessages.objects()
        return sentimentMessages
     

    def add(self, sentimentMessage):
        if not sentimentMessage: 
            raise Exception("no sentimentMessage given")
            return 
        if sentimentMessage.sentiment == 0: 
            raise Exception("sentimentMessage has no sentiment")
            return 
        if sentimentMessage.chatId == 0: 
            raise Exception("sentimentMessage has no chatId")
            return 
        if not sentimentMessage.date: 
            raise Exception("sentimentMessage has no date")
            return  

        sentimentmessagecheck = run.SentimentMessages.objects(date=sentimentMessage.date, sentiment = sentimentMessage.sentiment, chatId = sentimentMessage.chatId).first()
       
        if sentimentmessagecheck:
            print(sentimentmessagecheck.to_json())
            sentimentMessage._id = sentimentmessagecheck._id
            return sentimentMessage.save(update=True)

        sentimentMessage.save()
        return sentimentMessage

    def update(self, sentimentMessage):
        if not sentimentMessage: 
            raise Exception("no sentimentMessage given")
            return 
        if sentimentMessage.sentiment == 0: 
            raise Exception("sentimentMessage has no sentiment")
            return 
        if sentimentMessage.chatId == 0: 
            raise Exception("sentimentMessage has no chatId")
            return 
        if not sentimentMessage.date: 
            raise Exception("sentimentMessage has no date")
            return 
        sentimentMessageCheck = run.SentimentMessages.objects(_id=sentimentMessage._id).first()
        #chat doesn't exsist
        if not sentimentMessageCheck:
            return
        else:
            sentimentMessageCheck.update(set__sentiment=sentimentMessage.sentiment, set__chatId=sentimentMessage.chatId, set__date=sentimentMessage.date,
                                   set__mostUsedVerb=sentimentMessage.mostUsedVerb, set__mostUsedCombinationOfWords=sentimentMessage.mostUsedCombinationOfWords,
                                   set__mostUsedPlaces=sentimentMessage.mostUsedPlaces, set__mostUsedEntities=sentimentMessage.mostUsedEntities,
                                   set__number = sentimentMessage.number)
        return sentimentMessage

    def delete(self, sentimentMessage):
        if not sentimentMessage: 
            raise Exception("no sentimentMessage given")
            return 
        if not sentimentMessage.id: 
            raise Exception("sentimentMessage has no id")
            return 

        sentimentMessage = run.SentimentMessages.objects(id=sentimentMessage.id).first()
        if not sentimentMessage:
            return
        else:
            sentimentMessage.delete()
        return sentimentMessage

