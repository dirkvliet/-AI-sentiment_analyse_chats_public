import pandas as pd
import json


class ReadExportFileTelegram:
    def __init__(self):
        """
        ReadExportFileTelegram is class to read export chat file from telegram
        """
    
    def convertFileToDataFrame(self, path):
        """
        read a export file from a telegram chat to a dataframe in format [id, date, Message]
        parameter path this location of the file relative to the root of the project where startup (run.py) is located
        returns dataframe in format [id, date, Message]
        """
        with open(path, 'r',  encoding='utf-8') as f:
            data = json.load(f)

        dfN = pd.DataFrame(columns=['id', 'date', 'message'])
        
        for iterator in data['messages']:
            text = ""
            if(iterator["type"] == "message"):
                for iteratorInnerMessage in iterator['text_entities']:
                     if(iteratorInnerMessage["type"] == "plain"):
                            text += str(iteratorInnerMessage["text"])
                            text += str(" ")
            if(text != ""):
                dfN.loc [len(dfN.id)] = [iterator["id"], iterator['date'], text] 
        return dfN