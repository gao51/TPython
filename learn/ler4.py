from bs4 import BeautifulSoup
from urllib.request import urlopen

try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPErro as e:
    print(e)

bsobj = BeautifulSoup(html.read())
print(bsobj)