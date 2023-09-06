import feedparser
import requests
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
from datetime import datetime



url = "https://cmsemeditation.blogspot.com/feeds/posts/default"


def getBibleContent():
    d = feedparser.parse(url)
    
    soup = BeautifulSoup(d.entries[0].summary,"html.parser")
    # print(soup)

    dateStr = ""
    dateStr = str(datetime.today().year) + "년 " + str(datetime.today().month) + "월" + " " + str(datetime.today().day) + "일"

    dateStr1 = ""
    dateStr1 = str(datetime.today().year) + "-" + str(datetime.today().month).zfill(2) + "-" + str(datetime.today().day).zfill(2)
    result = re.search(dateStr1, d.entries[0].updated)

    if result:
        content = []
        content.append(dateStr + "\n\n")
        # content.append(soup.find("h1").string)
        content.append(soup.find("h3").string + "\n\n")

        entries = soup.findAll("div")
        
        for entry in entries:
          # if entry.find("span", "number") :
          #    if not entry.find("br") :
          #       content.append(entry.getText() + "\n\n")
          # else:
          #    if entry.get('style') != None and "font-family: NanumGothic;" in entry.get('style'):
          #       content.append(entry.getText())
          content.append(entry.getText() + "\n\n")
        
        return content
    return None

def messageFormat():
  i = 0
  content = ""
  for entry in getBibleContent():
    content = content + entry
  print(content)
  return content


messageFormat();
