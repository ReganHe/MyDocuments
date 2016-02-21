# -*- coding: utf-8 -*-

import unittest
import os
# import urllib.request
import requests



        # 定义调用的接口地址
        url = "http://99.48.236.130:9260/FileUpload.ashx"
        # 获取上传文件路径
        pa = os.path.abspath("C:/Users/SE0002/Desktop/Muen.txt")
        # 定义请求头
        # header = {"Content-Type": "multipart/form-data", "Authorization": "Base 61bc6439867e4f33b31a4b81f2bdbe96"}
        # 定义请求体
        data = {'fieldNameHere': ('Desert.jpg', open(pa).read(), 'image/jpeg')}
        try:
            re = requests.post(url=url, data=data)
            print(re.text())
            """
            re = urllib.request.Request(url=url, data=data, headers=header, method='POST')
            resp = urllib.request.urlopen(re)
            f = resp.read()
            print(f.decode())
            """
        except(ZeroDivisionError, Exception) as e:
            print(e)


