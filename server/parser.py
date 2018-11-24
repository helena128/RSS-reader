import feedparser

def parse_source(src_link):
	rss = feedparser.parse(src_link)
	entries = rss.entries.copy()
	del rss["entries"]
	#print(rss)

	#print("\n================================\n")
	#print(entries)
	return rss, entries

if __name__ == '__main__':
	rss_inf, entries = parse_source('http://www.reddit.com/r/python/.rss')
	print('RSS: ' + str(rss_inf))