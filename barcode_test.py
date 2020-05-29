#!/usr/bin/env python
#-*-coding:utf-8-*-

import requests
import zxing

imgUrl='http://wx.51eanj.com/group1/M00/4B/00/CgD-oF7OSwOAcI_GAAASJNAJneY485.png'
local_filename = imgUrl.split('/')[-1]
print(local_filename)
r = requests.get(imgUrl)
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.content)

with open(local_filename,"wb") as f:
    f.write(r.content)

zx = zxing.BarCodeReader()
barcode = zx.decode('CgD-oF7OSwOAcI_GAAASJNAJneY485.png')
print(barcode.parsed)