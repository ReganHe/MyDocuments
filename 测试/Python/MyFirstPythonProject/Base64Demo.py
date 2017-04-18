# -*- coding: utf-8 -*-

import unittest
import os
import urllib.request
import base64
#import requests

if __name__ == '__main__':
    try:
        # 获取上传文件路径
        pa = os.path.abspath("TestData/1.txt")
        print(pa)
        byteContent=open(pa , 'rb').read()
        print(byteContent)
        #strContent=base64.encodebytes(byteContent).decode(encoding="utf-8", errors="ignore")
        strContent=base64.b64encode(byteContent).decode(encoding="utf-8", errors="ignore")
        print("strContent=")
        print(strContent)
        temp= strContent.encode(encoding="utf-8", errors="ignore")
        print(temp)

        data ="file="+strContent+"&filename=test.txt"
        url = "http://99.48.236.130:9260/Base64Upload.ashx"
        header_dict = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Base 61bc6439867e4f33b31a4b81f2bdbe96'}
        re = urllib.request.Request(url=url, data=data.encode(encoding="utf-8", errors="ignore"), headers=header_dict, method='POST')
        resp = urllib.request.urlopen(re)
        f = resp.read()
        print(f.decode())
    except(ZeroDivisionError, Exception) as e:
        print(e)

