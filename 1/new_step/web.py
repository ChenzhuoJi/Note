from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")

soup=bs(html.read())
print(soup.prettify())
#print(soup.title.name)
#print(soup.h1)
#print(soup.get_text())
#nameList = soup.findAll("span", {"class":"green"})
#for name in nameList: 
#    print(name.get_text())