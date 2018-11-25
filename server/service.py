import repository
import parser
from bson import json_util

def save_rss(rss_link):
	rss_inf, entries = parser.parse_source(rss_link)
	repository.save_data(rss_inf, entries)

def get_feeds(rss_id, feed_per_page, page_number):
	return json_util.dumps(list(repository.get_feeds(rss_id, feed_per_page, page_number)))

def get_all_rss():
	return json_util.dumps(list(repository.get_all_rss()))

def get_rss_info(rss_id):
	return repository.get_rss_info(rss_id)

def get_number_of_feeds(rss_id):
	return repository.get_number_of_feeds(rss_id)

if __name__ == '__main__':
	save_rss('http://www.reddit.com/r/python/.rss')