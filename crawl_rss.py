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
        content.append(dateStr)
        # content.append(soup.find("h1").string)
        content.append(soup.find("h3").string)

        entries = soup.findAll("span")
        
        for entry in entries:
          if entry.find("span", "number") :
             if not entry.find("br") :
                content.append(entry.getText())
            #  greenSpans = entry.find_all("span", style="font-family: NanumGothic; letter-spacing: 0.2px;")
             
          # greenSpans = entry.find_all("span", style="font-family: NanumGothic; letter-spacing: 0.2px;")
          # for span in greenSpans:
          #   content.append(span.getText())
          
        # print(entry)
        
        # test1 = soup.findAll("span")
        # greenSpan = entry[0].find_all("span", attrs={'style': {'color: green;'}})[0]
        # greenParent = greenSpan.parent
        # print(greenParent.getText())

        # while True:
        #     # print(greenParent.getText())
        #     content.append(greenParent.getText().replace('\xa0', ' '))
        #     if greenParent.nextSibling is None:
        #         break
        #     greenParent = greenParent.nextSibling

        print(content)
        return content
    return None
# getBibleContent()

def messageFormat():
  i = 0
  content = ""
  for entry in getBibleContent():
    content = content + entry + "\n\n"
  #   i=i+1
  #   if i<3:
  #     content = content + entry + "\n\n"
  #   else:
  # # content = content + entry + "\n\n"
  #     content = content + entry + "\n"
  # if(i % 4 == 0):
#     content = content + "\n\n"
  return content


messageFormat();
