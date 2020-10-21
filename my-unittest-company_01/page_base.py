from poium import Page,PageElement

class BaiduPage(Page):
    baidu_input=PageElement(xpath='//*[@id="kw"]',describe="输入框")
    baidu_buttion=PageElement(id_='su',describe="确定按钮")