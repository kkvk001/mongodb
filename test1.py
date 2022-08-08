import pymongo

client=pymongo.MongoClient("mongodb+srv://kkvk001:kkvk001@cluster2.n8exmct.mongodb.net/?retryWrites=true&w=majority")
db=client.test
data={
     "name":"kashif"
}

database = client['myinfo']
collection = database['kk']
collection.insert_one(data)