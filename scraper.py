from bs4 import BeautifulSoup
from urllib.request import urlopen
f = urlopen('http://www.python.org/')

URL = 'http://'

if __name__ == '__main__':
    print('scraping at ', URL)
    print(f.read())