from decimal import Decimal
from selenium.webdriver.common.by import By

import page_object.JsbSellerPage
from common.readelement import Element
from page.webpage import WebPage, sleep
from utils import tool_util
from utils.log import Log

user = Element('JsbUserProductOrder')
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


class JsbSellerRawAdd(WebPage):
    def seller_backstage_title(self):
        title = self.element_text(user['卖家登录标题'])
        try:
            assert title == '金塑宝 商家管理后台'
            log.info('当前界面标题是否正常 断言判断一致')
        except AssertionError:
            self.fial_info()

    def seller_phone_login(self, serve, seller_phone):
        if serve == '24':
            self.driver.get(seller_url['24'])
        else:
            self.driver.get(seller_url['20'])
        self.seller_backstage_title()
        sleep(0.2)
        self.input_clear_text(user['卖家登录手机号'], seller_phone)
        self.is_click(user['卖家验证码按钮'])
        self.input_clear_text(user['卖家验证码文本框'], 666666)
        self.is_click(user['卖家登录按钮'])
        sleep()
        try:
            if serve == '24':
                assert self.return_current_url() == seller_url['24_登录后']
            else:
                assert self.return_current_url() == seller_url['20_登录后']
            log.info("卖家登录信息:   _____" + self.element_text(user['卖家登录信息']))
        except AssertionError:
            self.fial_info()
