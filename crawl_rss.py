import feedparser
import requests
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
from datetime import datetime



url = "https://cmsemeditation.blogspot.com/feeds/posts/default"

date = ""
words = ""

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
        # content.append(dateStr + "\n\n")
        global date, words
        date = dateStr
        words = soup.find("h2").string
        entries = soup.findAll("div")
        
        for entry in entries:
            content.append(entry.getText())
        
        return content
    
    return None
# getBibleContent()

def messageFormat():
  content = ""

  max_len = max(getBibleContent(), key=len)

  def add_prefix(match):
      return '\n\n' + match.group(0)
  
  content = content + date + '\n\n' + words + '\n'
  content = content + re.sub('\\d+\\s', add_prefix, max_len)


  #   i=i+1
  #   if i<3:
  #     content = content + entry + "\n\n"
  #   else:
  # # content = content + entry + "\n\n"
  #     content = content + entry + "\n"
  # if(i % 4 == 0):
#     content = content + "\n\n"
  print(content)
  return content


messageFormat();
