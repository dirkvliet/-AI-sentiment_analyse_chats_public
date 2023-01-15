# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.overview import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
import MiddleWare.SyncTelegramToDB

from run import SyncDB
from models.mongoDB.SyncDBCRUD import SyncDBCRUD
from datetime import datetime
from apps.overview.LineDiagramMessages import LineDiagramMessages
from apps.overview.TableMessagesByChat import TableMessagesByChat
from apps.overview.PieChartSentiment import PieChartSentiment
from apps.overview.BarChartNegativeSentiment import BarChartNegativeSentiment
import asyncio

from apps.overview.ChatOptions import ChatOptions

@blueprint.route('updatedatabase',  methods=['GET', 'POST'])
def updatedatabase():
        syncDBRepo = SyncDBCRUD()
        sync = MiddleWare.SyncTelegramToDB.SyncTelegramToDB()
        latestDBUpdate = syncDBRepo.getLatest()
        if(latestDBUpdate):
            if(latestDBUpdate.running):
                latestDBUpdate.actualObject = "already running"
                return latestDBUpdate.to_json()


        syncDB = SyncDB(timeStamp = datetime.now(), running = True, actualObject="running")
        syncDBRepo.add(syncDB);
        asyncio.run(sync.syncToDB())
        
        return syncDBRepo.getLatest().to_json()

@blueprint.route('getstatedatabase',  methods=['GET', 'POST'])
def getdatabasestate():
        syncDBRepo = SyncDBCRUD()
        latestDBUpdate = syncDBRepo.getLatest()
        if latestDBUpdate:
            return latestDBUpdate.to_json()
        return {}

@blueprint.route('messagebychat',  methods=['GET', 'POST'])
def getmessagebychatdata():
    tableMessagesByChat = TableMessagesByChat()
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
        return tableMessagesByChat.getData(timerange = timerange, chats = chats)
    else:
        return tableMessagesByChat.getData(timerange = 24, chats = None)



@blueprint.route('messagelinediagram',  methods=['GET', 'POST'])
def getlinediagramdata():
    lineDiagramMessage = LineDiagramMessages()
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
        return lineDiagramMessage.getData(timerange = timerange, chats = chats)
    else:
        return lineDiagramMessage.getData(timerange = 24, chats = None)

@blueprint.route('sentimentpiechart',  methods=['GET', 'POST'])
def getpiechartdata():
    pieChartSentiment = PieChartSentiment()
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
        return pieChartSentiment.getData(timerange = timerange, chats = chats)
    else:
        return pieChartSentiment.getData(timerange = 24, chats = None)


@blueprint.route('negativesentimentbarchart',  methods=['GET', 'POST'])
def getdata():
    barChartNegativeSentiment = BarChartNegativeSentiment()
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
        return barChartNegativeSentiment.getData(timerange = timerange, chats = chats)
    else:
        return barChartNegativeSentiment.getData(timerange = 24, chats = None)



@blueprint.route('index')
@login_required
def index():

    try:
        return render_template("overview/" + "index.html", segment="index", data="",  header="", title="overview", image="")

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
