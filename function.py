# -*- coding: UTF-8 -*-
import os
import time


# 实现延时,默认为0.5秒
def delay(t=0.5):
    time.sleep(t)


# 打开APP
def app_open(package):
    os.system("adb shell am start -n" + " " + package)
    delay(1)  # 打开APP时间可能较长需要延时等待


# 点击函数
def click(x, y):
    os.system("adb shell input tap" + " " + x + " " + y)
    delay()


# 滑动函数
def slide(x1, y1, x2, y2, slide_time=0):
    os.system(
        "adb shell input swipe" + " " + str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2) + " " + str(slide_time))
    delay(0.8)


# 输入文本
def text_input(text):
    os.system("adb shell input text" + " " + text)
