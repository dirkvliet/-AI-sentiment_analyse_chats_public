from telethon.sync import TelegramClient
from datetime import datetime, timedelta
import asyncio
import pandas as pd
from telethon.tl.types import PeerUser
import run

class TelegramApi:
    #client = None

    def __init__(self):
        """
        TelegramApi is the application that requests the API GET, to Telegram
        """
        #if TelegramApi.client == None:
        api_id = "29174514"
        api_hash = "29b50f7a27be60a0f959c1ad2ba17341"
        phone_number = "+31625564723"
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        self.client  = TelegramClient('Jan Hoovense.session',
                                api_id,
                                api_hash, loop=loop, sequential_updates=True)
        self.client.connect()

        # get all chats
        # if not client.is_user_authorized():
        #     client.send_code_request(phone_number)
        #     me = client.sign_in(phone_number, input('Enter code: '))
        

    def get_dialogs(self):
        """
        Get dialogs is a function to get all the dialogs a telegram user is part of
        """
        dialogs =  self.client.get_dialogs()
        return dialogs

    def get_messages_last_24hours(self, dialog_id):
        """
        Get messages_last_24hours is a function to get all the messages from a specific dialog for the last 24 hours.
        dialog_id: the id telegram has given the dialog
        """
        onlylastday = False
        channel_entity =  self.client.get_entity(dialog_id)
        pre_first_post_id =  self.client.get_messages(channel_entity, limit=1, offset_date=(
                datetime.now() - timedelta(days=1)))
        if(len(pre_first_post_id) == 0): 
             onlylastday = True
             pre_first_post_id =  self.client.get_messages(channel_entity, limit=1, reverse=True, offset_date=(
                datetime.now() - timedelta(days=1)))

        if (len(pre_first_post_id) == 0):
            return
        
        if(len(pre_first_post_id) == 1 & onlylastday): 
            return pre_first_post_id

        pre_first_post_id = pre_first_post_id[0].id
        posts =  self.client.get_messages(channel_entity, min_id=pre_first_post_id, limit=10000, reverse=True)
        return posts

    
    def get_messages_from_offsetdate(self, offsetdate, chat_id):
        """
        Get messages_from_offsetdate is a function to get all the messages from a specific dialog from a specified time
        chat_id: the id telegram has given the chat
        offsetdate the timestamp in the past to begin with
        """
        reverse = False
        channel_entity =  self.client.get_entity(chat_id)
        pre_first_post_id =  self.client.get_messages(channel_entity, limit=1, offset_date=offsetdate)
        if(len(pre_first_post_id) == 0): 
             reverse = True
             pre_first_post_id =  self.client.get_messages(channel_entity, limit=1, reverse=True, offset_date=offsetdate)

        if (len(pre_first_post_id) == 0):
            return
        
        if(len(pre_first_post_id) == 1 & reverse): 
            return pre_first_post_id

        pre_first_post_id = pre_first_post_id[0].id
        posts =  self.client.get_messages(channel_entity, min_id=pre_first_post_id, limit=10000, reverse=True)
        return posts

    def messageResponseToDataFrame(self, messages):
        """
        Convert message response to dataframe
        parameter messages format wat you recieve from the function get message last 
        returns dataframe in format

            id   |    date                 |    Message
        ---------------------------------------------------
            0    | 22-06-22T18:06:54.0000  | tetstwtstftf wercwddcdrwsffg
        """
        dfN = pd.DataFrame(columns=['id', 'date', 'message', 'userId'])    
        for iterator in messages:
                userid = -1
                if(type(iterator.from_id) == PeerUser):
                    userid = iterator.from_id.user_id
                dfN.loc [len(dfN.id)] = [iterator.id, iterator.date.strftime('%Y-%m-%dT%H:%M:%S.%f'), iterator.text, userid] 
        return dfN

    def getUserbyId(self, userids):
        """
        get users by id's
        parameter list with userid's
        return list of User objects
        """
        users = []
        for id in userids:
            if(id > 0):
                peerUser = self.client.get_entity(id)
                users.append(run.User(userId = id,name = str(peerUser.first_name) + " " + (str(peerUser.last_name) if str(peerUser.last_name) != 'None' else '')))
            else:
                users.append(run.User(userId = id,name = "unknown"))
        return users
        
    

    async def disconnectclient(self):
        await self.client.disconnect()

    def __del__(self):
        """
        destructer of TelegramApi
        """
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.disconnectclient())
