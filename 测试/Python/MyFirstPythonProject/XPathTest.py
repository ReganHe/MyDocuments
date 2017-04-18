#coding=utf-8
#E:\Python34\Lib\site-packages\selenium\webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
if __name__ == '__main__':
    driver = webdriver.Ie() 
    print("open IE explorer")
    #web='http://ccmssit/clv'
    url='http://99.48.237.32/CCPClvServiceDev/UndoTask.htm'
    driver.get(url)
    driver.maximize_window()
    time.sleep(3)
    driver.switch_to_window(driver.current_window_handle)
    print ("title of current page is %s" %(driver.title))
    print ("url of current page is %s" %(driver.current_url))
    #xpath="//input[@id='btnPass']"
    #xpath="//div[@id='TabContainerMain_TabPanelContent']/div/table/tbody/tr/td/div/div[1]/div[1]"    
    #xpath="//div[@id='TabContainerMain_TabPanelContent']/div[@class='content01']"
    '''
    xpath="//div[@id='TabContainerMain_TabPanelContent']/div[@class='content01']/div/table/tbody/tr/td/div/div/div"
    ele=driver.find_elements_by_xpath(xpath)
    print(ele)
    print("元素名称:" + ele[0].text)
    print("元素内容:" + ele[1].text)
    print("元素内容:" + ele[2].text)
    print(dir(ele))
    '''
    xpath="//div[@id='TabContainerMain_TabPanelContent']/div[@class='content01']/div"
    groups=driver.find_elements_by_xpath(xpath)
    #print(dir(groups[0])) 
    groupIndex=1
    for group in groups:
        print ("第"+str(groupIndex)+"组:")        
        groupText=group.find_element_by_xpath(xpath +"["+str(groupIndex)+"]"+ "/div/span")
        print("组名:"+groupText.text)        
        print("组元素")
        groupXpath=xpath +"["+str(groupIndex)+"]"+ "/table/tbody/tr/td/div/div"
        elements=group.find_elements_by_xpath(groupXpath)
        elementIndex=1
        for element in elements:
            print ("第"+str(elementIndex)+"元素:")
            elementXpath=groupXpath +"["+str(elementIndex)+"]"+ "/div"
            elementContents=element.find_elements_by_xpath(elementXpath)
            print("Key:"+elementContents[0].text)
            print("Value:"+elementContents[1].text)
            #print(element.text)
            elementIndex+=1
            
        groupIndex+=1
        #print(groupIndex)
    #print(ele)
    driver.close()
    driver.quit()
