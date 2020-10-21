from base_page import BasePage
from selenium.webdriver.common.by import By
from page_base import BaiduPage

class SearchPage(BasePage):
    str="小龙女"

    #定位搜索内容的填入
    def input_text(self,text):
        self.page.baidu_input=text

    #定位百度一下按钮，点击一次
    def click_element(self):
        self.page.baidu_buttion.click()

    #执行业务的方法
    def search_text(self):
        self.open()
        self.input_text(self.str)
        self.click_element()
        self.quit()