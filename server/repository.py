import pymongo
import json
from bson import json_util
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["rss"]
rss_collection = db["rss"]
feed_collection = db["feeds"]
rss_collection.create_index('feed.link', unique = True)
feed_collection.create_index('link', unique = True)
feed_collection.create_index('src', unique = False)
feed_collection.create_index('updated', unique = False)

def save_data(rss_src, feeds):
	if rss_collection.count_documents({"feed.link" : rss_src["feed"]["link"]}) == 0:
		print('Adding')
		print(rss_collection.insert_one(rss_src))
	else:
		print('Already in db')

	for feed in feeds:
		#print(feed.link)
		if feed_collection.count_documents({"link": feed["link"]}) == 0:
			print('Saving')
			feed["src"] = rss_src["feed"]["link"]
			feed_collection.insert(feed)
		else:
			print('Already exists')

''' Getting information about '''
def get_feeds(rss_id, feed_per_page, page_number):
	rss_link = get_rss_link_by_id(rss_id)
	print('Get feeds with rss: ' + rss_link)
	skip_number = int(feed_per_page) * int(page_number)
	return feed_collection.find({"src": rss_link}).sort("updated", -1)\
		.skip(int(feed_per_page) * int(page_number)).limit(int(feed_per_page))

def get_number_of_feeds(rss_id):
	rss_link = get_rss_link_by_id(rss_id)
	return str(feed_collection.count_documents({"src": rss_link}))

''' Getting info about one rss source '''
def get_rss_info(rss_id):
	return rss_collection.find_one({"_id": ObjectId(rss_id)})

''' Getting info about all rss '''
def get_all_rss():
	return rss_collection.find()

def get_rss_link_by_id(rss_id):
	return rss_collection.find_one({"_id": ObjectId(rss_id)})["feed"]["link"]

#if __name__ == '__main__':
	#save()