import urllib2
from bs4 import BeautifulSoup
import pyttsx
import sys

class Wikipedia:
	def crawlSimpleParagraph(self,url):
		req = urllib2.Request(url,headers={'User-Agent' : "Magic Browser"})
		con = urllib2.urlopen(req)
		soup = BeautifulSoup(con,'lxml')
		div = soup.find("div",{"class":"mw-parser-output"})
		for row in div.findAll('p'):
			print row.getText()
			engine.say(row.getText())
		engine.runAndWait()

engine = pyttsx.init()
engine.setProperty("rate",150)
voices = engine.getProperty('voices')
wiki = Wikipedia()
word = sys.argv[1]
#wiki.crawlSimpleParagraph("https://en.wikipedia.org/wiki/Dennis_Ritchie")
wiki.crawlSimpleParagraph("https://en.wikipedia.org/wiki/"+word)
