class SentimentOptions():
    def __init__(self, sentimentId, sentiment, option):
        self.sentimentId = sentimentId
        self.sentiment = sentiment
        self.option = option

    def to_json(self):
        return{
            'sentimentId': self.sentimentId, 
            'sentiment': self.sentiment, 
            'option': self.option            
            }