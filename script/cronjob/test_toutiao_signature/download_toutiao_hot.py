import copy
import time
from lxml import etree
from selenium import webdriver



def down(url):
    dirver = webdriver.Chrome(executable_path='D:/code/SDK/chromedriver_win32/chromedriver.exe')
    dirver.get(url)  # 加载url
    count = 1  # 执行次数，默认一次
    while True:
        response = dirver.page_source  # 获取网页源码
        print(response)
        html_str = etree.HTML(response)  # HTML格式展示
        print(html_str)


        print('******正在下载{}页数据******'.format(count))
        time.sleep(5)
        # 以下方法是点击“下一页”按钮，可以通过xpath定位，也可以通过linktext定位
        # dirver.find_element_by_xpath(r'//*[@id="articlelistnew"]/div[82]/span/span/span[1]/a[12]').click()
        dirver.find_element_by_link_text("下一页").click()
        count += 1  # 循环执行
        time.sleep(5)
        if count == 4:  # 设置爬的数据页数
            break
    print('****全部数据下载完成****')


if __name__ == '__main__':
    url = "https://www.toutiao.com/"
    down(url)