# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import gzip
from io import BytesIO
import re
import os
import time
import threading
import sys

#当前文件所在目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


#传入url,以字符串形式返回页面内容
def getHtml(url):
    #r的类型为class 'requests.models.Response'
    r = requests.get(url)
    r.encoding  = 'utf-8'
    # print(type(r))
    # print(type(r.text))
    # buff = BytesIO(r.text)
    # f = gzip.GzipFile(fileobj=buff)
    #html为str类型
    html = r.text
    # print(type(html))
    # print(html)
    return html

#传入上级url，获取上级页面内所有内容url,返url列表
def get_3_url(upper_url):
    goal_url_list = []
    html = getHtml(upper_url)
    soup = BeautifulSoup(html, "lxml")
    soup_a = soup.find_all('a', {'target': "_blank"})
    for i in soup_a:
        # print(i.get("href"))
        regex = re.search('/pic/[1-7]/(.*?).html',i.get("href"))
        if regex:
            # print(i.get("href"))
            uri = i.get("href")
            goal_url = "https://www.8848mk.com" + uri
            print(goal_url)
            goal_url_list.append(goal_url)
    print(goal_url_list)
    return goal_url_list




#传入图片面img_url,解析出页面所有图片地址，返回地址列表img_urls
def  getImg(img_url):
    print("看到我就是新的页面！")
    img_urls = []
    img_html = getHtml(img_url)
    bs_img = BeautifulSoup(img_html,"lxml")
    # print(type(bs_img))
    img_list = bs_img.find_all('img')
    # print(img_list)
    for i in img_list:
        img_urls.append(i.get("src"))
    # print(img_urls)
    return img_urls

#根据图片地址列表下载图片到目录IMG中，图片名保持原图片名
def downloadImg(img_urls):
    dir_name = 'IMG'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    for i in img_urls:
        filename = i.split('/')[-1]
        print(filename)
        r = requests.get(i)
        with open(os.path.join(BASE_DIR,dir_name)+"/"+filename, "wb") as f:
            f.write(r.content)

def mul_threads(func_test,arg1):
    #记录实验开始时间
    t1 = time.time()
    th_lst = []
    for i in range(10):
        th = threading.Thread(target=func_test, args=[arg1])
        th_lst.append(th)
    print(th_lst)
    for th in th_lst:
        # print("一个线程启动")
        th.start()
    # for th in th_lst:
    #     # print("等待线程结束，阻塞")
    #     th.join()
    t2 = time.time()
    t = t2-t1
    print("使用时间：%f" % t)
    return t


if __name__ == '__main__':
    # '''
    _url = "https://www.8848mk.com"
    num = 2
    while num <= 7:
        _2_url = "https://www.8848mk.com/pic/5/index_" + str(num) + ".html"
        print(_2_url)
        # url = "https://www.8848mk.com/pic/7/index_2.html"
        goal_urls = get_3_url(_2_url)
        if goal_urls:
            for g_url in goal_urls:
                img_url_list = getImg(g_url)
                print(img_url_list)
                mul_threads(downloadImg, img_url_list)
        else:
            print("没有这个二级页面！")
            sys.exit(1)
        num += 1
    # '''
