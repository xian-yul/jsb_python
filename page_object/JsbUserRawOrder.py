#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from decimal import Decimal

from selenium.webdriver.common import keys

from common.readelement import Element
from page.webpage import WebPage
from utils.log import Log
from utils.times import sleep

user = Element('JsbUserOrder')
log = Log()
user_url = {'24_home': 'http://192.168.101.24:8090/shop/home', '20_home': 'https://demo.jinsubao.cn/',
            '24_order_url': 'http://192.168.101.24:8090/user-center/purchase-order',
            '20_order_url': 'https://demo.jinsubao.cn/user-center/purchase-order',
            '24_order_detail': 'http://192.168.101.24:8090/user-center/purchase-order-detail/',
            '20_order_detail': 'https://demo.jinsubao.cn/user-center/purchase-order-detail/'}
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


class JsbUserRawOrder(WebPage):
    def user_login(self, serve, phone):
        if serve == '24':
            self.driver.get(user_url['24_home'])
        else:
            self.driver.get(user_url['20_home'])
        self.click_user_login(phone)

    def click_login_exit(self):
        self.is_click(user['买家退出登录按钮'])
        log.info('退出登录成功')

    def delivery_method(self, pickup_type, shop_num):
        min_purchase = self.element_text(user['market_min_purchase'])
        min_purchase = min_purchase[6:]
        if shop_num < int(min_purchase):
            self.inputs_clear_text(user['market_num'], 0, min_purchase)
        else:
            self.inputs_clear_text(user['market_num'], 0, shop_num)
        raw_price = 0
        if pickup_type == 2:
            self.find_elements(user['delivery_method'])[1].click()
            self.find_elements(user['delivery_type'])[0].click()
            raw_price = self.element_text(user['market_unit_price'])
            raw_price = raw_price[5:]
            self.is_click(user['purchase_btn'])
            log.info('进行配送方式_款到发货')
        elif pickup_type == 3:
            self.find_elements(user['delivery_method'])[1].click()
            self.find_elements(user['delivery_type'])[1].click()
            raw_price = self.element_text(user['market_unit_price'])
            raw_price = raw_price[5:]
            self.is_click(user['purchase_btn'])
            log.info('进行配送方式_定金+货到付款')
        elif pickup_type == 1:
            self.find_elements(user['delivery_method'])[0].click()
            raw_price = self.element_text(user['market_unit_price'])
            raw_price = raw_price[5:]
            self.is_click(user['purchase_btn'])
            log.info('进行自提方式_款到发货')
        return raw_price

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
            if price.find('不'):
                price = price[:-3]
            else:
                price = price[:-2]
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
        if self.find_element(user['place_order_btn']).is_enabled():
            self.is_click(user['place_order_btn'])
        else:
            while not self.find_element(user['place_order_btn']).is_enabled():
                sleep(3)
                if self.find_element(user['place_order_btn']).is_enabled():
                    self.is_click(user['place_order_btn'])
                    break
        sleep(3)
        try:
            if serve == '24':
                assert self.return_current_url() == user_url['24_order_url']
            else:
                assert self.return_current_url() == user_url['20_order_url']
            log.info('订单提交成功')
        except AssertionError:
            self.fial_info()

    def shipping_address(self, address_name):
        if address_name != '':
            self.is_click(user['显示更多地址'])
            loc = "xpath==//*[contains(text()," + address_name + ")]"
            self.is_click(loc)
            log.info('选择地址： ' + address_name)

    def sign_method(self, sign_type):
        if sign_type == 1:
            self.is_click(user['personal_signing'])
            self.is_click(user['personal_signing_alert'])
            log.info('进行 个人签署')

    def billing_judgment(self, billing_type):
        if billing_type == 1:
            self.is_click(user['order_invoicing'])
            log.info('选择订单开票')

    def buyers_and_sellers_sign(self, serve, seller_phone, place_order_num, seller_address, pickup_type,
                                multiple_type, deposit):
        log.info('进行买卖家签署支付发货收货')
        try:
            self.seller_goods_sign(serve, seller_phone, place_order_num, pickup_type, deposit)
            sleep(0.2)
            self.user_goods_sign_pay(serve, pickup_type, multiple_type)
            # sleep(0.2)
            # self.seller_goods_deliver(serve, seller_address, pickup_type, multiple_type)
            # sleep(0.2)
            # self.user_goods_receipt(serve, pickup_type, multiple_type)
        except:
            self.fial_info()

    def seller_goods_deliver(self, serve, seller_address, pickup_type, multiple_type):
        log.info('------------------------------------------------')
        log.info('进入卖家发货')
        if serve == '24':
            self.driver.get(seller_url['24_order_list'])
        else:
            self.driver.get(seller_url['20_order_list'])
        # if pickup_type == 3 and multiple_type != 0:
        #     self.seller_disposable(serve, pickup_type, seller_address)
        if multiple_type == 1:
            self.seller_disposable(serve, pickup_type, seller_address)
        elif multiple_type == 0:
            log.info('进行一单多发')
            self.seller_multiple_order(serve, seller_address, pickup_type)

    def seller_skip_goods(self, menu, submenu):
        self.is_click(user[menu])
        self.is_click(user[submenu])
        log.info('进入卖家   ____' + menu + "________子菜单_____" + submenu)
        sleep(0.1)

    def seller_goods_sign(self, serve, seller_phone, place_order_num, pickup_type, deposit):
        log.info('------------------------------------------------')
        log.info('进入卖家生成签署合同')
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
        if pickup_type == 3:
            self.input_clear_text(user['seller_deposit'], deposit)
            sleep(0.2)
        self.find_elements(user['seller_order_detail_btn'])[1].click()
        sleep(0.5)
        self.find_elements(user['seller_order_detail_btn'])[3].click()
        sleep(0.2)
        self.signing_contract()

    def user_goods_receipt(self, serve, pickup_type, multiple_type):
        log.info('------------------------------------------------')
        log.info('进入买家收货')
        if serve == '24':
            self.driver.get(user_url['24_order_url'])
        else:
            self.driver.get(user_url['20_order_url'])
        sleep(0.5)

        if multiple_type == 1 and pickup_type == 2:
            self.user_receipt()
        elif multiple_type == 1 and pickup_type == 1:
            self.user_receipt()
        elif multiple_type == 1 and pickup_type == 3:
            log.info('进行定金订单支付尾款')
            self.find_elements(user['user_order_list_btn'])[0].click()
            self.input_clear_text(user['user_pay_text'], '666666')
            sleep(0.2)
            self.find_element(user['user_pay_btn']).click()
            sleep()
            if serve == '24':
                self.driver.get(user_url['24_order_url'])
            else:
                self.driver.get(user_url['20_order_url'])
            sleep(0.5)
            self.user_receipt()
        else:
            log.info('进行多订单收货')
            self.user_over_charge(pickup_type)

    def user_goods_sign_pay(self, serve, pickup_type, multiple_type):
        log.info('------------------------------------------------')
        log.info('进入买家签署合同并支付')
        if serve == '24':
            self.driver.get(user_url['24_order_url'])
        else:
            self.driver.get(user_url['20_order_url'])
        log.info('进行买家合同签署')
        sleep()
        self.find_elements(user['user_order_list_btn'])[0].click()
        sleep(0.2)
        self.find_elements(user['买家弹窗_确定'])[1].click()
        self.signing_contract()
        self.find_elements(user['user_order_list_btn'])[0].click()
        sleep()
        if pickup_type == 3:
            log.info('进行买家定金订单支付')
            self.input_clear_text(user['user_pay_text'], '666666')
            sleep(0.2)
            self.find_element(user['user_pay_btn']).click()
            sleep(3)
            try:
                if serve == '24':
                    assert set(user_url['24_order_detail']).issubset(set(self.return_current_url()))
                else:
                    assert set(user_url['20_order_detail']).issubset(set(self.return_current_url()))
                log.info('定金支付成功')
            except AssertionError:
                self.fial_info()
        else:
            log.info('进行买家订单支付')
            self.input_clear_text(user['user_pay_text'], '666666')
            flag = self.getElementExistance(user['user_advance_pay'])
            if flag:
                self.find_elements(user['user_advance_pay'])[1].click()
                self.find_elements(user['user_advance_pay'])[2].click()
            self.find_element(user['user_pay_btn']).click()
            sleep(3)
            try:
                if serve == '24':
                    assert set(user_url['24_order_detail']).issubset(set(self.return_current_url()))
                else:
                    assert set(user_url['20_order_detail']).issubset(set(self.return_current_url()))
                    log.info('原料订单支付成功')
            except AssertionError:
                self.fial_info()
        if pickup_type == 1 or pickup_type == 2:
            if serve == '24':
                self.driver.get(user_url['24_order_url'])
            else:
                self.driver.get(user_url['20_order_url'])
        if pickup_type == 1:
            log.info('进行自提信息填写')
            if multiple_type == 0:
                log.info('进入一单多提')
                self.user_more_mention(serve)
            else:
                log.info('进入一次性提货')
                self.find_elements(user['user_order_list_btn'])[0].click()
                sleep(0.5)
                self.input_clear_text(user['self_lifting_driverName'], '司机名称123')
                self.input_clear_text(user['self_lifting_driverIdNumber'], '220422199312260410')
                self.input_clear_text(user['self_lifting_phone'], '18965699791')
                self.input_clear_text(user['self_lifting_licenseNumber'], '闽D16491')
                self.find_elements(user['self_lifting_time'])[1].click()
                self.is_click(user['self_lifting_time_determine'])
                sleep(0.2)
                self.find_elements(user['self_lifting_entrust'])[1].click()
                self.pickup_signing_contract()

    def place_raw_order(self, serve, user_phone, org_name, pickup_type, shop_num, address_name,
                        sign_type, billing_type, seller_phone, limit, seller_address, multiple_type, deposit
                        ):
        self.click_user_login(serve, user_phone)
        place_order_num = 0
        while place_order_num < limit:
            sleep(0.3)
            if place_order_num > 0:
                self.find_elements(user['navigation_bar'])[1].click()
            else:
                self.find_elements(user['navigation_bar'])[0].click()
            self.script('3000')
            self.inputs_clear_text(user['market_search_text'], 1, org_name)
            self.is_click(user['market_search_btn'])
            self.is_click(user['market_goods'])
            self.win_handles('-1')
            sleep(0.5)
            raw_price = self.delivery_method(pickup_type, shop_num)
            flag = self.order_amount_judgment(2, raw_price)
            try:
                if flag == 'true':
                    if pickup_type == 2 and pickup_type == 3:
                        self.shipping_address(address_name)
                    self.script('10000')
                    sleep(0.2)
                    self.sign_method(sign_type)
                    sleep(0.2)
                    self.billing_judgment(billing_type)
                    self.place_order_submit(serve)
                    sleep(0.2)
                    if serve == '24':
                        assert self.driver.current_url == user_url['24_order_url']
                    else:
                        assert self.driver.current_url == user_url['20_order_url']
                    log.info('下单完毕')
                    self.buyers_and_sellers_sign(serve, seller_phone, place_order_num, seller_address, pickup_type,
                                                 multiple_type, deposit)
                    place_order_num += 1
                    log.info('当前下单次数 : ' + str(place_order_num) + '  预计下单次数: ' + str(limit))
                else:
                    log.info("下单判断出现异常")
                    self.base_get_img()
            except AssertionError:
                self.fial_info()

    def seller_multiple_order(self, serve, seller_address, pickup_type):
        log.info('进入卖家一单多发')
        multiple_num = 1
        num = 0
        sleep(0.2)
        if serve == '24':
            self.driver.get(seller_url['24_order_list'])
        else:
            self.driver.get(seller_url['20_order_list'])
        if pickup_type == 2 or pickup_type == 3:
            while multiple_num <= 9:
                self.find_elements(user['seller_order_list_btn'])[0].click()
                if multiple_num == 1:
                    self.find_elements(user['deliver_mention'])[1].click()
                else:
                    self.is_click(user['add_deliver'])
                self.script('800')
                sleep(0.5)
                self.find_elements(user['seller_order_deliver_place'])[0].click()
                sleep(0.2)
                self.click_area()
                sleep(0.2)
                self.input_clear_text(user['seller_order_address'], seller_address)
                if multiple_num == 1:
                    num = self.element_text(user['surplus_num'])
                    num = num[7:]
                    num = num[:-1]
                    num = float(num) / 10
                    num = round(num, 3)
                # if multiple_num != 9:
                self.input_clear_text(user['num'], num)
                if multiple_num == 9:
                    num = self.element_text(user['surplus_num'])
                    num = num[7:]
                    num = num[:-1]
                    self.input_clear_text(user['num'], num)
                sleep(0.2)
                if multiple_num == 1:
                    self.find_elements(user['seller_order_deliver'])[1].click()
                else:
                    self.is_click(user['seller_order_deliver'])
                self.signing_contract()
                try:
                    if serve == '24':
                        assert self.driver.current_url == seller_url['24_order_list']
                    else:
                        assert self.driver.current_url == seller_url['20_order_list']
                except:
                    self.fial_info()
                log.info("当前发货单数为:" + str(multiple_num) + "    当前发货数量为:" + str(num))
                multiple_num += 1
        elif pickup_type == 1:
            while multiple_num <= 9:
                self.find_elements(user['seller_order_list_btn'])[0].click()
                sleep(0.2)
                self.find_elements(user['seller_order_deliver'])[1].click()
                self.signing_contract()
                log.info('当前交货单数为:' + str(multiple_num))
                if multiple_num != 9:
                    multiple_num += 1
                else:
                    break
            log.info('交货完毕  已交货单数:' + str(multiple_num))

    def user_more_mention(self, serve):
        log.info('进入买家一单多提')
        more_num = 1
        pickup_num = '0.111'
        if serve == '24':
            self.driver.get(user_url['24_order_url'])
        else:
            self.driver.get(user_url['20_order_url'])
        while more_num <= 9:
            self.find_elements(user['user_order_list_btn'])[0].click()
            if more_num == 1:
                self.is_click(user['more_mention'])
                pickup_num = self.find_elements(user['self_lifting_num'])[7].text
                pickup_num = pickup_num[14:]
                pickup_num = pickup_num[:-1]
                pickup_num = float(pickup_num) / 9
                pickup_num = round(pickup_num, 3)
            else:
                self.find_elements(user['add_delivery_single'])[-1].click()
            sleep(0.2)
            self.self_lifting(1, pickup_num, more_num)
            log.info('当前新增提货单: ' + str(more_num))
            if more_num != 9:
                more_num += 1
            else:
                break
        log.info('新增提货单完毕 已新增:' + str(more_num))

    def self_lifting(self, more, pickup_num, more_num):
        if more != 1:
            self.find_elements(user['user_order_list_btn'])[0].click()
        sleep(0.5)
        self.inputs_clear_text(user['self_lifting_driverName'], -1, '司机名称123')
        self.inputs_clear_text(user['self_lifting_driverIdNumber'], -1, '220422199312260410')
        self.inputs_clear_text(user['self_lifting_phone'], -1, '18965699791')
        self.inputs_clear_text(user['self_lifting_licenseNumber'], -1, '闽D16491')
        self.find_elements(user['self_lifting_time'])[1].click()
        sleep(0.2)
        self.is_click(user['self_lifting_time_determine'])
        if more_num != 9:
            self.inputs_clear_text(user['num'], -1, pickup_num)
        else:
            pickup_num = self.find_elements(user['self_lifting_num'])[7].text
            pickup_num = pickup_num[14:]
            pickup_num = pickup_num[:-1]
            self.inputs_clear_text(user['num'], -1, pickup_num)
        sleep(0.2)
        self.find_elements(user['self_lifting_entrust'])[1].click()
        self.pickup_signing_contract()

    def ces(self, serve, seller_phone, seller_address, user_phone):
        self.user_login(serve, user_phone)
        if serve == '24':
            self.driver.get(user_url['24_order_url'])
        else:
            self.driver.get(user_url['20_order_url'])
        self.find_elements(user['see_look'])[0].click()

    def user_over_charge(self, pickup_type):
        charge_num = 1
        log.info('进入买家多发收货')
        self.find_elements(user['user_order_list_btn'])[0].click()
        sleep(0.2)
        if pickup_type == 2:
            while charge_num <= 9:
                if charge_num != 1:
                    self.find_elements(user['multiple_order_single'])[charge_num - 1].click()
                self.script('10000')
                lis = self.find_elements(user['user_detail_receipt'])
                if len(lis) == 4:
                    self.find_elements(user['user_detail_receipt'])[3].click()
                else:
                    self.find_elements(user['user_detail_receipt'])[2].click()
                self.signing_contract()
                self.script('0')
                sleep(0.2)
                log.info('当前收货单数:' + str(charge_num))
                charge_num += 1
            order_status = self.find_elements(user['order_status'])[1]
            status = '完成' in order_status.text
            if not status:
                self.fial_info()
            else:
                log.info('买家多发订单收货完毕  订单已完成')
            log.info('买家多发收货结束')
        elif pickup_type == 1:
            while charge_num <= 9:
                if charge_num != 1:
                    self.find_elements(user['multiple_order_single'])[charge_num - 1].click()
                self.script('10000')
                lis = self.find_elements(user['user_detail_receipt'])
                if len(lis) == 5:
                    self.find_elements(user['user_detail_receipt'])[4].click()
                else:
                    self.find_elements(user['user_detail_receipt'])[5].click()
                self.signing_contract()
                self.script('0')
                sleep(0.2)
                log.info('当前收货单数:' + str(charge_num))
                charge_num += 1
            order_status = self.find_elements(user['order_status'])[1]
            status = '完成' in order_status.text
            if not status:
                self.fial_info()
            else:
                log.info('买家多提订单收货完毕  订单已完成')
            log.info('买家多提收货结束')

    def seller_disposable(self, serve, pickup_type, seller_address):
        log.info('进行一次性发货')
        self.find_elements(user['seller_order_list_btn'])[0].click()
        sleep()
        self.script('500')
        if pickup_type == 1:
            self.find_elements(user['seller_order_deliver'])[1].click()
        else:
            self.find_elements(user['seller_order_deliver_place'])[0].click()
            sleep(0.2)
            self.click_area()
            sleep(0.2)
            self.input_clear_text(user['seller_order_address'], seller_address)
            if pickup_type == 2 or pickup_type == 3:
                self.find_elements(user['seller_order_deliver'])[1].click()
            else:
                self.is_click(user['seller_order_deliver'])
        self.signing_contract()
        try:
            if serve == '24':
                assert self.return_current_url() == seller_url['24_order_list']
            else:
                assert self.return_current_url() == seller_url['20_order_list']
            log.info('卖家发货成功')
            sleep(1)
        except AssertionError:
            self.fial_info()

    def user_receipt(self):
        self.find_elements(user['user_order_list_btn'])[0].click()
        self.signing_contract()
        sleep(1)
        signature_detail = self.find_elements(user['user_order_list_status'])
        signature = '完成' in signature_detail[1].text
        if not signature:
            self.fial_info()
        log.info('买家原料订单收货成功')
