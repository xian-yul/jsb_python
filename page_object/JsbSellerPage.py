#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import string

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

import page_object.JsbUserPage
from common.readelement import Element
from page.webpage import WebPage, sleep
from utils.log import Log
from utils.tool_util import goods_deliver_area

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
              'skip_分类': '产品分类', 'skip_订单': '订单合同', 'skip_产品': '产品列表', 'skip_供需': '供需管理',
              'skip_仓库': '仓库地址', '原料类型': '添加商品原料类型', '制成品类型': '添加商品制成品类型',
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


class JsbSellerPage(WebPage):

    def seller_backstage_title(self):
        title = self.element_text(seller['卖家登录标题'])
        assert title == '金塑宝 商家管理后台'
        log.info('当前界面标题是否正常 断言判断一致')

    def input_seller_phone(self, phone):
        self.input_text(seller['手机号'], phone)

    def click_phone_code(self):
        self.is_click(seller['手机号验证码'])

    def click_phone_login_btn(self):
        self.is_click(seller['手机号登录'])

    def toggle_phone_login(self):
        self.is_click(seller['卖家登录手机号切换'])

    def toggle_number_login(self):
        self.is_click(seller['卖家登录子账号切换'])

    def seller_number_username(self, number):
        self.input_text(seller['子账号账号'], number)

    def seller_number_password(self, password):
        self.input_text(seller['子账号密码'], password)

    def seller_number_login_btn(self):
        self.is_click(seller['子账号登陆'])

    def seller_popup_closes(self):
        self.is_click(seller['登录弹窗'])
        sleep(0.2)
        self.is_click(seller['登录弹窗'])
        sleep(0.5)

    def seller_goods_click_online(self, code):
        if code == 1:
            self.is_click(seller['原料点击上架'])
        else:
            self.is_click(seller['制成品点击上架'])
        self.driver.find_elements(By.XPATH,
                                  "// button[@class='ant-btn ant-btn-primary']")[2].click()
        log.info('商品点击上架')
        sleep(0.5)

    def seller_login_info(self):
        login_name = self.element_text(seller['登录后昵称'])
        login_identity = self.element_text(seller['登录后身份'])
        log.info('登录后的昵称 : ' + login_name + '  登录后的身份 : ' + login_identity)

    def seller_exit_login(self):
        try:
            exit_name = self.find_element(seller['登录文案'])
        except:
            log.info('登录文案已消失')
            self.is_click(seller['退出点击姓名'])
            sleep(0.2)
            self.is_click(seller['退出点击退出'])
            sleep(0.2)
            self.is_click(seller['退出确定'])
            sleep(0.2)
            self.seller_backstage_title()
            log.info('退出登录成功')

    def seller_phone_login(self, serve, phone):
        if serve == '24':
            self.driver.get(seller_url['24'])
        else:
            self.driver.get(seller_url['20'])
        self.seller_backstage_title()
        self.input_seller_phone(phone)
        log.info('输入手机号  : ' + phone)
        self.click_phone_code()
        log.info('点击验证码按钮')
        sleep(0.2)
        self.click_phone_login_btn()
        log.info('点击登录')
        sleep(0.2)
        self.seller_login_info()

    def seller_number_login(self, serve, number, password):
        if serve == '24':
            self.driver.get(seller_url['24'])
        else:
            self.driver.get(seller_url['20'])
        self.toggle_number_login()
        log.info('切换子账号登录')
        sleep(0.5)
        self.seller_number_username(number)
        log.info('输入账号  : ' + number)
        sleep(0.5)
        self.seller_number_password(password)
        sleep(0.5)
        log.info('输入密码  : ' + password)
        self.seller_number_login_btn()
        log.info('点击登录')
        self.seller_login_info()
        sleep()

    def seller_goods_sign(self, serve, seller_phone, limit):
        if limit > 1:
            if serve == '24':
                self.driver.get(seller_url['24'])
            else:
                self.driver.get(seller_url['20'])
        else:
            self.seller_phone_login(serve, seller_phone)
        self.is_click(seller['订单合同'])
        self.is_click(seller['卖家订单列表'])
        log.info('进入卖家订单进行签署合同')
        self.is_click(seller['卖家订单列表详情'])
        sleep(0.2)
        self.is_click(seller['点击生成合同'])
        self.is_click(seller['点击生成并签署'])
        self.signing_contract()

    def seller_goods_ship(self, serve):
        if serve == '24':
            self.driver.get(seller_url['24_order_list'])
        else:
            self.driver.get(seller_url['20_order_list'])
        log.info('进入卖家订单进行发货')
        self.is_click(seller['列表发货按钮'])
        self.script('5000')
        self.input_text(seller['发货详细地址'], 'selenium发货地址')
        self.is_click(seller['发货地点'])
        self.click_area()
        sleep(0.1)
        ship_btn = self.find_elements(seller['发货按钮'])
        ship_btn[0].click()
        self.signing_contract()
        log.info('卖家发货成功')

    def seller_skip_goods(self, skip_name):
        self.is_click(seller['点击产品管理'])
        self.is_click(seller[seller_url[skip_name]])
        log.info('进入卖家' + skip_name)
        sleep(0.1)

    def seller_goods_choose(self, goods_type):
        sleep(1)
        self.is_click(seller['点击添加商品'])
        sleep(1)
        self.is_click(seller[seller_url[goods_type]])
        log.info('选择商品添加类型 : ' + seller_url[goods_type])

    def seller_goods_grade(self, grade_number):
        sleep(0.5)
        self.is_click(seller['点击智能搜索'])
        try:
            grade = self.find_elements(seller['牌号css'])
            self.script_top(grade[59])
            sleep(2)
            # grade = self.find_elements(seller['牌号css'])
            # sleep(0.2)
            # self.script_top(grade[119])  # 拖动到可见的元素去
            # sleep(2)
            # grade = self.find_elements(seller['牌号css'])
            # self.script_top(grade[179])  # 拖动到可见的元素去
            # sleep(2)
            # grade = self.find_elements(seller['牌号css'])
            # self.script_top(grade[239])  # 拖动到可见的元素去
            # sleep(2)
            # grade = self.find_elements(seller['牌号css'])
            # self.script_top(grade[299])  # 拖动到可见的元素去
            # sleep(2)
            # grade = self.find_elements(seller['牌号css'])
            # self.script_top(grade[359])  # 拖动到可见的元素去
            # sleep(2)
            # grade = self.find_elements(seller['牌号css'])
            # self.script_top(grade[419])  # 拖动到可见的元素去
            # sleep(2)
            # grade = self.find_elements(seller['牌号css'])
            # self.script_top(grade[479])  # 拖动到可见的元素去
            # sleep(2)
            log.info('当前获取的牌号数量: ' + str(len(grade)))
            log.info('选择的牌号为 : ' + grade[grade_number].text)
            grade[grade_number].click()
        except:
            self.base_get_img()
            self.fail('牌号选择出错 或 无当前牌号')

    def seller_goods_stock_purchase(self, stock, min_purchase):
        self.input_clear_text(seller['原料库存'], stock)
        self.input_clear_text(seller['最低采购'], min_purchase)
        log.info('进行库存、最低采购填入')

    def seller_goods_delivery(self, deliver_type, deliver_price, pickup_price, delivery_days, pickup_day):
        self.input_clear_text(seller['配送单价'], deliver_price)
        self.is_click(seller['定金勾选'])
        self.is_click(seller['款到发货'])
        self.input_clear_text(seller['配送天数'], delivery_days)
        if deliver_type == 1:
            self.is_click(seller['点击自提按钮'])
            sleep(0.2)
            self.is_click(seller['自提款到发货'])
            self.input_clear_text(seller['自提单价'], pickup_price)
            self.input_clear_text(seller['提货时间'], pickup_day)
        log.info('商品金额配送信息信息填入')

    def seller_goods_deliver_area(self, deliver_area):
        self.is_click(seller['配送范围点击'])
        sleep(0.2)
        click_area = goods_deliver_area(deliver_area)
        if deliver_area != '全国':
            self.is_click(click_area)
        self.is_click(seller['配送范围选择全部'])
        try:
            self.is_click(seller['配送范围点击确定'])
        except:
            log.info('div[5]元素寻找不到 / 使用div[6]元素')
            self.is_click(seller['配送范围点击确定1'])
        log.info('选择的配送地区范围： ' + deliver_area)

    def seller_goods_unit_price(self, deliver_type, unit_price_type):
        if unit_price_type == 1:
            self.is_click(seller['自提不含税'])
        if deliver_type == 1:
            self.is_click(seller['配送不含税'])

    def seller_goods_upload(self, img_path, video_path):
        user = page_object.JsbUserPage.JsbUserPage(self.driver)
        user.script('950')
        self.driver.find_element(By.XPATH,
                                 "//*[@id='rawProvideImgVos']/div[2]/div[2]/div/span/div/div[1]/span/div[2]/span/input").send_keys(
            img_path)
        sleep()
        self.driver.find_element(By.XPATH,
                                 "//*[@id='rawProvideImgVos']/div[1]/div[2]/div/span/div/span/div[2]/span/input").send_keys(
            video_path)
        sleep(0.5)
        log.info('进行原料商品图片、视频上传')
        user.script('200')

    def seller_goods_detail(self, serve, profiles, detail, grade_number, upload_img, upload_video):
        self.seller_add_goods_repeat(profiles, detail)
        sleep(0.5)
        try:
            sleep(0.2)
            self.is_click(seller['原料提交'])
            sleep(0.2)
            log.info('原料添加进行提交')
            if serve == '24':
                assert self.return_current_url() == seller_url['24_raw_list']
            else:
                assert self.return_current_url() == seller_url['20_raw_list']
            log.info('原料新增成功')
            log.info('添加牌号成功 当前牌号为 :' + str(grade_number))
            grade_number += 1
            log.info('添加牌号成功 下次牌号为 :' + str(grade_number))
            return int(grade_number)
        except:
            self.base_get_img()
            log.info('添加牌号重复 当前牌号为 :' + str(grade_number))
            grade_number += 1
            log.info('添加牌号重复 下次牌号为 :' + str(grade_number))
            self.seller_goods_grade(grade_number)
            self.seller_goods_upload(upload_img, upload_video)
            self.seller_goods_detail(serve, profiles, detail, grade_number, upload_img, upload_video)

    def seller_goods_add_info(self, serve, grade_number, stock, min_purchase,
                              delivery_price,
                              deliver_area, deliver_day, pickup_day,
                              deliver_type,
                              pickup_price,
                              upload_img, upload_video, unit_price_type, profiles, detail):
        self.seller_goods_grade(grade_number)
        self.seller_goods_stock_purchase(stock, min_purchase)
        self.seller_goods_delivery(deliver_type, delivery_price, pickup_price, deliver_day, pickup_day)
        self.seller_goods_deliver_area(deliver_area)
        sleep(0.2)
        self.seller_goods_unit_price(deliver_type, unit_price_type)
        self.seller_goods_upload(upload_img, upload_video)
        sleep(1)
        grade_number = self.seller_goods_detail(serve, profiles, detail, grade_number, upload_img, upload_video)
        sleep(0.5)
        return grade_number

    def seller_goods_add_raw(self, serve, seller_phone, add_goods_type, grade_number, stock, min_purchase,
                             delivery_price,
                             deliver_area, deliver_day, pickup_day,
                             deliver_type,
                             pickup_price,
                             upload_img, upload_video, unit_price_type, profiles, detail, limit):
        self.seller_phone_login(serve, seller_phone)
        sleep(0.2)
        self.seller_skip_goods('skip_产品')
        add_num = 0
        add_number = grade_number
        while add_num < limit:
            sleep(0.2)
            self.seller_goods_choose(add_goods_type)
            sleep(0.2)
            add_number = self.seller_goods_add_info(serve, add_number, stock, min_purchase,
                                                    delivery_price,
                                                    deliver_area, deliver_day, pickup_day,
                                                    deliver_type,
                                                    pickup_price,
                                                    upload_img, upload_video, unit_price_type, profiles, detail)
            self.seller_goods_click_online(1)
            sleep(0.2)
            add_num += 1
            add_number += 1
            log.info('当前添加次数 : ' + str(add_num) + '  目标添加次数  : ' + str(limit))
            log.info('------------------------------------------------------------------------------------------------')

    def seller_product_info(self, title, subtitle, keywords, code, material, brand, need_sign_type):
        log.info("制成品商品基本信息填入")
        self.input_text(seller['制成品标题'], title)
        self.is_click(seller['制成品分类'])
        classify_id = self.find_elements(seller['分类class'])
        classify_id[0].click()
        log.info("所选择的商品分类 : " + classify_id[0].text)
        self.input_text(seller['制成品简略标题'], subtitle)
        self.input_text(seller['产品编号'], code)
        self.input_text(seller['材质'], material)
        self.input_text(seller['品牌'], brand)
        self.is_click(seller['制塑工艺'])
        craft = self.find_elements(seller['制塑工艺选择'])
        craft[0].click()
        craft[1].click()
        log.info('选择的制塑工艺 : ' + craft[0].text + ' \ ' + craft[1].text)
        self.is_click(seller['制成品关键词'])
        self.input_text(seller['制成品关键词输入'], keywords)
        self.input_text(seller['制成品关键词输入'], Keys.ENTER)
        log.info('输入的关键词 : ' + keywords)
        if need_sign_type == 1:
            self.is_click(seller['合同按钮点击'])
            log.info('该商品选择签署合同')

    def seller_product_logistics(self, address):
        self.is_click(seller['物流模板点击'])
        freight = self.find_elements(seller['物流选择'])
        freight[-1].click()
        log.info('当前选择的物流模板 : ' + freight[-1].text)
        self.input_text(seller['详细地址'], address)
        self.is_click(seller['制成品发货地点'])
        self.click_area()

    def seller_product_sku(self, sku_img, sku_name, sku_price, sku_min_purchase, sku_stock, sku_weight, sku_remark):
        log.info('产品规格信息填入')
        self.driver.find_element(By.XPATH,
                                 "//*[@id='ProductSpecsItemForm_url']/div[1]/span/div[2]/span/input").send_keys(
            sku_img)
        sleep(0.5)
        self.input_clear_text(seller['规格名称'], sku_name)
        self.input_clear_text(seller['制成品单价'], sku_price)
        self.input_clear_text(seller['制成品最低采购'], sku_min_purchase)
        self.input_clear_text(seller['制成品库存'], sku_stock)
        self.input_clear_text(seller['制成品重量'], sku_weight)
        self.input_clear_text(seller['规格备注'], sku_remark)

    def seller_product_detail(self, serve, img_path, video_path, profiles, detail):
        log.info('商品详情信息填入')
        self.seller_product_upload(img_path, video_path)
        sleep(0.5)
        self.seller_add_goods_repeat(profiles, detail)
        try:
            self.is_click(seller['制成品点击提交'])
            if serve == '24':
                assert self.return_current_url() == seller_url['24_product_list']
            else:
                assert self.return_current_url() == seller_url['20_product_list']
            log.info('制成品添加成功')
        except:
            log.info('测试出错 或 断言失败 ')
            self.fial_info()

    def seller_product_upload(self, img_path, video_path):
        self.driver.find_element(By.XPATH,
                                 "//*[@id='goodsImgVos']/div[2]/div[2]/div/span/div/div[1]/span/div[2]/span/input").send_keys(
            img_path)
        sleep(0.5)
        self.driver.find_element(By.XPATH,
                                 "//*[@id='goodsImgVos']/div[1]/div[2]/div/span/div/span/div[2]/span/input").send_keys(
            video_path)
        log.info('进行制成品商品图片、视频上传')

    def seller_add_goods_repeat(self, profiles, detail):
        self.input_clear_text(seller['内容概要'], profiles)
        iframe = self.find_element(seller['iframe框架'])
        self.driver.switch_to.frame(iframe)
        log.info('定位进入原料详情iframe')
        sleep(0.5)
        self.input_text(seller['商品详情'], detail)
        self.driver.switch_to.default_content()
        log.info('退出原料详情iframe定位')
        sleep(0.5)

    def seller_goods_add_product(self, serve, seller_phone, goods_type, title, subtitle, keywords, code, material,
                                 brand,
                                 need_sign_type, address, sku_img, sku_name, sku_price, sku_min_purchase, sku_stock,
                                 sku_weight, sku_remark, img_path, video_path, profiles, detail, limit):
        self.seller_phone_login(serve, seller_phone)
        self.seller_skip_goods('skip_产品')
        add_num = 0
        while add_num < limit:
            sleep(0.2)
            self.seller_goods_choose(goods_type)
            sleep(0.2)
            self.seller_product_info(title + str(add_num), subtitle, keywords, code, material, brand, need_sign_type)
            self.seller_product_logistics(address)
            self.script('5000')
            self.seller_product_sku(sku_img, sku_name, sku_price, sku_min_purchase, sku_stock, sku_weight, sku_remark)
            self.script('1000')
            self.seller_product_detail(serve, img_path, video_path, profiles, detail)
            self.seller_goods_click_online(2)
            add_num += 1
            log.info('当前添加次数 : ' + str(add_num) + '  目标添加次数  : ' + str(limit))

    def seller_goods_classification_detail(self, type_name, classification_type, state, father_type):
        #  old_classification = self.find_elements(seller['分类tr'])
        #   log.info(old_classification)
        self.is_click(seller['添加分类按钮'])
        self.input_text(seller['分类名称'], type_name)
        if state == 1:
            self.is_click(seller['分类启用状态'])
            log.info('该分类进行启用')
        if classification_type == 2:
            self.is_click(seller_url[classification_type])
        if father_type == 1:
            self.is_click(seller['点击分类父类'])
            father = self.find_elements(seller['分类父类选择'])
            father[0].click()
            log.info('选择父类为: ' + father[0].text)
        self.is_click(seller['分类点击确定'])
        self.refresh()
        #  new_classification = self.find_elements(seller['分类tr'])
        try:
            #    # assert len(new_classification) > len(old_classification)
            log.info('产品分类添加成功')
        except:
            log.info('产品分类添加失败')
            self.fial_info()

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
        self.click_action(seller['金额卷元增加'], 1)
        self.click_action(seller['发放数量点击增加'], 10)
        log.info(num.get_attribute())
        self.input_text(seller['金额卷满元'], 10)
        self.is_click(seller['领取后生效'])
        self.click_action(seller['有效天数点击增加'], 1)
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
        except:
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
        self.is_click(seller['市场信息智能搜索'])
        self.is_click(seller['市场信息牌号选择'])
        self.click_action(seller['市场信息单吨价格增加'], 1)
        self.click_action(seller['市场信息发布数量增加'], 1)
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
        self.click_action(seller['采购需求卖主数量增加'], 1)
        self.click_action(seller['采购需求单吨价格增加'], 1)
        self.click_action(seller['采购需求订购数量增加'], 1)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="rawDemAndImgList"]/div[1]/div[2]/div/span/div/span/div[2]/span/input').send_keys(
            video_path)
        self.is_click(seller['供需交货范围'])
        self.click_area()
        self.is_click(seller['采购需求智能搜索'])
        self.is_click(seller['采购需求牌号选择'])
        self.is_click(seller['采购需求提交'])

    def seller_supply_submit(self):
        try:
            assert self.return_current_url() == seller_url['供需列表']
            log.info('新增供需成功')
        except:
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
        except:
            log.info('优惠劵添加失败 ')
            self.fial_info()

    def seller_supply_demand(self, serve, seller_phone, supply_type, limit, title, content, video_path, img_path):
        self.seller_phone_login(serve, seller_phone)
        self.seller_skip_goods('skip_供需')
        add_num = 0
        while add_num < limit:
            self.is_click(seller['供需点击发布'])
            if supply_type == 1:
                self.seller_supply_market(title, content, video_path, img_path)
            else:
                self.seller_supply_purchase(title, content, video_path, img_path)
            self.seller_supply_submit()
            add_num += 1
            log.info('当前添加次数 : ' + str(add_num) + '  目标添加次数  : ' + str(limit))
