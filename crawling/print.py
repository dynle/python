# Anchor extraction from HTML document
from bs4 import BeautifulSoup
from urllib.request import urlopen

# just print out
with urlopen('https://www.oricon.co.jp/rank/js/d/2020-05-21/') as response:
    soup = BeautifulSoup(response, 'html.parser')
    i = 1
    for anchor in soup.select("div.content-rank-main h2.title"):
        print(str(i),anchor.get_text())
        i +=1