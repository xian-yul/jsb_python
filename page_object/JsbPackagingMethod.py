from common.readelement import Element
from page.webpage import WebPage
from page_object.JsbSellerPage import JsbSeller
from page_object.JsbUserPage import JsbUserPage
from utils import tool_util
from utils.log import Log
from utils.times import sleep

user_url = {'24': 'http://192.168.101.24:8090/shop/home', '20': 'https://demo.jinsubao.cn/'}
seller_url = {'24': 'http://192.168.101.24:8070/user/login', '20': 'https://slrdm.jinsubao.cn/'}

user_yaml = Element('user')
seller_yaml = Element('seller')
log = Log()


class JsbPackagingMethod(WebPage):

    def seller_coupon(self, serve, seller_phone, coupon_name, coupon_type, suit_type, target_range_type, content, quota,
                      limit):
        seller = JsbSeller(self.driver)
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
        seller = JsbSeller(self.driver)
        seller.seller_phone_login(serve, seller_phone)
        seller.seller_skip_goods('点击产品管理', '仓库地址')
        add_num = 0
        log.info('进行添加仓库地址')
        while add_num < limit:
            seller.seller_storehouse_detail(storehouse_name, storehouse_address, storehouse_contact,
                                            storehouse_phone, default)
            log.info('当前添加次数 : ' + str(add_num) + '  预计添加次数  : ' + str(limit))
            add_num += 1

    def seller_goods_classification_add(self, serve, seller_phone, type_name, classification_type, state, father_type,
                                        limit):
        seller = JsbSeller(self.driver)
        seller.seller_phone_login(serve, seller_phone)
        seller.seller_skip_goods('点击产品管理', '产品分类')
        add_num = 0
        while add_num < limit:
            seller.seller_goods_classification_detail(type_name, classification_type, state, father_type)
            log.info('当前添加次数 : ' + str(add_num) + '  预计添加次数  : ' + str(limit))
            add_num += 1

    def seller_supply_demand(self, serve, seller_phone, supply_type, limit, title, content, video_path, img_path):
        seller = JsbSeller(self.driver)
        seller.seller_supply_demand(serve, seller_phone, supply_type, limit, title, content, video_path, img_path)

    def user_address(self, serve, user_phone, recipient_name, address_name, contact_phone, post_code,
                     fixed_telephone, default_type,
                     limit):
        user = JsbUserPage(self.driver)
        user.user_address_add(serve, user_phone, recipient_name, address_name, contact_phone, post_code,
                              fixed_telephone, default_type,
                              limit)

    def user_industry_academia_repeatedly(self, serve, user_phone, industry_type, title, profiles, phone, detail,
                                          contacts,
                                          img_path, video_path, patent_number, limit):
        user = JsbUserPage(self.driver)
        user.user_industry_academia(serve, user_phone, industry_type, title, profiles, phone, detail, contacts,
                                    img_path, video_path, patent_number, limit)

    def user_supply_demand(self, serve, user_phone, publish_type, title, content, img_path, seller_num, price,
                           order_num, limit, video_path):
        user = JsbUserPage(self.driver)
        user.user_supply_demand(serve, user_phone, publish_type, title, content, img_path, seller_num, price,
                                order_num, limit, video_path)
