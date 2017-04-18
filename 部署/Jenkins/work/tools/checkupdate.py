# -*- coding: gb2312 -*- 
'''
定时任务:
  1. 读取配置XML文件(TODO),获取firefly与本地workspace目录的对应关系
  2. 读取配置XML文件(TODO),获取Jenkins的任务与firefly目录的对应关系
  3. 获取firefly的安装路径
  4. 调用firefly的命令行，设置workspace本地路径
  5. 调用firefly的命令行，更新代码库，获得更新代码路径信息
  6. 分析更新的代码路径对应的Jenkins任务，并触发Jenkins构建
  7. 结束处理
'''

from __future__ import print_function
from threading  import Thread
import subprocess, urllib
import pycurl, time, os, re, sys

#["MMSC",      '"D:\\work\\hff_workspace\\MerchantMerchandiseServiceCenter\\update.bat" ./Code/Project/MSSC', '"D:\\work\\hff_workspace\\MerchantMerchandiseServiceCenter\\changelog.bat" ', 
#        "http://99.48.237.23:9090/jenkins/job/CCMS_MerchantMerchandiseServiceCenter/build?token=8542A00F103F6E9CA9EEBDB3B9365A35&cause=job_is_triger_by_code_change"],

# firefly 操作命令
SCM_UPDATE_SRC_CMD_LIST = [
  #Key(表示是否共享同一个firefly的workspace), UPDATE Command,  CHANGELOG Command, TriggerUrl
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
  ["Vortex",  '"D:\\work\\hff_workspace\\Vortex\\update.bat" ./影像调阅API/Code/VortextApi', '"D:\\work\\hff_workspace\\Vortex\\changelog.bat" ', 
        "http://99.48.237.23:9090/jenkins/job/Vortex/build?token=8542A00F103F6E9CA9EEBDB3B9365A35&cause=job_is_triger_by_code_change"],
  ["GW",  '"D:\\work\\hff_workspace\\GW\\update.bat" ./Code/Project/GW.Web', '"D:\\work\\hff_workspace\\GW\\changelog.bat" ', 
        "http://99.48.237.23:9090/jenkins/job/GW/build?token=8542A00F103F6E9CA9EEBDB3B9365A35&cause=job_is_triger_by_code_change"]
]

# 如果可能，添加中文进来
FF_UPDATE_ACTIONS = ["update", "更新", "create", "创建", "add", "添加", "delete", "删除", "remove", "删除", "modify", "修改"]

G_JOB_DONE = False
def monitor_thread(task_process, CHGLOG_CMD):
    global G_JOB_DONE 
    tryTimes = 6 # 最多等待6秒
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
    
    # 初始java.exe进程PID列表
    origPidList = get_current_java_pidlist()
    time.sleep(1)
    
    proc = subprocess.Popen(CHGLOG_CMD + ' "'+ filePath +'"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    userName = None
    updateTime = None
    G_JOB_DONE = False
    maxReadLines = 15 # 最多读入15行
    monitor = Thread(target=monitor_thread, args=(proc, CHGLOG_CMD))
    monitor.daemon = True # thread dies with the program
    monitor.start()
    while maxReadLines > 0 :
        orig_line = proc.stdout.readline()
        new_line = orig_line.lower().strip()
        # 获取提交用户信息
        if new_line.startswith("user") :
            m = re.match(r"user\:(.*)", new_line)
            if m != None:
                userName = m.group(1).strip()
        elif new_line.startswith("用户") :
            m = re.match(r"用户\:(.*)", new_line)
            if m != None:
                userName = m.group(1).strip()
        #获取提交时间
        if new_line.startswith("last modified time") :
            m = re.match(r"last modified time\:(.*)", new_line)
            if m != None:
                updateTime = m.group(1).strip()
        elif new_line.startswith("最近更改时间") :
            m = re.match(r"最近更改时间\:(.*)", new_line)
            if m != None:
                updateTime = m.group(1).strip()
        
        print(orig_line, end="")
        if (userName == None or updateTime == None):
            maxReadLines -= 1 # 还需要读入更多内容
        else:
            maxReadLines = 0 # 不用再去试了
    else:
        print("terminate process(normal): "+CHGLOG_CMD)
        proc.terminate()
    G_JOB_DONE = True
    monitor.join() # 子线程结束后，proc也会结束
    proc.wait()
    if userName == None: userName = "无法获取用户"
    if updateTime == None: updateTime = "无法获取时间"
    
    # 强制结束新建的java进程. FIXME：此处可能存在风险。
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
    maxReadLines = 2000 # 最多读入2000行
    while maxReadLines > 0 :
        proc.poll()
        new_msg = proc.stdout.readline()
        if new_msg == "" and proc.returncode != None :
            print("...terminate UPDATE process(normal)...")
            proc.terminate() # 正常结束也要杀进程
            break
        print(new_msg, end="")
        output_msg += new_msg
        maxReadLines -= 1
        time.sleep(0.1) # 此处要延时
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
            # 设置标志位
            if oneLine.lower().startswith("updating local files") or oneLine.lower().startswith("更新本地文件"):
                tmpFlag = True
            #在没有找到"updating local files"行之前，不进行后续操作
            continue 
        m = re.match(r"([^ ]+)[ ]+(.*)", oneLine)
        if m == None:
            continue
        tmpAction = m.group(1)
        if (tmpAction.lower() in FF_UPDATE_ACTIONS) :
            tmpFilePath = m.group(2).strip()
            fileList.append(tmpFilePath.lower()) # 文件路径全部转换为小写
    return fileList

def triggerBuileJob( jobUrl ):
    c = pycurl.Curl()
    c.setopt(pycurl.URL, jobUrl)
    c.setopt(pycurl.VERBOSE, 0)
    c.setopt(pycurl.USERPWD, 'jenkins:1qaz@WSX')
    c.perform()
    # 检查返回结果
    http_code = c.getinfo(pycurl.HTTP_CODE)
    if (200 <= http_code and http_code < 300) :
        return True
    else:
        return False

if __name__ == "__main__":
    # 1. 执行更新代码库操作
    triggerJobInfoList = []
    DelayTimeDict = dict()
    for Key, updateCmd, chglogCmd, triggerUrl in SCM_UPDATE_SRC_CMD_LIST:
        result = sys_command(updateCmd)
        updateInfo = get_update_file_info(result)
        if len(updateInfo) > 0:
            # 找到需要触发构建的代码更新
            filePath = updateInfo[0] # 找到第一个文件取代码提交人
            try:
                userName, updateTime = get_changelog(chglogCmd, filePath)
            except Exception as Err:
                print(" .... cannot get changelog .... Err:" + str(Err))
                userName = "无法获取用户"; updateTime = "无法获取时间"
            # XXXXXXX 相同workspace的构建之间需要延时，避免firefly的冲突 XXXXXXX
            if Key in DelayTimeDict:
                DelayTimeDict[Key] += 8  # 每次延时8秒
            else:
                DelayTimeDict[Key] = 0
            triggerJobInfoList.append([triggerUrl, userName, updateTime, Key])
    #end for
    print(" ================== wait1 for 2 seconds ================== ")
    time.sleep(2)
    # 3. 触发Jenkins任务
    for triggerUrl, userName, updateTime, Key in triggerJobInfoList:
        # XXXXXXX 相同workspace的构建之间需要延时，避免firefly的冲突 XXXXXXX
        if Key in DelayTimeDict and DelayTimeDict[Key] > 0:
            DelayTimeDict[Key] -= 8
            time.sleep(8)
        # 触发构建
        causeInfo = "代码提交人:"+userName+", 提交时间:"+updateTime
        jobUrl = triggerUrl.replace("job_is_triger_by_code_change", urllib.quote(causeInfo.decode('gbk').encode("utf-8"), ""))
        if triggerBuileJob(jobUrl) == False :
            print("====!!!!trigger jenkins build job error!!!!====")
        else:
            pass # success!
    #end for
    print(" ================== wait2 for 2 seconds ================== ")
    time.sleep(2)
