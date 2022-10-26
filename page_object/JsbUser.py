#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from decimal import Decimal

from selenium.webdriver.common.by import By

import page_object.JsbSellerPage
from common.readelement import Element
from page.webpage import WebPage, sleep
from utils import tool_util
from utils.log import Log

user = Element('user')
log = Log()
user_url = {'24_home': 'http://192.168.101.24:8090/shop/home', '20_home': 'https://demo.jinsubao.cn/',
            '产学融合需求列表添加': 'http://192.168.101.24:8090/user-center/demand-information-form',
            '产学融合需求列表': 'http://192.168.101.24:8090/user-center/integration-production/demand-information-list',
            '产学融合法律服务添加': 'http://192.168.101.24:8090/user-center/legal-service-form',
            '产学融合研究成果添加': 'http://192.168.101.24:8090/user-center/research-result-form',
            '产学融合研究成果列表': 'http://192.168.101.24:8090/user-center/integration-production/research-resultList',
            '产学融合法律服务列表': 'http://192.168.101.24:8090/user-center/integration-production/legal-service-list',
            '24注册后': 'http://192.168.101.24:8090/home/index',
            '20注册后': 'https://demo.jinsubao.cn/home/index',
            '供需资讯列表url': 'http://192.168.101.24:8090/user-center/purchase-info/purchase-list',
            '采购需求发布url': 'http://192.168.101.24:8090/user-center/purchase-info/purchase-form',
            '市场信息发布url': 'http://192.168.101.24:8090/user-center/purchase-info/purchase-form',
            '24_order_url': 'http://192.168.101.24:8090/user-center/purchase-order',
            '20_order_url': 'https://demo.jinsubao.cn/user-center/purchase-order',
            '24_order_detail': 'http://192.168.101.24:8090/user-center/purchase-order-detail',
            '20_order_detail': 'https://demo.jinsubao.cn/user-center/purchase-order-detail'}
seller_url = {'24': 'http://192.168.101.24:8070/user/login', '20': 'https://slrdm.jinsubao.cn/'}
user_menu = {'地址管理': '点击地址管理', '产学融合': '买家用户中心产学融合', '供需资讯': '买家供需资讯'}


class JsbUser(WebPage):
    def user_login(self, serve, phone):
        if serve == '24':
            self.driver.get(user_url['24_home'])
        else:
            self.driver.get(user_url['20_home'])
        self.click_user_login(phone)

    def click_user_login(self, phone):
        self.is_click(user['登录'])
        log.info('在买家首页点击登录按钮')
        self.input_text(user['登录手机号'], phone)
        log.info('输入登录手机号: ' + phone)
        self.is_click(user['验证码按钮'])
        log.info('点击验证码按钮')
        self.is_click(user['登录按钮'])
        log.info('点击登录')
        try:
            login_phone = self.element_text(user['登录后手机号'])
            assert set(login_phone).issubset(set(phone))
            log.info('比较后登录前输入手机号 :' + phone + '  与登录后一致 :' + login_phone)
        except AssertionError:
            self.fial_info()

    def order_amount_judgment(self, code, price):
        flag = 'true'
        if code == 1:
            product_detail = self.find_elements(user['订单_总计信息'])
            product_num = product_detail[1].text
            product_freight = product_detail[3].text
            product_freight = product_freight[1:]
            product_actual = product_detail[4].text
            product_actual = product_actual[1:]
            if Decimal(product_actual) == (Decimal(price) * Decimal(product_num)) + Decimal(
                    product_freight):
                log.info(
                    "金额判断一致  _________ 实付款  " + product_actual + " == 单价  " + price + " * 数量  " + product_num + " + 运费  " + product_freight)
            else:
                log.info(
                    "金额判断不一致  _________ 实付款  " + product_actual + " == 单价  " + price + " * 数量  " + product_num + " + 运费  " + product_freight)
                flag = 'false'
                self.base_get_img()
        elif code == 2:
            raw_detail = self.find_elements(user['订单_总计信息'])
            raw_num = raw_detail[1].text
            raw_actual = raw_detail[3].text
            raw_actual = raw_actual[1:]
            if Decimal(raw_actual) == Decimal(price) * Decimal(raw_num):
                log.info(
                    "金额判断一致  _________ 实付款  " + raw_actual + " == 单价  " + price + " * 数量  " + raw_num)
            else:
                log.info(
                    "金额判断不一致  _________ 实付款  " + raw_actual + " == 单价  " + price + " * 数量  " + raw_num)
                flag = 'false'
                self.base_get_img()
        return flag

    def place_order_submit(self, serve):
        while not self.find_element(user['提交订单']).is_enabled():
            sleep(3)
            if self.find_element(user['提交订单']).is_enabled():
                self.find_element(user['提交订单']).click()
                sleep(2)
                break
            try:
                if serve == '24':
                    assert self.return_current_url() == user_url['24_order_url']
                else:
                    assert self.return_current_url() == user_url['20_order_url']
                log.info('订单提交成功')
            except AssertionError:
                self.fial_info()

    def place_product_order(self, serve, user_phone, seller_phone, product_name, shop_num, cart_type, address, limit):
        seller = page_object.JsbSellerPage.JsbSellerPage(self.driver)
        self.user_login(serve, user_phone)
        place_order_num = 0
        while place_order_num < limit:
            self.find_elements(user['买家导航栏'])[1].click()
            self.script('3000')
            self.find_element(user['制成品商城_搜索栏']).send_keys(product_name)
            self.find_elements(user['制成品商城_搜索查询'])[0].click()
            sleep(0.2)
            self.find_elements(user['制成品商城_商品'])[0].click()
            self.win_handles('-1')
            self.inputs_clear_text(user['制成品商城_制成品数量选择'], 0, shop_num)
            if cart_type == 1:
                self.find_elements(user['制成品商城_制成品加入货单'])[0].click()
                sleep(0.2)
                self.find_elements(user['加入货单_点击确定'])[0].click()
                sleep(10)
            else:
                product_price = self.element_text(user['制成品商城_制成品单价'])
                product_price = product_price[5:]
                self.find_element(user['制成品商城_制成品一键采购']).click()
                sleep(0.5)
                try:
                    if self.order_amount_judgment(1, product_price):
                        self.script('10000')
                        self.place_order_submit(serve)
                        sleep()
                        signature_detail = self.find_elements(user['订单列表_状态'])
                        signature = '不需要签署' in signature_detail[1].text
                        if signature:
                            self.product_order_pay(serve, signature)
                            seller.seller_order_deliver(serve, signature, seller_phone, address)
                            self.product_order_receipt(serve)
                        else:
                            seller.seller_product_order(serve, seller_phone)
                            self.product_order_pay(serve, signature)
                            seller.seller_order_deliver(serve, signature, seller_phone, address)
                            self.product_order_receipt(serve)
                except:

                    self.fial_info()
            place_order_num += 1
            log.info('当前下单次数 : ' + str(place_order_num) + '  预计下单次数  : ' + str(limit))

    def product_order_pay(self, serve, signature):
        if not signature:
            if serve == '24':
                self.driver.get(user_url['24_order_url'])
            else:
                self.driver.get(user_url['20_order_url'])
            self.find_elements(user['订单列表_按钮'])[0].click()
            sleep(0.2)
            self.find_elements(user['弹窗_确定'])[1].click()
            self.signing_contract()
        self.find_elements(user['订单列表_按钮'])[0].click()
        sleep()
        self.input_clear_text(user['支付界面_支付文本框'], '666666')
        self.find_element(user['支付界面_支付按钮']).click()
        sleep(3)
        try:
            if serve == '24':
                assert set(user_url['24_order_detail']).issubset(set(self.return_current_url()))
            else:
                assert set(user_url['20_order_detail']).issubset(set(self.return_current_url()))
                log.info('制成品订单支付成功')
        except AssertionError:
            self.fial_info()

    def product_order_receipt(self, serve):
        if serve == '24':
            self.driver.get(user_url['24_order_url'])
        else:
            self.driver.get(user_url['20_order_url'])
        sleep(0.5)
        self.find_elements(user['订单列表_按钮'])[0].click()
        self.find_elements(user['弹窗_确定'])[1].click()
        sleep(1)
        signature_detail = self.find_elements(user['订单列表_状态'])
        signature = '完成' in signature_detail[1].text
        if not signature:
            self.fial_info()
        log.info('买家制成品订单收货成功')
