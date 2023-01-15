# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
from   flask_migrate import Migrate
from   flask_minify  import Minify
from   sys import exit
import json

from apps.config import config_dict
from apps import create_app, db
from flask_mongoengine import MongoEngine
from ML_DataCleaning.Predictors import predictors
from ML_DataCleaning.my_tokenizer import my_tokenizer


# WARNING: Don't run with debug turned on in production!
DEBUG = (os.getenv('DEBUG', 'False') == 'True')

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'

try:

    # Load the configuration using the default values
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

app = create_app(app_config)
app.config['MONGODB_SETTINGS'] = {
    'db': 'myFirstDatabase',
    'host': 'mongodb+srv://ReservationAppRoot:VOfCmj2gTVkNw3HT@reservationapp.fugsp.mongodb.net/?retryWrites=true&w=majority',
    'port': 27017
}

mongodb = MongoEngine()
mongodb.init_app(app)
Migrate(app, db)

class Chat(mongodb.Document):
    chatId = mongodb.IntField()
    name = mongodb.StringField()

    def to_json(self):
        return {"chatId": self.chatId,
                "name": self.name}

class Message(mongodb.Document):
    messageId = mongodb.IntField()
    date = mongodb.DateTimeField()
    message = mongodb.StringField()
    chatId = mongodb.IntField()
    prediction = mongodb.IntField()
    userId = mongodb.IntField()

    def to_json(self):
        return {"messageId": self.messageId,
                "message": self.message,
                "date": self.date,
                "chatId": self.chatId,
                "prediction": self.prediction, 
                "userId": self.userId
                }

class SyncDB(mongodb.Document):
    timeStamp = mongodb.DateTimeField()
    running = mongodb.BooleanField()
    actualObject = mongodb.StringField()

    def to_json(self):
        return {"timeStamp": self.timeStamp,
                "running": self.running,
                "actualObject": self.actualObject,
                }

class SentimentMessages(mongodb.Document):
    sentiment = mongodb.IntField()
    number  = mongodb.IntField()
    chatId = mongodb.IntField()
    date = mongodb.DateTimeField()
    mostUsedCombinationOfWords = mongodb.ListField()
    mostUsedVerb = mongodb.ListField()
    mostUsedPlaces = mongodb.ListField()
    mostUsedEntities = mongodb.ListField()

    def to_json(self):
        return {
                "sentiment": self.sentiment,
                "number": self.number,
                "chatId": self.chatId,
                "date": self.date.strftime('%Y-%m-%dT%H:00:00.000Z'),
                "mostUsedCombinationOfWords": self.mostUsedCombinationOfWords,
                "mostUsedVerb": self.mostUsedVerb,
                "mostUsedPlaces": self.mostUsedPlaces, 
                "mostUsedEntities": self.mostUsedEntities
                }
    
    def date_to_json(self):
        return {
                "date": self.date.strftime('%H:00'),                           
                }


class User(mongodb.Document):
    userId = mongodb.IntField()
    name  = mongodb.StringField()

    def to_json(self):
        return {
                "userId": self.userId,
                "name": self.name
                }



class Messages(mongodb.Document):
    number  = mongodb.IntField()
    chatId = mongodb.IntField()
    date = mongodb.DateTimeField()
    mostUsedCombinationOfWords = mongodb.ListField()
    mostUsedVerb = mongodb.ListField()
    mostUsedPlaces = mongodb.ListField()
    mostUsedEntities = mongodb.ListField()

    def to_json(self):
        return {
                "number": self.number,
                "chatId": self.chatId,
                "date": self.date.strftime('%Y-%m-%dT%H:00:00.000Z'),
                "mostUsedCombinationOfWords": self.mostUsedCombinationOfWords,
                "mostUsedVerb": self.mostUsedVerb,
                "mostUsedPlaces": self.mostUsedPlaces, 
                "mostUsedEntities": self.mostUsedEntities                           
                }
   
    def date_to_json(self):
        return {
                "date": self.date.strftime('%H:00'),                           
                }

if not DEBUG:
    Minify(app=app, html=True, js=False, cssless=False)
    
if DEBUG:
    app.logger.info('DEBUG       = ' + str(DEBUG)             )
    app.logger.info('DBMS        = ' + app_config.SQLALCHEMY_DATABASE_URI)
    app.logger.info('ASSETS_ROOT = ' + app_config.ASSETS_ROOT )

if __name__ == "__main__":
    app.run()
