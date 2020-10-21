import unittest
from selenium import webdriver
from time import sleep
from ReadEexcel import ReadExcel1
from ddt import ddt,data,unpack

@ddt
class TestYt(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://passport.ctrip.com/user/login")
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("end")

    @data(*ReadExcel1().read_excel())
    #不加*：[{'username': 'keywong', 'password': 123456}, {'username': 'meichen', 'password': 666666}]
    #加*：{'username': 'keywong', 'password': 123456}, {'username': 'meichen', 'password': 666666}
    # def test_xiecheng(self,data):
    #     self.driver.find_element_by_id("nloginname").send_keys(data['username'])
    #     self.driver.find_element_by_id("npwd").send_keys(data['password'])
    #     sleep(2)
    #     self.assertIn("ctrip",self.driver.current_url)
    #     #print(data)

    #等价于如下：
    @data(*ReadExcel1().read_excel())
    @unpack
    def test_xiecheng2(self,username,password):
        self.driver.find_element_by_id("nloginname").send_keys(username)
        self.driver.find_element_by_id("npwd").send_keys(password)
        sleep(2)
        self.assertIn("ctrip",self.driver.current_url)
        #print(username,password)

    #列表、元组、集合用*解包，字典用**解包，解包到结果为XXX，XXX，接收端为data，如果是列表、元组、集合可以直接用data[2]取参数，字典用data['key']。
    #                                   或者再用@unpack解包成单独的数据，接收端用username和password

if __name__ =='__main__':
    unittest.main()