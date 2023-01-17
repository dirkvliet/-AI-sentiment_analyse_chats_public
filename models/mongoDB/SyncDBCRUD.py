import run
from datetime import datetime, timedelta

class SyncDBCRUD():
    def getLatest(self):
        syncDB = run.SyncDB.objects().first()
        if not syncDB:
            return run.SyncDB(timeStamp = datetime.now(), running = False, actualObject = "first time")
        else:
            return syncDB

    def getAll(self):
        syncDBs = run.SyncDB.objects()
        return syncDBs
     

    def add(self, syncDB):
        if not syncDB: 
            raise Exception("no syncDB given")
            return 
        if not syncDB.timeStamp: 
            raise Exception("syncDB has no chat timestamp")
            return 
        if not syncDB.running: 
            raise Exception("syncDB has no running")
            return 
        if not syncDB.actualObject: 
            raise Exception("syncDB has no actualObject")
            return 


        #check if chat already exsist
        if run.SyncDB.objects(timeStamp=syncDB.timeStamp).first():
            #self.update(chat)
            return

        syncDB.save()
        return syncDB

    def update(self, syncDB):
        if not syncDB: 
            raise Exception("no syncDB given")
            return 
        if not syncDB.timeStamp: 
            raise Exception("syncDB has no chat timestamp")
            return 
        if not syncDB.actualObject: 
            raise Exception("syncDB has no actualObject")
            return 

        syncDBCheck = run.SyncDB.objects(id=syncDB.id).first()
        #chat doesn't exsist
        if not syncDBCheck:
            return
        else:
            syncDB.update(running=syncDB.running, actualObject=syncDB.actualObject)
        return syncDB

    def delete(self, syncDB):
        if not syncDB: 
            raise Exception("no syncDB given")
            return 
        if not syncDB.id: 
            raise Exception("syncDB has no id")
            return 

        syncDB = run.SyncDB.objects(id=syncDB.id).first()
        if not syncDB:
            return
        else:
            syncDB.delete()
        return syncDB

