import requests
from bs4 import BeautifulSoup
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

search = "weather in tel aviv in celsius"
URL = "https://www.google.com/search?q=" + search

req = requests.get(URL)
sav = BeautifulSoup(req.text, "html.parser")
update = sav.find("div", class_ = "BNeawe").text
result = u"The current weather in Tel-Aviv is:%s" %update
print (result)
