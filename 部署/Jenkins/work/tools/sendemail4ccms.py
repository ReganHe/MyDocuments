# -*- coding: gb2312 -*- 

import sys
from suds import WebFault
from suds.client import Client

if __name__ == "__main__":
    # sendemail.py "${strResult}" "${strProject}" "${jobUrl}"
    try:
        if len(sys.argv) < 4 :
            print "****缺少参数, 失败退出****"
            exit(0)
        url = 'http://ccms/portal/webservice/CMBMailService.asmx?WSDL'
        client = Client(url)
        # 接口格式： SendCMBEmail(to:string, cc:string, bcc:string, subject:string, content:string)
        subject = "Jenkins构建状态: 【" + sys.argv[1] +"】- " + sys.argv[2] 
        content = '''请打开链接 <a href="''' + sys.argv[3] + '''">'''+ sys.argv[3] + "</a> 查看详情"
        nameList = ["zhaofei2004@cmbchina.com",  "jianglei810@cmbchina.com",  "jianglujie@cmbchina.com", "xiemz@cmbchina.com",
            "lenghj@cmbchina.com", "clarkmeng@cmbchina.com", "sunconglong@cmbchina.com", "wangxinhong@cmbchina.com",
            "zhujianjing@cmbchina.com", "zhuangjun@cmbchina.com", "hongyanhua@cmbchina.com", ]
        emailList = ", ".join(nameList)
        returnCode = client.service.SendCMBEmail(emailList, "", "", subject.decode('gb2312'), content.decode('gb2312'))
        if (returnCode == None) :
            print "Send Message Success!"
        else:
            print "Send Message error: returncode = %s" % returnCode
    except WebFault, f:
        print f
    except Exception, e: 
        print e
