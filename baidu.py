#!/usr/bin/env python3
#-*-coding:utf-8-*-

from bs4 import BeautifulSoup
from urllib import request
from urllib import error
import pprint

def getHtml(url):
    try:
        html = request.urlopen(url)
    except error.HTTPError as e:
        return None
    # pprint.pprint(html)
    soup = BeautifulSoup(html, "lxml")
    pprint.pprint(soup.find_all('p'))

if __name__ == '__main__':
    url = "http://www.sina.com"
    getHtml(url)