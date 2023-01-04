#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import string

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from common.readelement import Element
from page.webpage import WebPage
from utils.log import Log
from utils.times import sleep

seller = Element('seller')
user_url = {'24': 'http://192.168.101.24:8090/shop/home', '20': 'https://demo.jinsubao.cn/'}
seller_url = {'24': 'http://192.168.101.24:8070/user/login', '20': 'https://slrdm.jinsubao.cn/',
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
coupon_url = {1: '全部用户卷', 2: '新用户卷', 3: '关注用户卷', 4: '老用户卷', 5: '全部商品', 6: '指定商品', 7: '满减卷',
              8: '吨减卷', 9: '点击店铺优惠劵',
              10: '点击企业优惠劵'}
log = Log()


class JsbSeller(WebPage):

    def seller_coupon_skip(self, coupon_type):
        self.is_click(seller['营销管理'])
        sleep(0.1)
        self.is_click(seller['优惠劵'])
        self.is_click(seller[coupon_url[coupon_type]])
        log.info('进入营销管理优惠劵')

    def seller_coupon_detail(self, coupon_name, suit_type, target_range_type, content, quota):
        log.info('进入填写优惠劵信息')
        self.input_text(seller['优惠劵标题'], coupon_name)
        if suit_type == 1:
            self.is_click(seller['点击指定商品'])
            self.is_click(seller['点击添加指定商品'])
            self.is_click(seller['指定商品勾选全部'])
            self.is_click(seller['指定商品点击确定'])
            self.script('2000')
        self.is_click(seller[coupon_url[target_range_type]])
        num = self.find_element(seller['发放数量'])
        self.input_clear_text(seller['金额卷元'], 1)
        self.input_clear_text(seller['发放数量'], 10)
        log.info(num.get_attribute())
        self.input_text(seller['金额卷满元'], 10)
        self.is_click(seller['领取后生效'])
        self.input_clear_text(seller['有效天数'], 1)
        self.input_text(seller['使用说明'], content)
        log.info('进入优惠劵信息填写完毕')
        self.script('2000')
        self.is_click(seller['优惠劵点击提交'])

    def seller_storehouse_detail(self, storehouse_name, storehouse_address, storehouse_contact,
                                 storehouse_phone, default):
        old_add_storehouse = self.find_elements(seller['新增增加判断'])
        log.info(len(old_add_storehouse))
        log.info('仓库信息填写')
        self.is_click(seller['仓库新增自提点'])
        self.input_text(seller['仓库名称'], storehouse_name)
        self.is_click(seller['仓库省市区'])
        self.click_area()
        self.input_text(seller['仓库详细地址'], storehouse_address)
        self.input_text(seller['仓库联系人'], storehouse_contact)
        self.input_text(seller['仓库联系方式'], storehouse_phone)
        if default == 1:
            self.is_click(seller['设置仓库默认地址'])
        self.is_click(seller['仓库点击确定'])
        log.info('仓库信息填写完毕')
        self.refresh()
        try:
            new_add_storehouse = self.find_elements(seller['新增增加判断'])
            log.info(len(new_add_storehouse))
            assert len(new_add_storehouse) > len(old_add_storehouse)
            log.info('新增仓库地址成功')
        except AssertionError:
            log.info('新增仓库地址失败')
            self.fial_info()

    def seller_supply_market(self, title, content, video_path, img_path):
        log.info('选择发布 市场信息 供需资讯')
        self.is_click(seller['选择市场信息'])
        self.is_click(seller['勾选供需发布协议'])
        self.is_click(seller['点击确定进行发布'])
        self.input_text(seller['供需标题'], title + "_市场信息")
        self.input_text(seller['供需内容简要'], content)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="rawDemAndImgList"]/div[2]/div[2]/div/span/div/div[1]/span/div[2]/span/input').send_keys(
            img_path)
        self.script('2000')
        sleep()
        # self.is_click(seller['市场信息智能搜索'])
        # self.is_click(seller['市场信息牌号选择'])
        # self.input_clear_text(seller['市场信息单吨价格增加'], 1)
        # self.input_clear_text(seller['市场信息发布数量增加'], 1)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="rawDemAndImgList"]/div[1]/div[2]/div/span/div/span/div[2]/span/input').send_keys(
            video_path)
        self.is_click(seller['供需交货范围'])
        self.click_area()
        self.is_click(seller['市场信息提交'])

    def seller_supply_purchase(self, title, content, video_path, img_path):
        log.info('选择发布 采购需求 供需资讯')
        self.is_click(seller['勾选供需发布协议'])
        self.is_click(seller['点击确定进行发布'])
        self.input_text(seller['供需标题'], title + "_采购需求")
        self.input_text(seller['供需内容简要'], content)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="rawDemAndImgList"]/div[2]/div[2]/div/span/div/div[1]/span/div[2]/span/input').send_keys(
            img_path)
        self.script('2000')
        # self.input_clear_text(seller['采购需求卖主数量增加'], 1)
        # self.input_clear_text(seller['采购需求单吨价格增加'], 1)
        # self.input_clear_text(seller['采购需求订购数量增加'], 1)
        # self.driver.find_element(By.XPATH,
        #                          '//*[@id="rawDemAndImgList"]/div[1]/div[2]/div/span/div/span/div[2]/span/input').send_keys(
        #     video_path)
        self.is_click(seller['供需交货范围'])
        self.click_area()
        self.is_click(seller['采购需求智能搜索'])
        sleep(0.2)
        self.is_click(seller['采购需求牌号选择'])
        sleep(0.5)
        self.is_click(seller['采购需求提交'])

    def seller_supply_submit(self):
        try:
            assert self.return_current_url() == seller_url['供需列表']
            log.info('新增供需成功')
        except AssertionError:
            log.info('新增供需失败')
            self.fial_info()

    def seller_coupon_submit(self, serve):
        try:
            sleep(0.5)
            if serve == '24':
                assert self.return_current_url() == coupon_url['24_coupon_list']
            else:
                assert self.return_current_url() == coupon_url['20_coupon_list']
            log.info('添加优惠劵成功')
        except AssertionError:
            log.info('优惠劵添加失败 ')
            self.fial_info()

    def seller_supply_demand(self, serve, seller_phone, supply_type, limit, title, content, video_path, img_path):
        self.seller_phone_login(serve, seller_phone)
        self.seller_skip_goods('点击产品管理', '供需管理')
        add_num = 0
        while add_num < limit:
            self.is_click(seller['供需点击发布'])
            if supply_type == 1:
                self.seller_supply_market(title, content, video_path, img_path)
            else:
                self.seller_supply_purchase(title, content, video_path, img_path)
            self.seller_supply_submit()
            add_num += 1
            log.info('当前添加次数 : ' + str(add_num) + '  预计添加次数  : ' + str(limit))
