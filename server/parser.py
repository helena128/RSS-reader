import feedparser
from rss_info import RssInfo 

def parse_source(soure):
	rss = feedparser.parse('http://www.reddit.com/r/python/.rss')

	rss_info = RssInfo(	rss['feed']['title'],
						rss['feed']['link'],
						rss.feed.subtitle )

	#print(rss_info)

	# num of entries
	print(len(rss['entries']))

	#print all entries
	#for post in rss.entries:
		#print(post.title + ": " + post.link)
		#print(post.updated)	
		#print()

if __name__ == '__main__':
	parse_source("tst")