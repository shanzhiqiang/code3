import page
from base.base import Base


class PageLogin(Base):
    #关闭更新弹窗
    def page_close_alert(self):
        self.base_click(page.login_close_alert)

    #点击我
    def page_click_me(self):
        self.base_click(page.login_me)

    #点击登录/注册
    def page_click_login(self):
        self.base_click(page.login_)

    #输入手机号
    def page_phone(self,phone):
        self.base_input(page.login_phone,phone)

    #输入密码
    def page_pwd(self,pwd):
        self.base_input(page.login_pwd,pwd)

    #点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.login_btn)
    #登录组合业务方法
    def page_login(self,phone,pwd):
        self.page_phone(phone)
        self.page_pwd(pwd)
        self.page_click_login_btn()