from time import sleep
from page_base import BaiduPage

#定义页面的基础类，所有的页面都需要集成这个基础类
class BasePage(object):
    #初始化基础类
    def __init__(self,driver,url):
        self.driver=driver
        self.url=url
        self.page=BaiduPage(driver)

    #启动浏览器，访问指定页面
    def open(self):
        self.driver.get(self.url)
        #self.driver.maximize_window()

    #浏览器退出
    def quit(self):
        sleep(2)
        self.driver.quit()