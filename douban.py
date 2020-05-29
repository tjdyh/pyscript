#-*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup

url = 'http://www.51eaju.com'
data = requests.get(url)
data.encoding = 'utf-8'
# print(data.text)

soup = BeautifulSoup(data.text, 'lxml')
print(soup)