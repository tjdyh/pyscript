# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import gzip
from io import BytesIO
import re
import os
import time
import threading

#当前文件所在目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))



def getHtml(url):
    r = requests.get(url)
    r.encoding  = 'utf-8'
    # print(type(r))
    # print(type(r.text))
    # buff = BytesIO(r.text)
    # f = gzip.GzipFile(fileobj=buff)
    html = r.text
    # print(html)
    return html

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
    for i in range(20):
        th = threading.Thread(target=func_test, args=[arg1])
        th_lst.append(th)
    print(th_lst)
    for th in th_lst:
        print("一个线程启动")
        th.start()
    for th in th_lst:
        print("等待线程结束，阻塞")
        th.join()
    t2 = time.time()
    t = t2-t1
    print("使用时间：%f" % t)
    return t


if __name__ == '__main__':
    url = "https://www.8848mk.com/pic/7/index.html"
    html = getHtml(url)
    # print(html)
    # '''
    soup = BeautifulSoup(html,"lxml")
    # print(type(soup))
    # print(soup)
    soup_a = soup.find_all('a',{'target':"_blank"})
    # soup_a = soup.find_all('li')
    # print(soup.find_all(text=regex))
    # print(type(soup_a))
    # print(soup_a)
    th_list = []
    for i in soup_a:
        # print(i.get("href"))
        regex = re.search('/pic/[1-7]/(.*?).html',i.get("href"))
        if regex:
            # print(i.get("href"))
            uri = i.get("href")
            goal_url = "https://www.8848mk.com" + uri
            print(goal_url)
            img_urls = getImg(goal_url)
            # print(img_urls)
            th_list = th_list + img_urls
    # print(th_list)
    # print(len(th_list))
    # mul_threads(downloadImg, th_list)
    #         th = threading.Thread(target=downloadImg, args=[img_urls])
    #         th_list.append(th)
    # print(th_list)
    # for t in th_list:
    #     print("一个页面的线程")
    #     t.start()
    # for t in th_list:
    #     print("线程阻塞")
    #     t.join()
    # '''
    # i=2
    # nextHtmlUrl  = url + "index_" + str(i) + ".html"
    # print(nextHtmlUrl)

# if __name__ == '__main__':
#     img_url = "https://www.3039mk.com/pic/5/2019-12-01/25460.html"
#     img_urls = getImg(img_url)
#     # downloadImg(img_urls)
#     mul_threads(downloadImg,img_urls)