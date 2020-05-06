import datetime
import time

now_time = datetime.datetime.now().strftime('%H:%M')
print("现在的时间是%s" % now_time)


class TimeGo(object):
    def __init__(self):
        self.times = {"7": "45", "14": "20", "19": "25"}
        self.i = 0
        self.user_list = {'user': "password"}  # 在这填写需要登录的用户名和密码

    def min_time(self):
        self.i = 0
        while self.i < 1:
            now = datetime.datetime.now()
            for key, val in self.times.items():
                # print(key, val)
                if str(now.hour) == key and str(datetime.datetime.now().strftime('%M')) == val:
                    # print("到点开始执行啦----------------qaqaqaqaqa")
                    self.user_login()
                    self.i += 1
                    break
            # 每隔60秒检测一次
            time.sleep(10)
        # print("over")

    def hour_time(self):
        while True:
            now = datetime.datetime.now()
            for key, val in self.times.items():
                if str(now.hour) == key:
                    print("到这个时间点了，开始登录，冲啊")
                    self.min_time()
                    print("这个时间点的已经打开操作完了，等待第二次到点操作")
            # 每隔一个小时检测一次
            time.sleep(3600)

    def user_login(self):
        from selenium import webdriver
        for key, val in self.user_list.items():
            # 1.创建Edge浏览器对象，这会在电脑上在打开一个浏览器窗口
            browser = webdriver.Chrome()
            # 2.通过浏览器向服务器发送URL请求
            browser.get('https://xuexi.boxuegu.com/video.html?courseId=2066')
            time.sleep(1)
            browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[1]/div[2]/p[1]/span").click()
            # print("点击了登录")
            time.sleep(0.5)
            # 获取指定的元素  输入账号密码
            browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[3]/div[2]/div[1]/input").send_keys(key)
            browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[3]/div[2]/div[2]/input").send_keys(val)
            browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[3]/div[2]/button").click()
            time.sleep(1)
            browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[5]/div/div/div[2]").click()  # 点击去上课
            # 延时，以便看清楚要进行的操作
            time.sleep(1)
            print("已经打开登录完毕")


if __name__ == '__main__':
    timeA = TimeGo()
    timeA.hour_time()

"""
运行  
时间也按照需要的时间更改即可
在self.init初始化方法里面填写账号密码即可，多账号以同格式填写即可


BUG 巨多，禁不起测试， 有待修改
第一版基本可用，不过也存在多次测试被封ip的可能性
同时，可实现同一用户多屏在线观看。(这个应该算博学谷的BUG)
"""