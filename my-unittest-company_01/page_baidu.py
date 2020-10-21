import unittest
from selenium import webdriver
from time import sleep
from search import SearchPage
from ddt import ddt,data

@ddt
class PageObjectUnit(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()

    def tearDown(self):
        sleep(2)
        self.sp.quit()

    @data("http://www.baidu.com")
    def test_a(self,url):
        self.sp=SearchPage(self.driver,url)
        self.sp.search_text()

if __name__=='__main__':
    unittest.main()
        