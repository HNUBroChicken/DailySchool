# -*- coding: UTF-8 -*-
import info
import function

# 定义手机型号
model = info.MI_9
# 定义身体状况
status = info.situation


# 点击第一个选项
def click_first():
    function.click(model['firstKey'][0], model['firstKey'][1])


# 点击第二个选项
def click_second():
    function.click(model['secondKey'][0], model['secondKey'][1])


# 打开今日校园app
def today_school_open():
    function.app_open("com.wisedu.cpdaily/com.wisorg.wisedu.home.ui.HomeActivity")  # 打开APP


# 进入主入口
def main_entrance():
    function.click(model['main'][0], model['main'][1])
    function.delay(1)  # 此处增加延迟，因为加载填报页面较慢


# 滑动至底部
def slide_to_bottom():
    function.slide(500, 2000, 500, 1000, 100)  # 参数可修改，能滑至底部即可


# 填写是否入苏返苏
def is_back():
    function.click(model['isBack'][0], model['isBack'][1])
    if status['isBack']:  # 如果反苏
        click_first()
    else:
        click_second()


# 填写本人健康状态
def my_status():
    function.click(model['myStatus'][0], model['myStatus'][1])
    if status['myStatus']:  # 如果状态正常
        click_first()
    else:
        click_second()


# 填写是否就诊
def is_sick():
    function.click(model['isSick'][0], model['isSick'][1])
    if status['isSick']:  # 如果就诊
        click_first()
    else:
        click_second()


# 填写家人情况
def parents_status():
    function.click(model['parentsStatus'][0], model['parentsStatus'][1])
    if status['parentsStatus']:  # 如果情况正常
        click_first()
    else:
        click_second()


# 填写心理状况
def mind_status():
    function.click(model['mindStatus'][0], model['mindStatus'][1])
    if status['mindStatus']:  # 如果状况正常
        click_first()
    else:
        click_second()


# 填写体温
def temperature():
    function.click(model['temperature'][0], model['temperature'][1])
    function.text_input(status['temperature'])  # 输入体温
    function.click(model['exit'][0], model['exit'][1])  # 关闭软键盘


# 提交数据
def submit():
    function.click(model['submit'][0], model['submit'][1])
