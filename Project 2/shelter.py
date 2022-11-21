#Example Python Code to Insert a Document
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,user,password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:35825'%(user,password))
        self.database = self.client['AAC']

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary
            print("++++++++++++++++++ animal created successifully+++++++++++++++")
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
    # THIS IS A READ METHOD
    def read(self, data):
        if data is not None:
            data = self.database.animals.find(data,{"_id":False})  # data should be dictionary   
            return data
        else:
            raise Exception("nothing to read, hint is empty")
            
            
    # this method will receive a dictionry, find all items that matvh the dictionary 
    #values and delete them
    def delete(self, _data):
        if _data is not None:
            data = self.read(_data) # checj if animal exists
            if data is None:
                print("Animal not found")
                return
            #if found delete the animal or animals
            self.database.animals.delete_many(_data)  # data should be dictionary 
            data = self.read(_data) #confirm if animal was deleted
            return data
        else:
            raise Exception("nothing to read, hint is empty")
            
    # this method update usin the id of the collection, one can also update using any key
    def update(self, _keys,_data):
        if _data is not None and _keys is not None:
            self.database.animals.update_many(_keys,{'$set':_data})  # _keys will check for the doc to update 
            data = self.read(_data)
            return data
        else:
            raise Exception("please nter both key and data to modify the collection")