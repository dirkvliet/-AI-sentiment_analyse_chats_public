class ChatOptions():
    def __init__(self, chatId, name, option):
        self.chatId = chatId
        self.name = name
        self.option = option

    def to_json(self):
        return{
            'chatId': self.chatId, 
            'name': self.name, 
            'option': self.option            
            }