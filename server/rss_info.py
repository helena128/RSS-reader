class RssInfo:
	def __init__(self, title, link, subtitle):
		self.title = title
		self.link = link
		self.subtitle = subtitle

	def __str__(self):
		return "Title: " + self.title + " Link: " + self.link