#/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request
from io import BytesIO
import gzip
import re
import os
import time
import ssl

i = 0
def getHtml(url):
    send_headers = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 65.0.3325.181 Safari / 537.36',
        'Accept': 'text / html, application / xhtml + xml, application / xml; q = 0.9, image / webp, image / apng, * / *;q = 0.8',
        'Connection': 'keep-alive'
    }
    context = ssl._create_unverified_context()
    urls = urllib.request.Request(url, headers=send_headers)
    html = urllib.request.urlopen(urls, context=context)
    if html.getcode() == 200:
        print ("已捕获",url,"目标站数据。。。")
        return html
    else:
        print ("访问出现错误。。。错误代码："),html.getcode()
        return None

def callBackFunc(block_Num,block_Size,total_Size):
    download_Percent = 100.0 * block_Num * block_Size /total_Size
    if download_Percent > 100:
        download_Percent = 100
    print("正在下载第",i,"张图片，已下载 %",download_Percent)

if __name__ == '__main__':
    gate_URL = "https://www.7797mk.com/pic/5/"
    html = getHtml(gate_URL)
    # print(html)
    html_Doc = html.read()
    buff = BytesIO(html_Doc)
    f = gzip.GzipFile(fileobj=buff)
    html_Doc = f.read().decode('utf-8')
    print(html_Doc)

    if html != None:
        soupHtml = BeautifulSoup(html_Doc, "lxml", from_encoding="utf-8")
        divs = soupHtml.findAll('a', target="_blank")
        print(divs)
        flag = 1
        for div in divs:
            div_Doc = str(div)
            soupDiv = BeautifulSoup(div_Doc, "lxml", from_encoding="utf-8")
            if soupDiv.find('img') != None:
                tag_img = soupDiv.find('img')
                filename = "Background"+str(time.time())
                tag_a = soupDiv.find('a')
                img_direction_url = tag_a['href']
                os.mkdir(filename)
                print("已创建目录")
                print(filename)
                print("开始下载资源。。。")
                img_Html = getHtml(img_direction_url)
                img_Doc = img_Html.read()
                while True:
                    i = i + 1
                    soup_Img_Doc = BeautifulSoup(img_Doc, "lxml", from_encoding="gb18030")
                    download_btn = soup_Img_Doc.find('a', class_="down-btn")
                    img_url = download_btn['href']
                    print("需要下载的图片URL",img_url)
                    _path_ = os.path.abspath(filename)
                    path = os.path.join(_path_, img_url[-6:])
                    urllib.request.urlretrieve(img_url,path,callBackFunc)
                    if i == 3:
                        break
                    else:
                        img_Tag_a = soup_Img_Doc.find('a', href=re.compile(r"\d_?.html"))
                        img_direction_url = "http://www.7797mk.com"+img_Tag_a['href']
                        img_Html = getHtml(img_direction_url)
                        img_Doc = img_Html.read()
                i = 0
    else:
        print ("获取失败。。。")