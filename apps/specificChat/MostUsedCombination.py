import json 
from bson import json_util

class MostUsedCombination():
    date = ""
    mostUsedCombination = []

    def __init__(self, date, mostUsedCombination):
        self.date = date
        self.mostUsedCombination = mostUsedCombination
    
    def to_json(self):
        return {
            "date": self.date,
            "mostUsedCombination": [json.dumps(mostused, default=json_util.default) for mostused in self.mostUsedCombination]
            }
