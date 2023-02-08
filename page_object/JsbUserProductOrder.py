#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from decimal import Decimal

from common.readelement import Element
from page.webpage import WebPage
from utils.log import Log
from utils.times import sleep

user = Element('JsbUserOrder')
log = Log()
user_url = {'24_home': 'http://192.168.101.24:8090/shop/home', '20_home': 'https://demo.jinsubao.cn/',
            '24_order_url': 'http://192.168.101.24:8090/user-center/purchase-order',
            '20_order_url': 'https://demo.jinsubao.cn/user-center/purchase-order',
            '24_order_detail': 'http://192.168.101.24:8090/user-center/purchase-order-detail',
            '20_order_detail': 'https://demo.jinsubao.cn/user-center/purchase-order-detail'}
seller_url = {'24': 'http://192.168.101.24:8070/user/login', '20': 'https://slrdm.jinsubao.cn/',
              '24_登录后': 'http://192.168.101.24:8070/dashboard', '20_登录后': 'https://slrdm.jinsubao.cn/dashboard',
              '供需列表': 'http://192.168.101.24:8070/product-manage/purchase-index/purchase-list',
              '24_raw_list': 'http://192.168.101.24:8070/product-manage/products-list/1',
              '20_raw_list': 'https://slrdm.jinsubao.cn/product-manage/products-list/1',
              '24_raw_add': 'http://192.168.101.24:8070/product-manage/raw-provide-form',
              '20_raw_add': 'https://slrdm.jinsubao.cn/product-manage/raw-provide-form',
              '24_product_list': 'http://192.168.101.24:8070/product-manage/products-list/2',
              '20_product_list': 'https://slrdm.jinsubao.cn/product-manage/products-list/2',
              '原料类型': '添加商品原料类型', '制成品类型': '添加商品制成品类型',
              '船货类型': '添加商品船货类型',
              '24_coupon_list': 'http://192.168.101.24:8070/marketing-manage/coupon-list',
              '24_coupon_add': 'http://192.168.101.24:8070/marketing-manage/creat-coupon/&1',
              '20_coupon_list': 'https://slrdm.jinsubao.cn/marketing-manage/coupon-list',
              '20_coupon_add': 'https://slrdm.jinsubao.cn/marketing-manage/creat-coupon/&1',
              '24_order_list': 'http://192.168.101.24:8070/order-manage/order-list',
              '20_order_list': 'https://slrdm.jinsubao.cn/order-manage/order-list'}
user_menu = {'地址管理': '点击地址管理', '产学融合': '买家用户中心产学融合', '供需资讯': '买家供需资讯'}


class JsbUserProductOrder(WebPage):

    def click_login_exit(self):
        self.is_click(user['买家退出登录按钮'])
        log.info('退出登录成功')

    def place_product_order(self, serve, user_phone, seller_phone, product_name, shop_num, cart_type, address,
                            sign_type, limit):
        self.click_user_login(serve, user_phone)
        place_order_num = 0
        while place_order_num < limit:
            if place_order_num > 0:
                self.find_elements(user['navigation_bar'])[2].click()
            else:
                self.find_elements(user['navigation_bar'])[1].click()
            self.script('3000')
            self.find_element(user['zcp_search']).send_keys(product_name)
            self.find_elements(user['zcp_search_btn'])[0].click()
            sleep(0.2)
            self.find_elements(user['zcp_product'])[0].click()
            self.win_handles('-1')
            min_purchase = self.element_text(user['zcp_min_purchase'])
            min_purchase = min_purchase[1:]
            if shop_num <= int(min_purchase):
                self.inputs_clear_text(user['zcp_buy_num'], 0, min_purchase)
            else:
                self.inputs_clear_text(user['zcp_buy_num'], 0, shop_num)
            if cart_type == 1:
                self.find_elements(user['zcp_product_cart'])[0].click()
                sleep(0.2)
                self.find_elements(user['加入货单_点击确定'])[0].click()
                sleep(10)
            else:
                product_price = self.element_text(user['zcp_product_price'])
                product_price = product_price[5:]
                self.find_element(user['zcp_product_purchase']).click()
                sleep(0.5)
                if sign_type == 1:
                    self.is_click(user['personal_signing'])
                    self.is_click(user['personal_signing_alert'])
                    log.info('进行 个人签署')
                try:
                    if self.order_amount_judgment(1, product_price):
                        self.script('10000')
                        self.place_order_submit(serve)
                        sleep()
                        signature_detail = self.find_elements(user['user_order_list_status'])
                        signature = '不需要签署' in signature_detail[1].text
                        if signature:
                            self.product_order_pay(serve, signature)
                            self.seller_order_deliver(serve, signature, seller_phone, address, place_order_num)
                            self.product_order_receipt(serve)
                        else:
                            self.seller_product_order(serve, seller_phone, place_order_num)
                            self.product_order_pay(serve, signature)
                            self.seller_order_deliver(serve, signature, seller_phone, address, place_order_num)
                            self.product_order_receipt(serve)
                except:
                    self.fial_info()
            log.info('当前下单次数 : ' + str(place_order_num) + '  预计下单次数  : ' + str(limit))
            place_order_num += 1

    def product_order_pay(self, serve, signature):
        if not signature:
            if serve == '24':
                self.driver.get(user_url['24_order_url'])
            else:
                self.driver.get(user_url['20_order_url'])
            sleep()
            self.find_elements(user['user_order_list_btn'])[0].click()
            sleep(0.2)
            self.find_elements(user['买家弹窗_确定'])[1].click()
            self.signing_contract()
        self.find_elements(user['user_order_list_btn'])[0].click()
        sleep()
        self.input_clear_text(user['user_pay_text'], '666666')
        self.find_element(user['user_pay_btn']).click()
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
        self.find_elements(user['user_order_list_btn'])[0].click()
        sleep(0.2)
        self.find_elements(user['买家弹窗_确定'])[1].click()
        sleep(1)
        signature_detail = self.find_elements(user['user_order_list_status'])
        sleep(0.2)
        signature = '完成' in signature_detail[1].text
        if not signature:
            self.fial_info()
        log.info('买家制成品订单收货成功')

    def seller_product_order(self, serve, seller_phone, place_order_num):
        if place_order_num == 0:
            self.seller_phone_login(serve, seller_phone)
            self.seller_skip_goods('order_contract', 'order_list')
        else:
            if serve == '24':
                self.driver.get(seller_url['24_order_list'])
            else:
                self.driver.get(seller_url['20_order_list'])
        self.find_elements(user['seller_order_list_btn'])[0].click()
        sleep()
        self.find_elements(user['seller_order_detail_btn'])[1].click()
        sleep(0.5)
        self.find_elements(user['seller_order_detail_btn'])[3].click()
        self.signing_contract()
        sleep()

    def seller_order_deliver(self, serve, signature, seller_phone, address, place_order_num):
        if not signature:
            if serve == '24':
                self.driver.get(seller_url['24_order_list'])
            else:
                self.driver.get(seller_url['20_order_list'])
        else:
            if place_order_num == 0:
                self.seller_phone_login(serve, seller_phone)
            self.seller_skip_goods('seller_order_contract', 'seller_order_list')
        self.find_elements(user['seller_order_list_btn'])[0].click()
        sleep(0.2)
        self.script('8000')
        self.find_elements(user['seller_order_deliver_place'])[0].click()
        sleep(0.2)
        self.click_area()
        sleep(0.2)
        self.input_clear_text(user['seller_order_address'], address)
        self.find_element(user['seller_order_deliver']).click()
        sleep(1)
        try:
            if serve == '24':
                assert self.return_current_url() == seller_url['24_order_list']
            else:
                assert self.return_current_url() == seller_url['20_order_list']
            log.info('卖家制成品发货成功')
            sleep(1)
        except AssertionError:
            self.fial_info()

    def seller_skip_goods(self, menu, submenu):
        self.is_click(user[menu])
        self.is_click(user[submenu])
        sleep(0.1)

    def order_amount_judgment(self, code, price):
        flag = 'true'
        if code == 1:
            product_detail = self.find_elements(user['order_info'])
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
            raw_detail = self.find_elements(user['order_info'])
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
        while not self.find_element(user['place_order_btn']).is_enabled():
            sleep(3)
            if self.find_element(user['place_order_btn']).is_enabled():
                self.find_element(user['place_order_btn']).click()
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
