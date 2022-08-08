import pymongo

client = pymongo.MongoClient("mongodb+srv://kkvk001:kashif123@cluster0.4zfowaa.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['myinfo']
collection = database["sudh"]


#data = collection.find({'companyName': 'iNeuron'})
d = collection.find({'courseOffered':{'$gt':'E'}})
for i in d:
    print(i)