# Anchor extraction from HTML document
from bs4 import BeautifulSoup
from urllib.request import urlopen

# open new file and save it
f = open("python/crawling/nettext.rtfd", 'w') # open file

with urlopen('https://www.naver.com/') as response:
    soup = BeautifulSoup(response, 'html.parser')
    i = 1
    for anchor in soup.select("ul.list_realtime NM_RTK_VIEW_list_content span.keyword"):
        data = str(i)+anchor.get_text()+"\n"
        i +=1
        f.write(data)
    f.close()