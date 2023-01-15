import run


class MessagesCRUD():

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
        
        messages = run.Messages.objects(date__gte=start, date__lte=end)
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
        
        messages = run.Messages.objects(date__gte=start, date__lte=end, chatId=chatId)
        return messages


    def getMostWordsDescBetweenTimestampsAndByChatId(self, start, end, chatId):
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
        messages = run.Messages.objects(date__gte=start, date__lte=end, chatId=chatId)
        for message in messages:
            mostusedwords.append(message.mostUsedCombinationOfWords)
        return mostusedwords

    
    def getMostUsedVerbsDescBetweenTimestampsAndByChatId(self, start, end, chatId):
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
        messages = run.Messages.objects(date__gte=start, date__lte=end, chatId=chatId)
        for message in messages: 
            for verb in message.mostUsedVerb: 
                mostusedverbs.append(verb)

        return sorted(mostusedverbs, key=lambda x: x[0], reverse=True)

    def getMostUsedLocationsDescBetweenTimestampsAndByChatId(self, start, end, chatId):
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
        mostusedlocations = []
        messages = run.Messages.objects(date__gte=start, date__lte=end, chatId=chatId)
        for message in messages:
            for location in message.mostUsedPlaces:
                mostusedlocations.append(location)

        return sorted(mostusedlocations, key=lambda x: x[0], reverse=True)

    def getMostUsedEntitiesDescBetweenTimestampsAndByChatId(self, start, end, chatId):
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
        mostusedentities = []
        messages = run.Messages.objects(date__gte=start, date__lte=end, chatId=chatId)
        for message in messages:
            for verb in message.mostUsedEntities:
                mostusedentities.append(verb)

        return sorted(mostusedentities, key=lambda x: x[0], reverse=True)

    def getByChatId(self,chatId):
        """
        function to get message by chatid
        parameter: chatid
        return Message objects or None
        """
        if not chatId: 
            raise Exception("chatId not given")
            return 
        
        messages = run.Messages.objects(chatId = chatId)
        return messages

    def getAll(self):
        messages = run.SentimentMessages.objects()
        return messages
     

    def add(self, message):
        if not message: 
            raise Exception("no message given")
            return 
        if message.chatId == 0: 
            raise Exception("message has no chatId")
            return 
        if not message.date: 
            raise Exception("message has no date")
            return 

        #if run.Message.objects(messageId=message.messageId).first():
        #    return

        message.save()
        return message

    def update(self, message):
        if not message: 
            raise Exception("no message given")
            return 
        if message.chatId == 0: 
            raise Exception("message has no chatId")
            return 
        if not message.date: 
            raise Exception("message has no date")
            return 

        messageCheck = run.SentimentMessages.objects(id=id).first()
        #chat doesn't exsist
        if not messageCheck:
            return
        else:
            message.update(chatId=run.SentimentMessages.chatId, date=run.SentimentMessages.date, mostUsedCombinationOfWords=run.SentimentMessages.mostUsedCombinationOfWords, number = run.SentimentMessages.number)
        return message

    def delete(self, message):
        if not message: 
            raise Exception("no message given")
            return 
        if not message.id: 
            raise Exception("message has no id")
            return 

        message = run.Messages.objects(id=message.id).first()
        if not message:
            return
        else:
            message.delete()
        return message

