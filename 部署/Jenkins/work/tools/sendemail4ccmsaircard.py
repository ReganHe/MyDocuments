# -*- coding: gb2312 -*- 
import sys
from suds import WebFault
from suds.client import Client

if __name__ == "__main__":
    # sendemail.py "${strResult}" "${strProject}" "${jobUrl}"
    try:
        if len(sys.argv) < 4 :
            print "****ȱ�ٲ���, ʧ���˳�****"
            exit(0)
        url = 'http://ccms/portal/webservice/CMBMailService.asmx?WSDL'
        client = Client(url)
        # �ӿڸ�ʽ�� SendCMBEmail(to:string, cc:string, bcc:string, subject:string, content:string)
        subject = "Jenkins����״̬: ��" + sys.argv[1] +"��- " + sys.argv[2] 
        content = '''������� <a href="''' + sys.argv[3] + '''">'''+ sys.argv[3] + "</a> �鿴����"
        nameList = ["lenghj@cmbchina.com","wangxinhong@cmbchina.com","clarkmeng@cmbchina.com","caohan672226@cmbchina.com","ahy01101112@cmbchina.com" ]
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
