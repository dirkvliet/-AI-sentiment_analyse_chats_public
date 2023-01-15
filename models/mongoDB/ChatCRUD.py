import run

class ChatCRUD():

#    def __init__(self):
        #init\

    def getById(self, chatId):
        if not chatId: 
            raise Exception("chatname not given")
            return 

        chat = run.Chat.objects(chatId=chatId)
        if not chat:
            return None
        else:
            return chat

    def getByName(self, chatName):
        if not chatName: 
            raise Exception("chatname not given")
            return 

        chat = run.Chat.objects(name=chatName).first()
        if not chat:
            return None
        else:
            return chat

    def getAll(self):
        chats = run.Chat.objects()
        return chats
     

    def add(self, chat):
        if not chat: 
            raise Exception("no chat given")
            return 
        if not chat.chatId: 
            raise Exception("chat has no chat id")
            return 
        if not chat.name: 
            raise Exception("chat has no chat name")
            return 

        #check if chat already exsist
        if run.Chat.objects(chatId=chat.chatId).first():
            return

        chat.save()
        return chat

    def update(self, chat):
        if not chat: 
            raise Exception("no chat given")
            return 
        if not chat.chatId: 
            raise Exception("chat has no chat id")
            return 
        if not chat.name: 
            raise Exception("chat has no chat name")
            return 

        chatCheck = run.Chat.objects(chatId=chat.chatId).first()
        #chat doesn't exsist
        if not chatCheck:
            return
        else:
            chat.update(name=chat.name)
        return chat

    def delete(self, chat):
        if not chat: 
            raise Exception("no chat given")
            return 
        if not chat.chatId: 
            raise Exception("chat has no chat id")
            return 

        chat = run.Chat.objects(chatId=chat.chatId).first()
        if not chat:
            return
        else:
            chat.delete()
        return chat

