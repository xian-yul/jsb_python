import page_object.JsbSellerPage
import page_object.JsbUserPage
from common.readelement import Element
from page.webpage import WebPage
from utils import tool_util
from utils.log import Log
from utils.times import sleep

user_url = {'24': 'http://192.168.101.24:8090/shop/home', '20': 'https://demo.jinsubao.cn/'}
seller_url = {'24': 'http://192.168.101.24:8070/user/login', '20': 'https://slrdm.jinsubao.cn/'}

user_yaml = Element('user')
seller_yaml = Element('seller')
log = Log()


class JsbPackagingMethod(WebPage):

    def seller_phone_login(self, serve, phone):
        if serve == '24':
            self.driver.get(seller_url['24'])
        else:
            self.driver.get(seller_url['20'])
        seller = page_object.JsbSellerPage.JsbSellerPage(self.driver)
        seller.seller_backstage_title()
        seller.input_seller_phone(phone)
        log.info('输入手机号  : ' + phone)
        seller.click_phone_code()
        log.info('点击验证码按钮')
        sleep(0.2)
        seller.click_phone_login_btn()
        log.info('点击登录')
        sleep(0.2)
        seller.seller_login_info()

    #     seller.seller_exit_login(log)

    def seller_number_login(self, serve, number, password):
        if serve == '24':
            self.driver.get(seller_url['24'])
        else:
            self.driver.get(seller_url['20'])
        seller = page_object.JsbSellerPage.JsbSellerPage(self.driver)
        seller.toggle_number_login()
        log.info('切换子账号登录')
        sleep(0.5)
        seller.seller_number_username(number)
        log.info('输入账号  : ' + number)
        sleep(0.5)
        seller.seller_number_password(password)
        sleep(0.5)
        log.info('输入密码  : ' + password)
        seller.seller_number_login_btn()
        log.info('点击登录')
        seller.seller_login_info()
        sleep()
        seller.seller_exit_login()

    def user_login(self, serve, phone):
        if serve == '24':
            self.driver.get(user_url['24'])
        else:
            self.driver.get(user_url['20'])
        user = page_object.JsbUserPage.JsbUserPage(self.driver)
        user.click_user_login()
        user.input_user_phone(phone)
        user.click_user_code()
        user.click_login_btn()
        user.compare_user_phone(phone)
        user.click_login_exit()

    def place_order_repeatedly(self, user_phone, org_name, shop_num, delivery_type, pickup_type, address_name,
                               sign_type,
                               billing_type, limit, seller_phone, serve):
        user = page_object.JsbUserPage.JsbUserPage(self.driver)

        user.place_order(user_phone, org_name, shop_num, delivery_type, pickup_type, address_name, sign_type,
                         billing_type, seller_phone, serve, limit)

    def seller_goods_add_product_repeatedly(self, serve, seller_phone, goods_type, title, subtitle, keywords, code,
                                            material,
                                            brand,
                                            need_sign_type, address, sku_img, sku_name, sku_price, sku_min_purchase,
                                            sku_stock,
                                            sku_weight, sku_remark, img_path, video_path, profiles, detail, limit):
        seller = page_object.JsbSellerPage.JsbSellerPage(self.driver)
        seller.seller_goods_add_product(serve, seller_phone, goods_type, title, subtitle, keywords, code, material,
                                        brand,
                                        need_sign_type, address, sku_img, sku_name, sku_price, sku_min_purchase,
                                        sku_stock,
                                        sku_weight, sku_remark, img_path, video_path, profiles, detail, limit)

    def seller_goods_add_raw_repeatedly(self, serve, seller_phone, add_goods_type, grade_number, stock, min_purchase,
                                        delivery_price,
                                        deliver_area, deliver_day, pickup_day,
                                        deliver_type,
                                        pickup_price,
                                        upload_img, upload_video, unit_price_type, profiles, detail, limit):
        seller = page_object.JsbSellerPage.JsbSellerPage(self.driver)
        seller.seller_goods_add_raw(serve, seller_phone, add_goods_type, grade_number, stock, min_purchase,
                                    delivery_price,
                                    deliver_area, deliver_day, pickup_day,
                                    deliver_type,
                                    pickup_price,
                                    upload_img, upload_video, unit_price_type, profiles, detail, limit)

    def seller_coupon(self, serve, seller_phone, coupon_name, coupon_type, suit_type, target_range_type, content, quota,
                      limit):
        seller = page_object.JsbSellerPage.JsbSellerPage(self.driver)
        seller.seller_phone_login(serve, seller_phone)
        seller.seller_coupon_skip(coupon_type)
        add_num = 0
        coupon_name = coupon_name + str(tool_util.random_number(3))
        while add_num < limit:
            self.is_click(seller_yaml['点击创建优惠劵'])
            seller.seller_coupon_detail(coupon_name, suit_type, target_range_type, content, quota)
            seller.seller_coupon_submit(serve)
            log.info('当前添加次数 : ' + str(add_num) + '  预计添加次数  : ' + str(limit))
            add_num += 1

    def seller_storehouse(self, serve, seller_phone, storehouse_name, storehouse_address, storehouse_contact,
                          storehouse_phone, default, limit):
        seller = page_object.JsbSellerPage.JsbSellerPage(self.driver)
        seller.seller_phone_login(serve, seller_phone)
        seller.seller_skip_goods('仓库')
        add_num = 0
        log.info('进行添加仓库地址')
        while add_num < limit:
            seller.seller_storehouse_detail(storehouse_name, storehouse_address, storehouse_contact,
                                            storehouse_phone, default)
            log.info('当前添加次数 : ' + str(add_num) + '  预计添加次数  : ' + str(limit))
            add_num += 1

    def seller_goods_classification_add(self, serve, seller_phone, type_name, classification_type, state, father_type,
                                        limit):
        seller = page_object.JsbSellerPage.JsbSellerPage(self.driver)
        seller.seller_phone_login(serve, seller_phone)
        seller.seller_skip_goods('分类')
        add_num = 0
        while add_num < limit:
            seller.seller_goods_classification_detail(type_name, classification_type, state, father_type)
            log.info('当前添加次数 : ' + str(add_num) + '  预计添加次数  : ' + str(limit))
            add_num += 1

    def seller_supply_demand(self, serve, seller_phone, supply_type, limit, title, content, video_path, img_path):
        seller = page_object.JsbSellerPage.JsbSellerPage(self.driver)
        seller.seller_supply_demand(serve, seller_phone, supply_type, limit, title, content, video_path, img_path)

    def user_address(self, serve, user_phone, recipient_name, address_name, contact_phone, post_code,
                     fixed_telephone, default_type,
                     limit):
        user = page_object.JsbUserPage.JsbUserPage(self.driver)
        user.user_address_add(serve, user_phone, recipient_name, address_name, contact_phone, post_code,
                              fixed_telephone, default_type,
                              limit)

    def user_industry_academia_repeatedly(self, serve, user_phone, industry_type, title, profiles, phone, detail,
                                          contacts,
                                          img_path, video_path, patent_number, limit):
        user = page_object.JsbUserPage.JsbUserPage(self.driver)
        user.user_industry_academia(serve, user_phone, industry_type, title, profiles, phone, detail, contacts,
                                    img_path, video_path, patent_number, limit)

    def user_supply_demand(self, serve, user_phone, publish_type, title, content, img_path, seller_num, price,
                           order_num, limit, video_path):
        user = page_object.JsbUserPage.JsbUserPage(self.driver)
        user.user_supply_demand(serve, user_phone, publish_type, title, content, img_path, seller_num, price,
                                order_num, limit, video_path)
