#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
selenium基类
本文件存放了selenium基类的封装方法
"""
import time

import allure
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
order = Element('JsbUserOrder')
seller = Element('seller')
opera = Element('JsbOpera')
user = Element('user')
goods = Element('JsbSellerGoodsAdd')
seller_url = {'24': 'http://192.168.101.24:8070/user/login', '20': 'https://slrdm.jinsubao.cn/',
              '24_登录后': 'http://192.168.101.24:8070/dashboard', '20_登录后': 'https://slrdm.jinsubao.cn/dashboard',
              '供需列表': 'http://192.168.101.24:8070/product-manage/purchase-index/purchase-list',
              '24_raw_list': 'http://192.168.101.24:8070/product-manage/products-list/1',
              '20_raw_list': 'https://slrdm.jinsubao.cn/product-manage/products-list/1',
              '24_raw_add': 'http://192.168.101.24:8070/product-manage/raw-provide-form',
              '20_raw_add': 'https://slrdm.jinsubao.cn/product-manage/raw-provide-form',
              '24_product_list': 'http://192.168.101.24:8070/product-manage/products-list/2',
              '20_product_list': 'https://slrdm.jinsubao.cn/product-manage/products-list/2',
              '原料': 0, '制成品': 1,
              '船货': 2,
              '24_coupon_list': 'http://192.168.101.24:8070/marketing-manage/coupon-list',
              '24_coupon_add': 'http://192.168.101.24:8070/marketing-manage/creat-coupon/&1',
              '20_coupon_list': 'https://slrdm.jinsubao.cn/marketing-manage/coupon-list',
              '20_coupon_add': 'https://slrdm.jinsubao.cn/marketing-manage/creat-coupon/&1',
              '24_order_list': 'http://192.168.101.24:8070/order-manage/order-list',
              '20_order_list': 'https://slrdm.jinsubao.cn/order-manage/order-list'}
user_url = {'24': 'http://192.168.101.24:8090/shop/home', '20': 'https://demo.jinsubao.cn/'}

opera_url = {'24': 'http://192.168.101.24:8050/user/login', '20': 'https://admdm.jinsubao.cn/user/login',
             '24_home': 'http://192.168.101.24:8050/dashboard', '20_home': 'https://admdm.jinsubao.cn/dashboard'}

areas = ["'黑龙江'", "'辽宁'", "'吉林'", "'河北'", "'河南'", "'湖北'", "'湖南'", "'山东'", "'山西'", "'陕西'", "'安徽'",
         "'浙江'",
         "'江苏'",
         "'福建'", "'广东'", "'海南'", "'四川'",
         "'云南'", "'贵州'", "'青海'", "'甘肃'", "'江西'", "'台湾'", "'上海'", "'天津'", "'重庆'", "'内蒙古'", "'宁夏'",
         "'新疆'",
         "'西藏'",
         "'广西'"]


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

    @allure.step('截图')
    def base_get_img(self):
        self.driver.get_screenshot_as_file("./{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))

    @allure.step('切换标签页')
    def win_handles(self, num):
        self.driver.close()
        handles = self.driver.window_handles
        num = int(num)
        self.driver.switch_to.window(handles[num])
        sleep(0.2)

    @allure.step('界面滚动条下拉')
    def script(self, js_size):
        # js脚本 滚动条下拉
        js = "var q=document.documentElement.scrollTop=" + js_size
        self.driver.execute_script(js)

    @allure.step('法大大合同签署')
    def signing_contract(self):
        log.info('进入法大大合同签署')
        sleep(2)
        iframe = self.find_element(order['signing_window'])
        self.driver.switch_to.frame(iframe)
        sleep(3)
        self.is_click(order['signing_btn'])
        sleep(2)
        self.input_clear_text(order['signing_text'], 999999)
        sleep()
        self.is_click(order['signing_determine'])
        sleep()
        self.driver.switch_to.default_content()
        sleep()
        self.is_click(order['over_signing'])
        log.info("退出签署中")
        sleep(1)

    @allure.step('发货委托合同签署')
    def signing_consignment_contract(self):
        log.info('进入发货委托合同签署')
        sleep(2)
        iframe = self.find_elements(order['consignment_sign'])
        self.driver.switch_to.frame(iframe[-1])
        sleep(3)
        self.is_click(order['consignment_sign_btn'])
        sleep(2)
        self.input_clear_text(order['signing_text'], 999999)
        sleep(0.5)
        self.is_click(order['signing_determine'])
        sleep()
        self.driver.switch_to.default_content()
        sleep()
        over_signing = self.find_elements(order['over_signing'])
        over_signing[1].click()
        log.info("退出签署中")
        sleep(1)

    @allure.step('合同签署')
    def pickup_signing_contract(self):
        log.info('合同进入签署')
        sleep(2)
        iframe = self.find_element(order['self_lifting_signing'])
        self.driver.switch_to.frame(iframe)
        sleep(2)
        self.is_click(order['signing_btn'])
        sleep(2)
        self.input_clear_text(order['signing_text'], 999999)
        sleep(0.2)
        self.is_click(order['signing_determine'])
        sleep()
        self.driver.switch_to.default_content()
        sleep()
        self.is_click(order['over_signing'])
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

    @allure.step('地区点击选择')
    def click_area(self):
        self.is_click(seller['点击市'])
        sleep(0.1)
        self.is_click(seller['点击省'])
        sleep(0.1)
        self.is_click(seller['点击区'])
        sleep(0.1)
        # log.info('选择的市 : ' + city.text + ',  所选择的省 : ' + province.text + ',   所选择的区 : ' + area.text)

    def fial_info(self):
        self.base_get_img()
        log.error('当前url: ' + self.return_current_url())
        self.driver.quit()

    @allure.step('返回当前url')
    def return_current_url(self):
        return self.driver.current_url

    @allure.step('单元素文本框输入')
    def input_clear_text(self, loc, text):
        loc_object = self.find_element(loc)
        loc_object.clear()
        loc_object.send_keys(keys.Keys.CONTROL, "a")
        for i in range(10):
            loc_object.send_keys(keys.Keys.BACKSPACE)
        loc_object.send_keys(text)

    @allure.step('多元素文本框输入')
    def inputs_clear_text(self, loc, index, text):
        loc_object = self.find_elements(loc)[index]
        loc_object.clear()
        loc_object.send_keys(keys.Keys.CONTROL, "a")
        for i in range(10):
            loc_object.send_keys(keys.Keys.BACKSPACE)
        loc_object.send_keys(text)

    def script_top(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)  # 拖动到可见的元素去

    def implicitly_wait(self, wait_time):
        self.driver.implicitly_wait(wait_time)

    @allure.step('卖家进行登录')
    def seller_phone_login(self, serve, sellerPhone):
        if serve == '24':
            self.driver.get(seller_url['24'])
        else:
            self.driver.get(seller_url['20'])
        sleep(0.2)
        if self.return_current_url == seller_url['24_登录后'] or self.return_current_url == seller_url['20_登录后']:
            log.info('当前卖家已进行登录直接跳过输入账号密码过程')
        else:
            self.input_clear_text(order['seller_login_phone'], sellerPhone)
            self.is_click(order['seller_code_btn'])
            self.input_clear_text(order['seller_code_text'], 666666)
            self.is_click(order['seller_login_btn'])
            sleep()
            try:
                if serve == '24':
                    assert self.return_current_url() == seller_url['24_登录后']
                else:
                    assert self.return_current_url() == seller_url['20_登录后']
                log.info("卖家登录信息:   " + self.element_text(order['seller_login_info']))
                sleep(0.5)
            except AssertionError:
                self.fial_info()

    def getElementExistance(self, element_xpath):
        """通过元素xpath判断是否存在该元素,存在返回true，不存在返回false"""
        element_existance = True
        try:
            # 尝试寻找元素，如若没有找到则会抛出异常
            element = self.find_elements(element_xpath)
        except:
            element_existance = False

        return element_existance

    @allure.step('用户进行登录')
    def click_user_login(self, serve, user_phone):
        if serve == '24':
            self.driver.get(user_url['24'])
        else:
            self.driver.get(user_url['20'])
        str_text = self.find_elements(order['user_login'])
        login = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, '登录')))
        login.click()
        # self.is_click(order['user_login'])
        log.info('在买家首页点击登录按钮')
        self.input_text(order['login_phone'], user_phone)
        log.info('输入登录手机号: ' + user_phone)
        self.is_click(order['code_btn'])
        log.info('点击验证码按钮')
        self.is_click(order['login_btn'])
        log.info('点击登录')
        try:
            login_phone = self.element_text(order['user_login_phone'])
            login_phone = login_phone[:-2]
            login_phone = login_phone[7:]
            assert login_phone.find(user_phone)
            log.info('比较后登录前输入手机号 :' + user_phone + '  与登录后一致 :' + login_phone)
        except AssertionError:
            self.fial_info()
        sleep(0.2)

    @allure.step('运营进行登录')
    def opera_login(self, serve, opera_phone):
        if serve == '24':
            self.driver.get(opera_url['24'])
        else:
            self.driver.get(opera_url['20'])
        self.input_clear_text(opera['opera_login_phone'], opera_phone)
        self.is_click(opera['opera_login_code_btn'])
        self.input_clear_text(opera['opera_login_code_text'], 666666)
        sleep(0.2)
        self.is_click(opera['opera_login_btn'])
        sleep(0.2)
        try:
            if serve == '24':
                assert self.return_current_url() == opera_url['24_home']
            else:
                assert self.return_current_url() == opera_url['20_home']
            log.info('运营端登录成功')
        except:
            self.fial_info()

    @allure.step('牌号智能搜索功能')
    def goods_grade(self, grade_number, add_type, number, circulation):
        sleep(0.5)
        self.is_click(goods['智能搜索'])
        if add_type == 1:
            self.inputs_clear_text(goods['智能搜索_输入框'], -1, number)
            sleep(0.1)
            self.is_click(goods['智能搜索_搜索'])

        try:
            sleep(0.5)
            gradeNum = 0
            while gradeNum < circulation:  # < x 为循环次数 加载原料选择
                grade = self.find_elements(goods['智能搜索_原料选择'])
                sleep()
                self.script_top(grade[-1])
                sleep(2)
                gradeNum += 1
            sleep(2)
            log.info('当前获取的牌号数量: ' + str(len(grade)))
            log.info('选择的牌号为 : ' + grade[grade_number].text)
            grade[grade_number].click()
        except:
            self.fial_info()

    def opera_transverse_scrollto(self):
        js = 'document.getElementsByClassName("ant-table-body")[0].scrollLeft=20000'
        self.driver.execute_script(js)
