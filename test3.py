import pymongo

client = pymongo.MongoClient("mongodb+srv://kkvk001:kashif123@cluster0.4zfowaa.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['myinfo']
collection = database["sudh"]

record = collection.find()
for i in record:
    print(i)
    