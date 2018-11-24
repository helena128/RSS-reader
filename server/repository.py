import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["rss"]
collection = db["news"]

def connect():
	mydict = {"name": "test"}
	x = collection.insert_one(mydict)
	print(x)

if __name__ == '__main__':
	connect()