# -*- coding: gb2312 -*- 
'''
��ʱ����:
  1. ��ȡ����XML�ļ�(TODO),��ȡfirefly�뱾��workspaceĿ¼�Ķ�Ӧ��ϵ
  2. ��ȡ����XML�ļ�(TODO),��ȡJenkins��������fireflyĿ¼�Ķ�Ӧ��ϵ
  3. ��ȡfirefly�İ�װ·��
  4. ����firefly�������У�����workspace����·��
  5. ����firefly�������У����´���⣬��ø��´���·����Ϣ
  6. �������µĴ���·����Ӧ��Jenkins���񣬲�����Jenkins����
  7. ��������
'''

from __future__ import print_function
from threading  import Thread
import subprocess, urllib
import pycurl, time, os, re, sys

#["MMSC",      '"D:\\work\\hff_workspace\\MerchantMerchandiseServiceCenter\\update.bat" ./Code/Project/MSSC', '"D:\\work\\hff_workspace\\MerchantMerchandiseServiceCenter\\changelog.bat" ', 
#        "http://99.48.237.23:9090/jenkins/job/CCMS_MerchantMerchandiseServiceCenter/build?token=8542A00F103F6E9CA9EEBDB3B9365A35&cause=job_is_triger_by_code_change"],

# firefly ��������
SCM_UPDATE_SRC_CMD_LIST = [
  #Key(��ʾ�Ƿ���ͬһ��firefly��workspace), UPDATE Command,  CHANGELOG Command, TriggerUrl
  #["AirCard",   '"D:\\work\\hff_workspace\\AirCard\\update.bat" ./Code/Project/AirCard', '"D:\\work\\hff_workspace\\AirCard\\changelog.bat" ', 
  #      "http://99.48.237.23:9090/jenkins/job/AirCard/build?token=8542A00F103F6E9CA9EEBDB3B9365A35&cause=job_is_triger_by_code_change"],
  ["Installment",       '"D:\\work\\hff_workspace\\Installment\\update.bat" ./Code/Project/InstallmentWebAPI', '"D:\\work\\hff_workspace\\Installment\\changelog.bat" ', 
        "http://99.48.237.23:9090/jenkins/job/InstallmentWebAPI/build?token=8542A00F103F6E9CA9EEBDB3B9365A35&cause=job_is_triger_by_code_change"],
  ["MSP",       '"D:\\work\\hff_workspace\\MerchantServicePlatform\\update.bat" ./Code/Project/MSP', '"D:\\work\\hff_workspace\\MerchantServicePlatform\\changelog.bat" ', 
        "http://99.48.237.23:9090/jenkins/job/MerchantServicePlatform/build?token=8542A00F103F6E9CA9EEBDB3B9365A35&cause=job_is_triger_by_code_change"],
  ["FSM",       '"D:\\work\\hff_workspace\\FSM\\update.bat" ./Code/Project/FileServiceManage', '"D:\\work\\hff_workspace\\FSM\\changelog.bat" ', 
        "http://99.48.237.23:9090/jenkins/job/FSM/build?token=8542A00F103F6E9CA9EEBDB3B9365A35&cause=job_is_triger_by_code_change"],
  ["FSP",       '"D:\\work\\hff_workspace\\FSP\\update.bat" ./Code/Project/FileServicePlatform', '"D:\\work\\hff_workspace\\FSP\\changelog.bat" ', 
        "http://99.48.237.23:9090/jenkins/job/FSP/build?token=8542A00F103F6E9CA9EEBDB3B9365A35&cause=job_is_triger_by_code_change"],
  ["WCHAT",     '"D:\\work\\hff_workspace\\WeChat\\update.bat" ./Code/Project/WeChatSolution', '"D:\\work\\hff_workspace\\WeChat\\changelog.bat" ', 
        "http://99.48.237.23:9090/jenkins/job/WeChat/build?token=8542A00F103F6E9CA9EEBDB3B9365A35&cause=job_is_triger_by_code_change"],
  ["CLM",     '"D:\\work\\hff_workspace\\ConsumerListManagement\\update.bat" ./Code/Project/ConsumerListManagement', '"D:\\work\\hff_workspace\\ConsumerListManagement\\changelog.bat" ', 
        "http://99.48.237.23:9090/jenkins/job/ConsumerListManagement/build?token=8542A00F103F6E9CA9EEBDB3B9365A35&cause=job_is_triger_by_code_change"],
  ["MMSC",      '"D:\\work\\hff_workspace\\MMSC\\update.bat" ./Code/Project/MSSC', '"D:\\work\\hff_workspace\\MMSC\\changelog.bat" ', 
       "http://99.48.237.23:9090/jenkins/job/MMSC/build?token=8542A00F103F6E9CA9EEBDB3B9365A35&cause=job_is_triger_by_code_change"],
  ["FSPV2",     '"D:\\work\\hff_workspace\\FSPV2\\update.bat" ./Code/Project/FileServicePlatformV2', '"D:\\work\\hff_workspace\\FSPV2\\changelog.bat" ', 
        "http://99.48.237.23:9090/jenkins/job/FSPV2/build?token=8542A00F103F6E9CA9EEBDB3B9365A35&cause=job_is_triger_by_code_change"],
  ["HBD",     '"D:\\work\\hff_workspace\\HBD\\update.bat" ./Code/NewProjectV2', '"D:\\work\\hff_workspace\\HBD\\changelog.bat" ', 
        "http://99.48.237.23:9090/jenkins/job/HBD/build?token=8542A00F103F6E9CA9EEBDB3B9365A35&cause=job_is_triger_by_code_change"],
  ["Vortex",  '"D:\\work\\hff_workspace\\Vortex\\update.bat" ./Ӱ�����API/Code/VortextApi', '"D:\\work\\hff_workspace\\Vortex\\changelog.bat" ', 
        "http://99.48.237.23:9090/jenkins/job/Vortex/build?token=8542A00F103F6E9CA9EEBDB3B9365A35&cause=job_is_triger_by_code_change"],
  ["GW",  '"D:\\work\\hff_workspace\\GW\\update.bat" ./Code/Project/GW.Web', '"D:\\work\\hff_workspace\\GW\\changelog.bat" ', 
        "http://99.48.237.23:9090/jenkins/job/GW/build?token=8542A00F103F6E9CA9EEBDB3B9365A35&cause=job_is_triger_by_code_change"]
]

# ������ܣ�������Ľ���
FF_UPDATE_ACTIONS = ["update", "����", "create", "����", "add", "���", "delete", "ɾ��", "remove", "ɾ��", "modify", "�޸�"]

G_JOB_DONE = False
def monitor_thread(task_process, CHGLOG_CMD):
    global G_JOB_DONE 
    tryTimes = 6 # ���ȴ�6��
    while(G_JOB_DONE == False and tryTimes > 0):
        time.sleep(1)
        tryTimes -= 1 
    else:
        if G_JOB_DONE == False :
            print("terminate process(timeout): "+CHGLOG_CMD)
            task_process.terminate()

def get_current_java_pidlist():
    taskListCmd = '''tasklist /V /FO LIST /FI "IMAGENAME eq java.exe"'''
    processInfo = sys_command(taskListCmd)
    pidList = []
    for oneLine in processInfo.splitlines():
        oneLine = oneLine.strip()
        m = re.match(r"PID[ ]*\:[ ]+([0-9]+)", oneLine)
        if m == None:
            continue
        pidList.append(m.group(1))
    return pidList

def taskkill_bypid(pidList):
    taskkillCmd = "taskkill /F /PID "
    for pid in pidList:
        sys_command(taskkillCmd + str(pid))

def get_changelog(CHGLOG_CMD, filePath):
    global G_JOB_DONE
    
    # ��ʼjava.exe����PID�б�
    origPidList = get_current_java_pidlist()
    time.sleep(1)
    
    proc = subprocess.Popen(CHGLOG_CMD + ' "'+ filePath +'"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    userName = None
    updateTime = None
    G_JOB_DONE = False
    maxReadLines = 15 # ������15��
    monitor = Thread(target=monitor_thread, args=(proc, CHGLOG_CMD))
    monitor.daemon = True # thread dies with the program
    monitor.start()
    while maxReadLines > 0 :
        orig_line = proc.stdout.readline()
        new_line = orig_line.lower().strip()
        # ��ȡ�ύ�û���Ϣ
        if new_line.startswith("user") :
            m = re.match(r"user\:(.*)", new_line)
            if m != None:
                userName = m.group(1).strip()
        elif new_line.startswith("�û�") :
            m = re.match(r"�û�\:(.*)", new_line)
            if m != None:
                userName = m.group(1).strip()
        #��ȡ�ύʱ��
        if new_line.startswith("last modified time") :
            m = re.match(r"last modified time\:(.*)", new_line)
            if m != None:
                updateTime = m.group(1).strip()
        elif new_line.startswith("�������ʱ��") :
            m = re.match(r"�������ʱ��\:(.*)", new_line)
            if m != None:
                updateTime = m.group(1).strip()
        
        print(orig_line, end="")
        if (userName == None or updateTime == None):
            maxReadLines -= 1 # ����Ҫ�����������
        else:
            maxReadLines = 0 # ������ȥ����
    else:
        print("terminate process(normal): "+CHGLOG_CMD)
        proc.terminate()
    G_JOB_DONE = True
    monitor.join() # ���߳̽�����procҲ�����
    proc.wait()
    if userName == None: userName = "�޷���ȡ�û�"
    if updateTime == None: updateTime = "�޷���ȡʱ��"
    
    # ǿ�ƽ����½���java����. FIXME���˴����ܴ��ڷ��ա�
    time.sleep(1)
    newPidList = get_current_java_pidlist()
    pidToKill = []
    for pid in newPidList:
        if not (pid in origPidList):
            pidToKill.append(pid)
    taskkill_bypid(pidToKill)
    
    return [userName, updateTime]

def sys_command(command):
    output_msg = ""
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    maxReadLines = 2000 # ������2000��
    while maxReadLines > 0 :
        proc.poll()
        new_msg = proc.stdout.readline()
        if new_msg == "" and proc.returncode != None :
            print("...terminate UPDATE process(normal)...")
            proc.terminate() # ��������ҲҪɱ����
            break
        print(new_msg, end="")
        output_msg += new_msg
        maxReadLines -= 1
        time.sleep(0.1) # �˴�Ҫ��ʱ
    else:
        print("...terminate UPDATE process(unhandled)...")
        proc.terminate()
        output_msg, err_msg = proc.communicate()
    return output_msg

def get_update_file_info(result):
    fileList = []
    tmpFlag = False
    for oneLine in result.splitlines():
        oneLine = oneLine.strip()
        if tmpFlag == False:
            # ���ñ�־λ
            if oneLine.lower().startswith("updating local files") or oneLine.lower().startswith("���±����ļ�"):
                tmpFlag = True
            #��û���ҵ�"updating local files"��֮ǰ�������к�������
            continue 
        m = re.match(r"([^ ]+)[ ]+(.*)", oneLine)
        if m == None:
            continue
        tmpAction = m.group(1)
        if (tmpAction.lower() in FF_UPDATE_ACTIONS) :
            tmpFilePath = m.group(2).strip()
            fileList.append(tmpFilePath.lower()) # �ļ�·��ȫ��ת��ΪСд
    return fileList

def triggerBuileJob( jobUrl ):
    c = pycurl.Curl()
    c.setopt(pycurl.URL, jobUrl)
    c.setopt(pycurl.VERBOSE, 0)
    c.setopt(pycurl.USERPWD, 'jenkins:1qaz@WSX')
    c.perform()
    # ��鷵�ؽ��
    http_code = c.getinfo(pycurl.HTTP_CODE)
    if (200 <= http_code and http_code < 300) :
        return True
    else:
        return False

if __name__ == "__main__":
    # 1. ִ�и��´�������
    triggerJobInfoList = []
    DelayTimeDict = dict()
    for Key, updateCmd, chglogCmd, triggerUrl in SCM_UPDATE_SRC_CMD_LIST:
        result = sys_command(updateCmd)
        updateInfo = get_update_file_info(result)
        if len(updateInfo) > 0:
            # �ҵ���Ҫ���������Ĵ������
            filePath = updateInfo[0] # �ҵ���һ���ļ�ȡ�����ύ��
            try:
                userName, updateTime = get_changelog(chglogCmd, filePath)
            except Exception as Err:
                print(" .... cannot get changelog .... Err:" + str(Err))
                userName = "�޷���ȡ�û�"; updateTime = "�޷���ȡʱ��"
            # XXXXXXX ��ͬworkspace�Ĺ���֮����Ҫ��ʱ������firefly�ĳ�ͻ XXXXXXX
            if Key in DelayTimeDict:
                DelayTimeDict[Key] += 8  # ÿ����ʱ8��
            else:
                DelayTimeDict[Key] = 0
            triggerJobInfoList.append([triggerUrl, userName, updateTime, Key])
    #end for
    print(" ================== wait1 for 2 seconds ================== ")
    time.sleep(2)
    # 3. ����Jenkins����
    for triggerUrl, userName, updateTime, Key in triggerJobInfoList:
        # XXXXXXX ��ͬworkspace�Ĺ���֮����Ҫ��ʱ������firefly�ĳ�ͻ XXXXXXX
        if Key in DelayTimeDict and DelayTimeDict[Key] > 0:
            DelayTimeDict[Key] -= 8
            time.sleep(8)
        # ��������
        causeInfo = "�����ύ��:"+userName+", �ύʱ��:"+updateTime
        jobUrl = triggerUrl.replace("job_is_triger_by_code_change", urllib.quote(causeInfo.decode('gbk').encode("utf-8"), ""))
        if triggerBuileJob(jobUrl) == False :
            print("====!!!!trigger jenkins build job error!!!!====")
        else:
            pass # success!
    #end for
    print(" ================== wait2 for 2 seconds ================== ")
    time.sleep(2)
