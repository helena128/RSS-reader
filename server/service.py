import repository
import parser
from bson import json_util

def save_rss(rss_link):
	rss_inf, entries = parser.parse_source(rss_link)
	repository.save_data(rss_inf, entries, rss_link)

def get_feeds(rss_link, feed_per_page, page_number):
	return json_util.dumps(list(repository.get_feeds(rss_link, feed_per_page, page_number)))

def get_all_rss():
	return json_util.dumps(list(repository.get_all_rss()))

if __name__ == '__main__':
	save_rss('http://www.reddit.com/r/python/.rss')