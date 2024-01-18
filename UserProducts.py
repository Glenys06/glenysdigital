import shelve
class Products:
    with shelve.open("CustomFlavour", "c") as db:
        created_count_id = db["creationID"]
#    def __init__(self, creationBase1, creationBase2, creationBase3, creationMixIn1, creationMixIn2, creationMixIn3, creationMixIn4, creationMixIn5, creationTopping1, creationTopping2, creationTopping3, firstUser, users):
    def __init__(self, creationBase1, creationMixIn1, creationTopping1, firstUser, users):
        # Products.created_count_id += 1
#        dbName = str("db\\") + str(".".join([creationBase1, creationBase2, creationBase3, creationMixIn1, creationMixIn2, creationMixIn3, creationMixIn4, creationMixIn5, creationTopping1, creationTopping2, creationTopping3])) + str(".db")
        dbName = str("db\\") + str(".".join([creationBase1, creationMixIn1, creationTopping1])) + str(".db")
        self.__dbName = str(dbName)
        try:
            with shelve.open(dbName, "r") as db:
                # HELP
        except:
            with shelve.open(dbName, "c") as db:
                # Try
        self.__creationID = Products.count_id
        self.__creationBase1 = creationBase1
        # self.__creationBase2 = creationBase2
        # self.__creationBase3 = creationBase3
        self.__creationMixIn1 = creationMixIn1
        # self.__creationMixIn2 = creationMixIn2
        # self.__creationMixIn3 = creationMixIn3
        # self.__creationMixIn4 = creationMixIn4
        # self.__creationMixIn5 = creationMixIn5
        self.__creationTopping1 = creationTopping1
        # self.__creationTopping2 = creationTopping2
        # self.__creationTopping3 = creationTopping3
        self.__firstUser = firstUser
        self.__users = users.split(",")
    def get_creationID(self):
        return self.__creationID
    def get_creationBase1(self):
        return self.__creationBase1
    def get_creationBase2(self):
        return self.__creationBase2
    def get_creationBase3(self):
        return self.__creationBase3
    def get_creationMixIn1(self):
        return self.__creationMixIn1
    def get_creationMixIn2(self):
        return self.__creationMixIn2
    def get_creationMixIn3(self):
        return self.__creationMixIn3
    def get_creationMixIn4(self):
        return self.__creationMixIn4
    def get_creationMixIn5(self):
        return self.__creationMixIn5
    def get_creationTopping1(self):
        return self.__creationTopping1
    def get_creationTopping2(self):
        return self.__creationTopping2
    def get_creationTopping3(self):
        return self.__creationTopping3
    def get_firstUser(self):
        return self.__firstUser
    def get_users(self):
        return self.__users

    def set_creationID(self):
        self.__creationID = Products.count_id
    def set_creationBase1(self, creationBase1):
        self.__creationBase1 = creationBase1
    def set_creationBase2(self, creationBase2):
        self.__creationBase2 = creationBase2
    def set_creationBase3(self, creationBase3):
        self.__creationBase3 = creationBase3
    def set_creationMixIn1(self, creationMixIn1):
        self.__creationMixIn1 = creationMixIn1
    def set_creationMixIn2(self, creationMixIn2):
        self.__creationMixIn2 = creationMixIn2
    def set_creationMixIn3(self, creationMixIn3):
        self.__creationMixIn3 = creationMixIn3
    def set_creationMixIn4(self, creationMixIn4):
        self.__creationMixIn4 = creationMixIn4
    def set_creationMixIn5(self, creationMixIn5):
        self.__creationMixIn5 = creationMixIn5
    def set_creationTopping1(self, creationTopping1):
        self.__creationTopping1 = creationTopping1
    def set_creationTopping2(self, creationTopping2):
        self.__creationTopping2 = creationTopping2
    def set_creationTopping3(self, creationTopping3):
        self.__creationTopping3 = creationTopping3
    def set_firstUser(self, firstUser):
        self.__firstUser = firstUser
    def set_users(self, users):
        self.__users.append(users)