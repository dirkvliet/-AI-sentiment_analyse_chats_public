import json 
from bson import json_util

class SentimentUser():
    def __init__(self, userId, num, sentiment, userName):
        self.userId = userId
        self.num = num
        self.sentiment = sentiment
        self.userName = userName

    def to_json(self):
        return{
            'userId': self.userId, 
            'num': self.num, 
            'sentiment': self.sentiment,     
            'userName': self.userName
            }