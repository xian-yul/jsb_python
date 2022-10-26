#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
selenium基类
本文件存放了selenium基类的封装方法
"""
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from common.readelement import Element
from config.conf import cm
from utils.log import Log
from utils.times import sleep

log = Log()

seller = Element('seller')
user = Element('user')


class WebPage(object):
    """selenium基类"""

    def __init__(self, driver):
        self.driver = webdriver.Chrome()
        self.driver = driver
        self.timeout = 20
        self.wait = WebDriverWait(self.driver, self.timeout)

    def get_url(self, url):
        """打开网址并验证"""
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
        #     log.info("打开网页：%s" % url)
        except TimeoutException:
            raise TimeoutException("打开%s超时请检查网络或网址服务器" % url)

    @staticmethod
    def element_locator(func, locator):
        """元素定位器"""
        name, value = locator
        return func(cm.LOCATE_MODE[name], value)

    def find_element(self, locator):
        """寻找单个元素"""
        return WebPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_element_located(args)), locator)

    def find_elements(self, locator):
        """查找多个相同的元素"""
        return WebPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_all_elements_located(args)), locator)

    def elements_num(self, locator):
        """获取相同元素的个数"""
        number = len(self.find_elements(locator))
        #   log.info("相同元素：{}".format((locator, number)))
        return number

    def input_text(self, locator, txt):
        """输入(输入前先清空)"""
        sleep(0.5)
        ele = self.find_element(locator)
        ele.clear()
        ele.send_keys(txt)

    #  log.info("输入文本：{}".format(txt))

    def is_click(self, locator):
        """点击"""
        self.find_element(locator).click()
        sleep()

    #   log.info("点击元素：{}".format(locator))

    def element_text(self, locator):
        """获取当前的text"""
        _text = self.find_element(locator).text
        #  log.info("获取文本：{}".format(_text))
        return _text

    @property
    def get_source(self):
        """获取页面源代码"""
        return self.driver.page_source

    def refresh(self):
        """刷新页面F5"""
        self.driver.refresh()
        self.driver.implicitly_wait(30)

    def base_get_img(self):
        self.driver.get_screenshot_as_file("./{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))

    def win_handles(self, num):
        self.driver.close()
        log.info('定位新标签')
        handles = self.driver.window_handles
        num = int(num)
        self.driver.switch_to.window(handles[num])
        sleep(0.2)

    def script(self, js_size):
        # js脚本 滚动条下拉
        js = "var q=document.documentElement.scrollTop=" + js_size
        self.driver.execute_script(js)
        log.info("js脚本滚动条下拉")

    def signing_contract(self):
        log.info('进入签署')
        sleep(2)
        iframe = self.find_element(user['签署窗口'])
        self.driver.switch_to.frame(iframe)
        sleep(2)
        self.is_click(user['签署按钮'])
        sleep(2)
        self.input_clear_text(user['签署文本框'], 999999)
        sleep(0.2)
        self.is_click(user['签署点击确定'])
        sleep()
        self.driver.switch_to.default_content()
        sleep()
        self.is_click(user['关闭签署窗口'])
        log.info("退出签署中")
        sleep(1)
        log.info('签署成功')

    def click_action(self, loc, num):
        text = 0
        ele = self.find_element(loc)
        while text < num:
            ActionChains(self.driver).click_and_hold(ele).perform()
            text += 1
        # 释放
        ActionChains(self.driver).release(ele).perform()

    def click_area(self):
        city = self.find_element(seller['点击市'])
        city.click()
        province = self.find_element(seller['点击省'])
        province.click()
        area = self.find_element(seller['点击区'])
        area.click()
        # log.info('选择的市 : ' + city.text + ',  所选择的省 : ' + province.text + ',   所选择的区 : ' + area.text)

    def fial_info(self):
        log.info('出现异常 或者 断言失败')
        self.base_get_img()
        log.info('当前url: ' + self.return_current_url())
        self.fail('测试失败')

    def return_current_url(self):
        return self.driver.current_url

    def input_clear_text(self, loc, text):
        loc_object = self.find_element(loc)
        loc_object.clear()
        loc_object.send_keys(keys.Keys.CONTROL, "a")
        for i in range(10):
            loc_object.send_keys(keys.Keys.BACKSPACE)
        loc_object.send_keys(text)

    def inputs_clear_text(self, loc, index, text):
        loc_object = self.find_elements(loc)[index]
        loc_object.clear()
        loc_object.send_keys(keys.Keys.CONTROL, "a")
        for i in range(10):
            loc_object.send_keys(keys.Keys.BACKSPACE)
        loc_object.send_keys(text)

    def script_top(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)  # 拖动到可见的元素去

    def implicitly_wait(self,time):
        self.driver.implicitly_wait(time)

