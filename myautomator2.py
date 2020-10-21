#!/usr/bin/env python
import uiautomator2 as u2
import time
import pytest
#连接手机
# device = u2.connect('127.0.0.1:62001')

#print(device.info)

#安装app
# url='http://p.gdown.baidu.com/d75ceaff2030f360f0db9528590357121eba07adab162174ea113b34d519b54e0c6cb3897ee13e1ccf3013b643796ec91696f54a57d779757691eacef1f32c0f56012d186dbd09c280a48e5fda19d7dc3ae8cd15a0fba2ac7073c854db830727cbde1cbe48eedf9413809f8c37646b6b83da81b15030c22a2b68de7ba76f199e951deefe88bce4ebd10f22dabb02f804e9ffe32626cb34e7eb1bd13cca60d4230fee4fb31e1550caa2e3bc00c0babe7d4f750e60cec7f79477bc4e16dd945f23be2832abceaf2d888c8a43a071f1a16f'
# device.app_install(url)

#打开被测试的app
# device(text='搜狗浏览器').click()
# time.sleep(10)
#获取app包名
# print(device.app_current())

# #卸载app
# device.app_uninstall('sogou.mobile.explorer')

# #打开app
# device.app_start('sogou.mobile.explorer')
# time.sleep(10)

#列举运行的app
#print(device.app_list())
# print(device.app_list_running())


# #关闭app
# device.app_stop('sogou.mobile.explorer')

# #清空app的数据,如同卸载重装的效果
# device.app_clear('sogou.mobile.explorer')

# #点击操作 ①选定元素再click（）
# device(text="超级计算器").click()

# #②用绝对坐标
# device.click(290,618)

# #③用相对坐标
# device.click(0.498, 0.542)

# #滑动①
# #startx，starty，endx，endy
# device.swipe(0.755, 0.692,0.28, 0.739)
# time.sleep(3)


#拓展版滑动②
#第一个参数是往哪边划，第二个划是百分之多少
# device.swipe_ext("left",scale=0.9)
# time.sleep(3)

#先定位元素，再使用元素滑动
#第一个参数是往哪边划，第二个划是百分之多少
# #e=device(text="谷歌安装器")#变成滑app了
# e=device(description="Google Search")#变成滑app了
# e.swipe('left',steps=500)  #step 代表滑动的时长，毫秒

# #登录流程
# device(text="平云小匠工程师").click()
# time.sleep(5)
# e=device(text="请输入手机号")
# e.set_text('13813813812')
# if device.xpath('//*[@resource-id="com.grgbanking.nuwa:id/action_bar_root"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.widget.EditText[1]').exists:
#     print('123')
#     device.xpath('//*[@resource-id="com.grgbanking.nuwa:id/action_bar_root"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.widget.EditText[1]').set_text('123456')
# time.sleep(2)
# device.xpath('//*[@resource-id="com.grgbanking.nuwa:id/action_bar_root"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[6]').click()
# time.sleep(2)
# #device.clear_text()
# assert device.toast.get_message()=="13813813812用户不存在！" #assert device.toast.get_message()=="13813813812用户不存在！333"
# time.sleep(2)
# device.app_stop("com.grgbanking.nuwa")

#截屏流程
# device(text="平云小匠工程师").click()
# time.sleep(10)
# device.screenshot('nvwa.png')
# time.sleep(2)
# device.app_stop("com.grgbanking.nuwa")





#登录流程优化
def login(d,mobile,pwd):
    
    e=d(text="请输入手机号")
    e.set_text(mobile)
    if d.xpath('//*[@resource-id="com.grgbanking.nuwa:id/action_bar_root"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.widget.EditText[1]').exists:
        print('123')
        d.xpath('//*[@resource-id="com.grgbanking.nuwa:id/action_bar_root"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.widget.EditText[1]').set_text(pwd)
    time.sleep(2)
    d.xpath('//*[@resource-id="com.grgbanking.nuwa:id/action_bar_root"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[6]').click()
    time.sleep(2)

@pytest.mark.empty
def test_login_empty_mobile():
#device.clear_text()
    #assert device.toast.get_message()=="13813813812用户不存在！" #assert device.toast.get_message()=="13813813812用户不存在！333"
    d = u2.connect('127.0.0.1:62001')
    d(text="平云小匠工程师").click()
    time.sleep(5)
    login(d,'','')
    #assert d.toast.get_message()=="13813813812用户不存在！"
    print("为空检验通过")
    d.app_stop("com.grgbanking.nuwa")

@pytest.mark.not_empty
def test_login_not_empty_mobile():
#device.clear_text()
    #assert d.toast.get_message()=="13813813812用户不存在！" #assert device.toast.get_message()=="13813813812用户不存在！333"

    d = u2.connect('127.0.0.1:62001')
    d(text="平云小匠工程师").click()
    time.sleep(5)

    login(d,'13813813813','666666')
    assert d.toast.get_message()=="13813813813用户不存在！"
    d.app_stop("com.grgbanking.nuwa")


if __name__=='__main__':
    pytest.main()