# -*- coding: utf-8 -*-

import unittest
import urllib
import urllib.request
import urllib.parse
import json


class MyTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_list(self):
        data = {"Head":
                    {"IndexKeyId": "201506128000004",
                     "ChannelId": "005",
                     "ScenarioId": "0000D",
                     "Priority": 0},
                "Body":
                    {"CaseNo": "201506128000004",
                     "ApplierChName": "影像验证六",
                     "PrimIdCardNo": "01360202199108189236",
                     "AdditionalCardChName": "",
                     "AdditionalCardIdCardNo": "00",
                     "DepartmentName": "ＰＳＰＴ９",
                     "PromoterNo": "20105",
                     "PromoterChiName": "孙超",
                     "PrimMobilePhone":"",
                     "PrimDepartmentTel": "",
                     "Email": "",
                     "ChannelId": "005",
                     "ScenarioId": "0000D",
                     "EntityNmbr": "0000000092",
                     "DocId": 0,
                     "FileIds": {"0": ["308450abe12a48b096468639d4cf4f2f.DAT"]}
                     }
                }
        # 接口地址
        url = "http://99.48.236.130:9160/api/Add/"
        # http头信息
        header_dict = {'Content-Type': 'application/json','charset':'utf-8'}
        # tmp_data = urllib.parse.urlencode(data)
        tmp_data = json.dumps(data)
        # 发送请求报文
        req = urllib.request.Request(url=url, data=tmp_data.encode(encoding="utf-8", errors="ignore"), headers = header_dict, method='PUT')
        # 获取返回报文
        f = urllib.request.urlopen(req, timeout=120)
        response = f.read()
        print(response.decode())


if __name__ == '__main__':
    unittest.main()
