import json 
from bson import json_util

class SentimentData():
    def __init__(self, messagesCount, positiveCount, neutralCount, negativeCount, positiveCountPrecent, negativeCountPrecent, neutralCountPrecent):
        self.messagesCount = messagesCount
        self.positiveCount = positiveCount
        self.neutralCount = neutralCount
        self.negativeCount = negativeCount
        self.positiveCountPercent = positiveCountPrecent
        self.negativeCountPercent = negativeCountPrecent
        self.neutralCountPercent = neutralCountPrecent

    def to_json(self):
        return{
            'messagesCount': self.messagesCount, 
            'positiveCount': self.positiveCount, 
            'neutralCount': self.neutralCount, 
            'negativeCount': self.negativeCount, 
            'positiveCountPercent': self.positiveCountPercent,
            'negativeCountPercent': self.negativeCountPercent, 
            'neutralCountPercent': self.neutralCountPercent
            }
    
    def labels_to_json(self):
        return{
            'positiveLabel': '%1.1f %% positive' % self.positiveCountPercent,
            'neutralLabel': '%1.1f  %% neutral' % self.neutralCountPercent,
            'negativeLabel': '%1.1f %% negative' % self.negativeCountPercent
            }