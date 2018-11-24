import pymongo
import json

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["rss"]
rss_collection = db["rss"]
feed_collection = db["feeds"]
rss_collection.create_index('feed.link', unique = True)
feed_collection.create_index('link', unique = True)
feed_collection.create_index('src', unique = False)
feed_collection.create_index('updated', unique = False)

def save_data(rss_src, feeds, rss_link):
	if rss_collection.count_documents({"feed.link" : rss_src["feed"]["link"]}) == 0:
		print('Adding')
		print(rss_collection.insert_one(rss_src))
	else:
		print('Already in db')

	for feed in feeds:
		#print(feed.link)
		if feed_collection.count_documents({"link": feed["link"]}) == 0:
			print('Saving')
			feed["src"] = rss_link
			feed_collection.insert(feed)
		else:
			print('Already exists')

''' Getting information about '''
def get_feeds(rss_link, feed_per_page, page_number):
	return feed_collection.find({"src": rss_link}).skip(int(feed_per_page) * 
		int(page_number)).limit(int(page_number))

''' Getting info about one rss source '''
def get_rss_info(rss_link):
	return rss_collection.find({'feed.link': rss_link})

''' Getting info about all rss '''
def get_all_rss():
	return rss_collection.find()

#if __name__ == '__main__':
	#save()