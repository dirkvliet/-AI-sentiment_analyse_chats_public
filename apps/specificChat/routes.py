# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.specificChat import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
import MiddleWare.SyncTelegramToDB

import run
from apps.specificChat.MostUsedCombinationOfWords import MostUsedCombinationOfWords
from apps.specificChat.MostUsedEntities import MostUsedEntities
from apps.specificChat.MostUsedLocations import MostUsedLocations
from models.mongoDB.SyncDBCRUD import SyncDBCRUD
from datetime import datetime
from apps.specificChat.LineDiagramSentimentMessages import LineDiagramSentimentMessages
from apps.overview.PieChartSentiment import PieChartSentiment
from apps.specificChat.MostUsedVerbs import MostUsedVerbs
from apps.specificChat.Chats import Chats
import asyncio

from apps.specificChat.ChatOptions import ChatOptions
from apps.specificChat.SentimentOptions import SentimentOptions

@blueprint.route('updatedatabase1',  methods=['GET', 'POST'])
def updatedatabase1():
        syncDBRepo = SyncDBCRUD()
        sync = MiddleWare.SyncTelegramToDB.SyncTelegramToDB()
        latestDBUpdate = syncDBRepo.getLatest()
        if(latestDBUpdate):
            if(latestDBUpdate.running):
                latestDBUpdate.actualObject = "already running"
                return latestDBUpdate.to_json()


        syncDB = run.SyncDB(timeStamp = datetime.now(), running = True, actualObject="running")
        syncDBRepo.add(syncDB);
        asyncio.run(sync.syncToDB())
        
        return syncDBRepo.getLatest().to_json()

@blueprint.route('getstatedatabase1',  methods=['GET', 'POST'])
def getdatabasestate1():
        syncDBRepo = run.SyncDBCRUD()
        latestDBUpdate = syncDBRepo.getLatest()
        if latestDBUpdate:
            return latestDBUpdate.to_json()
        return {}

@blueprint.route('mostUsedWords',  methods=['GET', 'POST'])
def getMostUsedWords():
    tableMostUsedWords = MostUsedCombinationOfWords()
    if request.method == 'POST':
        data = request.json
        chats = []
        sentiments = []

        timerange =  data['timerange'] if data['timerange'] is not None else 24

        for item in data['chatFilter']:
            chat = ChatOptions(chatId = item['chatId'], name = item['chatName'], option = item['option'])
            chats.append(chat)

        if len(chats) > 0:
            chats = list(filter(lambda x: (x.option == True), chats))
        chats =  chats if len(chats) > 0  else None

        for item in data['sentimentFilter']:
          sentiment = SentimentOptions(sentimentId = item['sentimentId'], sentiment = item['sentiment'], option = item['option'])
          sentiments.append(sentiment)

        if len(sentiments) > 0:
          sentiments = list(filter(lambda x: (x.option == True), sentiments))
          sentiments =  sentiments if len(sentiments) > 0  else None
        return tableMostUsedWords.getData(timerange = timerange, chats = chats, sentiments = sentiments)
    else:
        return tableMostUsedWords.getData(timerange = 24, chats = None, sentiments = None)


@blueprint.route('chats',  methods=['GET', 'POST'])
def chats():
    chats = Chats()
    if request.method == 'POST':
        data = request.json
        chats = []

        timerange =  data['timerange'] if data['timerange'] is not None else 24

        for item in data['chatFilter']:
            chat = ChatOptions(chatId = item['chatId'], name = item['chatName'], option = item['option'])
            chats.append(chat)

        if len(chats) > 0:
            chats = list(filter(lambda x: (x.option == True), chats))
        chats =  chats if len(chats) > 0  else None
        return chats.getData(timerange = timerange, chats = chats)
    else:
        return chats.getData(timerange = 24, chats = None)


@blueprint.route('sentimentmessageslinediagram',  methods=['GET', 'POST'])
def getsentimentlinediagramdata():
    lineDiagramSentimentMessages = LineDiagramSentimentMessages()
    if request.method == 'POST':
        data = request.json
        chats = []

        timerange =  data['timerange'] if data['timerange'] is not None else 24

        for item in data['chatFilter']:
            chat = ChatOptions(chatId = item['chatId'], name = item['chatName'], option = item['option'])
            chats.append(chat)

        if len(chats) > 0:
            chats = list(filter(lambda x: (x.option == True), chats))
        chats =  chats if len(chats) > 0  else None
        return lineDiagramSentimentMessages.getData(timerange = timerange, chats = chats)
    else:
        return lineDiagramSentimentMessages.getData(timerange = 24, chats = None)


@blueprint.route('MostUsedEntities',  methods=['GET', 'POST'])
def getmostusedentities():
    mostUsedEntities = MostUsedEntities()
    if request.method == 'POST':
        data = request.json
        chats = []
        sentiments = []
        timerange =  data['timerange'] if data['timerange'] is not None else 24

        for item in data['chatFilter']:
          chat = ChatOptions(chatId = item['chatId'], name = item['chatName'], option = item['option'])
          chats.append(chat)

        if len(chats) > 0:
          chats = list(filter(lambda x: (x.option == True), chats))
          chats =  chats if len(chats) > 0  else None

        for item in data['sentimentFilter']:
          sentiment = SentimentOptions(sentimentId = item['sentimentId'], sentiment = item['sentiment'], option = item['option'])
          sentiments.append(sentiment)

        if len(sentiments) > 0:
          sentiments = list(filter(lambda x: (x.option == True), sentiments))
          sentiments =  sentiments if len(sentiments) > 0  else None

        return mostUsedEntities.getData(timerange = timerange, chats = chats, sentiments = sentiments)
    else:
        return mostUsedEntities.getData(timerange = 24, chats = None, sentiments = None)

@blueprint.route('MostUsedVerbs',  methods=['GET', 'POST'])
def getmostusedverbsdata():
    mostUsedVerbs = MostUsedVerbs()
    if request.method == 'POST':
        data = request.json
        chats = []
        sentiments = []
        timerange =  data['timerange'] if data['timerange'] is not None else 24

        for item in data['chatFilter']:
          chat = ChatOptions(chatId = item['chatId'], name = item['chatName'], option = item['option'])
          chats.append(chat)

        if len(chats) > 0:
          chats = list(filter(lambda x: (x.option == True), chats))
          chats =  chats if len(chats) > 0  else None

        for item in data['sentimentFilter']:
          sentiment = SentimentOptions(sentimentId = item['sentimentId'], sentiment = item['sentiment'], option = item['option'])
          sentiments.append(sentiment)

        if len(sentiments) > 0:
          sentiments = list(filter(lambda x: (x.option == True), sentiments))
          sentiments =  sentiments if len(sentiments) > 0  else None
        return mostUsedVerbs.getData(timerange = timerange, chats = chats, sentiments = sentiments)
    else:
        return mostUsedVerbs.getData(timerange = 24, chats = None, sentiments = None)


@blueprint.route('MostUsedLocations',  methods=['GET', 'POST'])
def getmostusedlocationsdata():
    mostUsedLocations = MostUsedLocations()
    if request.method == 'POST':
        data = request.json
        chats = []
        sentiments = []

        timerange =  data['timerange'] if data['timerange'] is not None else 24
        for item in data['chatFilter']:
          chat = ChatOptions(chatId = item['chatId'], name = item['chatName'], option = item['option'])
          chats.append(chat)

        if len(chats) > 0:
          chats = list(filter(lambda x: (x.option == True), chats))
          chats = chats if len(chats) > 0  else None

        for item in data['sentimentFilter']:
          sentiment = SentimentOptions(sentimentId = item['sentimentId'], sentiment = item['sentiment'], option = item['option'])
          sentiments.append(sentiment)

        if len(sentiments) > 0:
          sentiments = list(filter(lambda x: (x.option == True), sentiments))
          sentiments =  sentiments if len(sentiments) > 0  else None
        return mostUsedLocations.getData(timerange = timerange, chats = chats, sentiments = sentiments)
    else:
        return mostUsedLocations.getData(timerange = 24, chats = None, sentiments = None)


@blueprint.route('specificChat')
@login_required
def specificChat():

    try:
        return render_template("specificChat/" + "index.html", segment="specificChat", data="",  header="", title="specificChat", image="")

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except Exception as e:
        print(e)
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
