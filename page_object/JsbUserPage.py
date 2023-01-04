#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from decimal import Decimal

from selenium.webdriver.common.by import By

from common.readelement import Element
from page.webpage import WebPage
from utils import tool_util
from utils.log import Log
from utils.times import sleep

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


class JsbUserPage(WebPage):

    def click_login_exit(self):
        self.is_click(user['退出登录按钮'])
        # self.find_element(user['登录'])
        log.info('退出登录成功')

    def user_login_exit(self, phone):
        self.click_user_login(phone)
        self.click_login_exit()

    def user_register(self, serve, limit):
        if serve == '24':
            self.driver.get(user_url['24_home'])
        else:
            self.driver.get(user_url['20_home'])
        sleep(0.2)
        register_num = 0
        while register_num < limit:
            sleep(0.2)
            phone = '189' + tool_util.random_number(8)
            name = "签章认证___" + tool_util.gbk2312_name() + tool_util.unicode_name()
            self.is_click(user['注册按钮'])
            self.win_handles('-1')
            log.info('进入注册界面')
            self.input_text(user['注册手机号'], phone)
            log.info('输入手机号 :' + phone)
            self.input_text(user['注册昵称'], name)
            log.info('输入注册昵称 :' + name)
            self.is_click(user['注册验证码按钮'])
            self.is_click(user['注册协议勾选'])
            self.is_click(user['注册提交按钮'])
            self.win_handles('-1')
            sleep()
            try:
                if serve == '24':
                    assert self.return_current_url() == user_url['24注册后']
                else:
                    assert self.return_current_url() == user_url['20注册后']
                log.info('注册成功')
                self.refresh()
                self.click_login_exit()
                register_num += 1
                log.info('当前添加次数 : ' + str(register_num) + '  预计添加次数  : ' + str(limit))
            except:
                self.fial_info()

    def user_address_add(self, serve, user_phone, recipient_name, address_name, contact_phone, post_code,
                         fixed_telephone, default_type,
                         limit):
        self.driver.get(user_url[serve])
        self.click_user_login(serve, user_phone)
        self.user_menu_skip('地址管理')
        address_num = 0
        while address_num < limit:
            sleep()
            self.user_address_detail(recipient_name, address_name, contact_phone, post_code, fixed_telephone,
                                     default_type
                                     )
            address_num += 1
            log.info('当前添加次数 : ' + str(address_num) + '  预计添加次数  : ' + str(limit))

    def user_menu_skip(self, click_menu):
        self.is_click(user['用户中心点击'])
        self.is_click(user[user_menu[click_menu]])
        log.info('进入' + click_menu + '菜单')

    def user_address_detail(self, recipient_name, address_name, contact_phone, post_code, fixed_telephone, default_type
                            ):
        log.info('进行用户地址信息填写')
        self.is_click(user['新增地址按钮'])
        self.input_text(user['地址收件人'], recipient_name + tool_util.gbk2312_name())
        self.is_click(user['用户收货地点'])
        self.click_area()
        self.input_text(user['用户详细地址'], address_name)
        phone = '189' + tool_util.random_number(8)
        self.input_text(user['收货联系人'], phone)
        self.input_text(user['收货邮编'], post_code)
        self.input_text(user['收货固定电话'], fixed_telephone)
        if default_type == 1:
            self.is_click(user['设置默认地址'])
            log.info('已设置为默认地址')
        self.driver.find_element(By.XPATH,
                                 "// button[@class='ant-btn ant-btn-primary']").click()
        log.info('收货地址新增成功')

    def user_industry_iframe(self, iframe, detail):
        industry_iframe = self.find_element(iframe)
        self.driver.switch_to.frame(industry_iframe)
        log.info('定位进入iframe')
        sleep(0.5)
        self.input_text(user['产学融合详情'], detail)
        self.driver.switch_to.default_content()
        log.info('退出iframe')

    def user_industry_need(self, title, profiles, phone, detail, contacts):
        log.info('进行产学融合_需求列表添加')
        title = '产学融合_需求列表'
        self.is_click(user['用户中心需求列表点击'])
        self.is_click(user['用户中心添加产学'])
        try:
            assert self.return_current_url() == user_url['产学融合需求列表添加']
            self.input_text(user['产学融合标题'], title)
            self.input_text(user['产学融合内容概要'], profiles)
            self.user_industry_iframe(user['产学融合iframe'], detail)
            self.input_text(user['产学融合姓名'], contacts)
            self.input_text(user['产学融合联系方式'], phone)
            self.is_click(user['产学融合需求提交'])
            assert self.return_current_url() == user_url['产学融合需求列表']
            log.info('产学融合_需求列表添加成功')
        except:
            self.fial_info()

    def user_research_results(self, title, profiles, phone, detail, contacts, video_path, img_path, patent_number):
        log.info('进行产学融合_研究成果添加')
        title = '产学融合_研究成果'
        self.is_click(user['用户中心点击研究成果'])
        self.is_click(user['用户中心添加产学'])
        try:
            assert self.return_current_url() == user_url['产学融合研究成果添加']
            self.input_text(user['产学融合标题'], title)
            self.input_text(user['产学融合研究成果项目介绍'], profiles)
            self.user_industry_iframe(user['产学融合iframe'], detail)
            self.driver.find_element(By.XPATH,
                                     '//*[@id="iarResearchImgVos"]/div[1]/div[2]/div/span/div/span/div[2]/span/input').send_keys(
                video_path)
            self.driver.find_element(By.XPATH,
                                     '//*[@id="iarResearchImgVos"]/div[2]/div[2]/div/span/div/span/div[2]/span/input').send_keys(
                img_path)
            self.input_text(user['产学融合研究成果专利号'], patent_number)
            self.input_text(user['产学融合姓名'], contacts)
            self.input_text(user['产学融合联系方式'], phone)
            self.is_click(user['产学融合研究成果提交'])
            assert self.return_current_url() == user_url['产学融合研究成果列表']
            log.info('产学融合_研究成果添加成功')
        except:
            self.fial_info()

    def user_legal_service(self, title, profiles, phone, detail, contacts):
        log.info('进行产学融合_法律服务添加')
        title = '产学融合_法律服务'
        self.is_click(user['用户中心点击法律服务'])
        self.is_click(user['用户中心添加产学'])
        try:
            assert self.return_current_url() == user_url['产学融合法律服务添加']
            self.input_text(user['产学融合标题'], title)
            self.input_text(user['产学融合内容概要'], profiles)
            self.user_industry_iframe(user['产学融合iframe'], detail)
            self.is_click(user['产学融合法律服务点击地区'])
            self.click_area()
            self.input_text(user['产学融合姓名'], contacts)
            self.input_text(user['产学融合联系方式'], phone)
            self.is_click(user['产学融合法律服务提交'])
            assert self.return_current_url() == user_url['产学融合法律服务列表']
            log.info('产学融合_法律服务添加成功')
        except:
            self.fial_info()

    def user_industry_academia(self, serve, user_phone, industry_type, title, profiles, phone, detail, contacts,
                               img_path, video_path, patent_number, limit):
        self.click_user_login(serve, user_phone)
        self.user_menu_skip('产学融合')
        add_num = 0
        while add_num < limit:
            if industry_type == 1:
                self.user_industry_need(title, profiles, phone, detail, contacts)
            elif industry_type == 2:
                self.user_research_results(title, profiles, phone, detail, contacts, video_path, img_path,
                                           patent_number)
            elif industry_type == 3:
                self.user_legal_service(title, profiles, phone, detail, contacts)
            add_num += 1
            log.info('当前添加次数 : ' + str(add_num) + '  预计添加次数  : ' + str(limit))

    def user_supply_skip(self, serve, user_phone):
        log.info('登录并进入用户中心 _ 供需资讯 点击发布')
        self.click_user_login(serve, user_phone)
        self.user_menu_skip('供需资讯')
        self.is_click(user['点击资讯首页'])

    def user_supply_publish(self, publish_type):
        log.info('供需发布选择')
        self.is_click(user['资讯点击发布'])
        if publish_type == 1:
            self.is_click(user['资讯点击市场信息'])
        self.is_click(user['资讯勾选规则'])
        self.is_click(user['资讯选择点击确定'])

    def user_procurement(self, title, content, img_path, seller_num, price, order_num, video_path):
        try:
            assert self.return_current_url() == user_url['采购需求发布url']
        except:
            self.fial_info()
        log.info('采购需求信息填写')
        self.input_text(user['供需资讯标题'], title + '_采购需求')
        self.input_text(user['供需资讯内容概要'], content)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="rawDemAndImgList"]/div[2]/div[2]/div/span/div/div[1]/span/div[2]/span/input').send_keys(
            img_path)
        sleep(0.2)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="rawDemAndImgList"]/div[1]/div[2]/div/span/div/span/div[2]/span/input').send_keys(
            video_path)
        self.is_click(user['采购需求智能搜索'])
        self.is_click(user['供需资讯选择原料'])
        self.script('2000')
        self.input_clear_text(user['供需咨询卖家数量'], seller_num)
        self.is_click(user['供需资讯交货范围'])
        self.click_area()
        self.input_clear_text(user['供需资讯单吨价格'], price)
        self.input_clear_text(user['供需资讯订购数量'], order_num)

        self.is_click(user['采购需求点击提交'])
        try:
            assert self.return_current_url() == user_url['供需资讯列表url']
        except:
            self.fial_info()
        log.info('采购需求信息填写完毕')

    def user_market(self, title, content, img_path, order_num, price, video_path):
        try:
            assert self.return_current_url() == user_url['市场信息发布url']
        except:
            self.fial_info()
        log.info('市场信息填写')
        self.input_text(user['供需资讯标题'], title + '_市场信息')
        self.input_text(user['供需资讯内容概要'], content)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="rawDemAndImgList"]/div[2]/div[2]/div/span/div/div[1]/span/div[2]/span/input').send_keys(
            img_path)
        sleep(0.2)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="rawDemAndImgList"]/div[1]/div[2]/div/span/div/span/div[2]/span/input').send_keys(
            video_path)
        self.is_click(user['市场信息智能搜索'])
        self.is_click(user['供需资讯选择原料'])
        self.script('2000')
        self.is_click(user['供需资讯交货范围'])
        self.click_area()
        self.input_clear_text(user['供需资讯订购数量'], order_num)
        self.input_clear_text(user['供需资讯单吨价格'], price)

        self.is_click(user['市场信息点击提交'])
        try:
            assert self.return_current_url() == user_url['供需资讯列表url']
        except:
            self.fial_info()
        log.info('市场信息填写完毕')

    def user_supply_demand(self, serve, user_phone, publish_type, title, content, img_path, seller_num, price,
                           order_num, limit, video_path):
        self.user_supply_skip(serve, user_phone)
        add_num = 0
        while add_num < limit:
            self.user_supply_publish(publish_type)
            if publish_type == 1:
                self.user_market(title, content, img_path, order_num, price, video_path)
            else:
                self.user_procurement(title, content, img_path, seller_num, price, order_num, video_path)
            self.refresh()
            add_num += 1
            log.info('当前添加次数 : ' + str(add_num) + '  预计添加次数  : ' + str(limit))
