from selenium.webdriver.support.wait import WebDriverWait

import page


class Base:
    #初始化
    def __init__(self,driver):
        self.driver = driver


    #查找元素
    def base_find(self,loc,timeout=5,poll=1.0):

        return WebDriverWait(self.driver,timeout,poll).\
            until(lambda x:x.find_element(*loc))

    #点击方法
    def base_click(self,loc,timeout=5,poll=1.0):
        self.base_find(loc,timeout,poll).click()

    #输入方法
    def base_input(self,loc,text,timeout=5,poll=1.0):
        #定位
        input_value = self.base_find(loc,timeout,poll)
        #清空
        input_value.clear()
        #输入
        input_value.send_keys(text)
    #获取属性值
    def base_get_att(self,loc,value):
        el = self.base_find(loc)
        return el.get_attribute(value)

    #获取登录按钮属性
    def page_get_attribute(self,att):
        return self.base_get_att(page.login_btn,att)