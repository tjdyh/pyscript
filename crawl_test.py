#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
import logging
from pprint import pprint

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
}

response = requests.request(method='get', url="http://www.xqiushu.com/t/6194/36289134.html", headers=headers)

# html =  response.content
# html_doc = str(html,'utf-8')
# print(html_doc)
# print(response.text.encode('utf-8'))
response.encoding='utf-8'
print(response.content)
with open('test1.html','wb') as f:
    f.write(response.content)