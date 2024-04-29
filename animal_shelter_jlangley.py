from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    
    def __init__(self, username, password):
        USER = 'aacuser'
        PASS = '5qjq7q5'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31733
        DB = 'AAC'
        COL = 'animals'
        
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
    
    # for project one
    # updated create and read methods for better error handling with try-except
    # updated create and read methods with better output for debugging and for
    # better visualization of success/fail during testing
    
    # method to implement the C in CRUD
    def create(self, data):
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True, data
            except Exception as e:
                print("Error occured during data insertion: ", str(e))
                return False, None
        else:
            raise ValueError("Nothing to save, because data parameter is empty")
            
    # method to implement the R in CRUD
    def read(self, data):
        if data is not None:
            try:
                result = list(self.collection.find(data))
                return result
            except Exception as e:
                print("Error occured during data query: ", str(e))
                return False, None
        else:
            raise ValueError("Nothing to view, because data parameter is empty")
            
    # method to implement the U in CRUD
    def update(self, data, newData):
        if data is not None:
            try:
                result = self.collection.update_many(data, { "$set": newData })
                print("Number of documents matched: ", result.matched_count)
                print("Number of documents modified: ", result.modified_count)
                
                # prints out the original data, with modifications
                updateData = self.collection.find(newData)
                for animal in updateData:
                    print(animal)
                return True, result.modified_count
            except Exception as e:
                print("Error occurred during data update: ", str(e))
                return False, None
        else:
            raise ValueError("Nothing to update, because data parameter is empty")
    
    # method to implement the D in CRUD
    def delete(self, data):
        if data is not None:
            try:
                result = self.collection.delete_many(data)
                print("Number of documents deleted: ", result.deleted_count)
                return True, result.deleted_count
            except Exception as e:
                print("Error occurred during data deletion: ", str(e))
                return False, None
        else:
            raise ValueError("Nothing to delete, because data paramter is empty")