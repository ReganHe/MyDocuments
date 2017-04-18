# -*- coding: utf-8 -*-

import unittest
import os
import urllib.request
#import requests

if __name__ == '__main__':
     # 定义调用的接口地址
    url = "http://99.48.236.130:9260/Base64Upload.ashx"
    # 获取上传文件路径
    pa = os.path.abspath("C:/Users/SE0002/Desktop/Muen.txt")
    # 定义请求头
    header_dict = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Base 61bc6439867e4f33b31a4b81f2bdbe96'}
    # 定义请求体
    data ="file="+"SGVsbG8gV29ybGQ"+"&filename=test.txt"
    try:
        """
        re = requests.post(url=url, data=data)
        print(re.text())
        """
        re = urllib.request.Request(url=url, data=data.encode(encoding="utf-8", errors="ignore"), headers=header_dict, method='POST')
        resp = urllib.request.urlopen(re)
        f = resp.read()
        print(f.decode())

    except(ZeroDivisionError, Exception) as e:
        print(e)

