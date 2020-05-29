# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request
import gzip
from io import BytesIO

request =  urllib.request.Request('https://www.7797mk.com/pic/5/')
response = urllib.request.urlopen(request)

buff = BytesIO(response.read())
f = gzip.GzipFile(fileobj=buff)
htmls = f.read().decode('utf-8')

print(htmls)