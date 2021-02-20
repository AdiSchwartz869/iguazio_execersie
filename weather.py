import requests
from bs4 import BeautifulSoup

search = "weather in tel aviv in celsius"
URL = "https://www.google.com/search?q=" + search

req = requests.get(URL)
sav = BeautifulSoup(req.text, "html.parser")
update = sav.find("div", class_ = "BNeawe").text
print "The current weather in Tel-Aviv is: " , update
