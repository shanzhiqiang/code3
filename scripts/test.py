from appium import webdriver
import time

# server 启动参数
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app的信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
#com.android.settings/.Settings
# 声明我们的driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)
#定位电池
dianchi = driver.find_element_by_xpath('//*[contains(@text,"电池")]')
#定位更多
more = driver.find_element_by_xpath('//*[contains(@text,"更多")]')
#从电池滑动到更多
driver.drag_and_drop(dianchi,more)
#点击安全
driver.find_element_by_xpath("//*[contains(@text,'安全')]").click()
#点击屏幕锁定方式
driver.find_element_by_xpath("//*[contains(@text,'屏幕锁定方式')]").click()
#点击图案
driver.find_element_by_xpath("//*[contains(@text,'图案')]").click()
#滑动
time.sleep(2)
TouchAction(driver).press(x="247",y="756").wait(200)\
    .move_to(x="728",y="756").wait(200).move_to(x="1202",y="756").perform()

time.sleep(2)
driver.quit()
