from base_page import BasePage
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    #定义一个id=kw的元素
    input_id=(By.XPATH,'//*[@id="kw"]')   #元组数据类型
    click_id=(By.ID,'su')
    #url ="http://www.baidu.com"
    str="小龙女"

    #定位搜索内容的填入
    def input_text(self,text):
        self.locator_element(*self.input_id).send_keys(text)

    #定位百度一下按钮，点击一次
    def click_element(self):
        self.locator_element(*self.click_id).click()

    #执行业务的方法
    def search_text(self):
        self.open()
        self.input_text(self.str)
        self.click_element()
        self.quit()