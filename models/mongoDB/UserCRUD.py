import run

class UserCRUD():

    def getById(self, userId):
        if not userId: 
            raise Exception("userId not given")
            return 

        user = run.User.objects(userId=userId)
        if not user:
            return None
        else:
            return user

    def getByName(self, userName):
        if not userName: 
            raise Exception("username not given")
            return 

        user = run.User.objects(name=userName).first()
        if not user:
            return None
        else:
            return user

    def getAll(self):
        users = run.User.objects()
        return users
     

    def add(self, user):
        if not user: 
            raise Exception("no user given")
            return 
        if not user.userId: 
            raise Exception("user has no user id")
            return 
        if not user.name: 
            raise Exception("user has no user name")
            return 

        #check if user already exsist
        if run.User.objects(userId=user.userId).first():
            return

        user.save()
        return user

    def update(self, user):
        if not user: 
            raise Exception("no user given")
            return 
        if not user.userId: 
            raise Exception("user has no user id")
            return 
        if not user.name: 
            raise Exception("user has no user name")
            return 

        userCheck = run.User.objects(userId=user.userId).first()
        #user doesn't exsist
        if not userCheck:
            return
        else:
            user.update(name=user.name)
        return user

    def delete(self, user):
        if not user: 
            raise Exception("no user given")
            return 
        if not user.userId: 
            raise Exception("user has no user id")
            return 

        user = run.User.objects(userId=user.userId).first()
        if not user:
            return
        else:
            user.delete()
        return user

