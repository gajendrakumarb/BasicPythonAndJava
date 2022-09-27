import pymongo

if __name__ == "__main__":
    print('welcome to MongoDB')
    myclient = pymongo.MongoClient('mongodb://localhost:27017')
    print(myclient)
    mydb = myclient['myTest_1_DB']
    mycollection1 = mydb['Sample_1_collection']
    testDictionory1 = {'name': 'java', 'level':'Medimum'}
    mycollection1.insert_one(testDictionory1)
    testDictionory2 = {'name': 'python', 'level':'Easy'}
    testDictionory3 = {'name': 'python', 'level':'Easy'}
    mycollection1.insert_one(testDictionory2)
    mycollection1.insert_one(testDictionory3)

    listOfDict1 = [{'name': 'c', 'level':'Easy'},
    {'name': 'c++', 'level':'medium'},
    {'name': 'statistics', 'level':'hard'},
    {'name': 'MusicTheory', 'level':'hard'}]
    
    mycollection1.insert_many(listOfDict1)

    mysearchitems = mycollection1.find({'name':'java'})
    print(list(mysearchitems))

    i = myclient.list_database_names()
    print(i)

    i= mydb.list_collection_names()
    print(i)

    mycollection1.update_one({'name':'java'},{"$set":{'icon':'coffee'}})
    mycollection1.update_many({'name':'java'},{"$set":{'icon':'coffee'}})