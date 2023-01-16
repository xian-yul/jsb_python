from common.readelement import Element
from page.webpage import WebPage
from utils.log import Log
from utils.times import sleep

address = Element('JsbUserAddress')
log = Log()


class JsbUserAddressPage(WebPage):

    def user_address_add(self, serve, user_phone, default_type, limit):
        address_num = 0
        self.click_user_login(serve, user_phone)
        self.is_click(address['user_home_click'])
        sleep(0.3)
        self.find_elements(address['user_home_li'])[8].click()
        sleep(0.2)
        while address_num < limit:
            self.find_elements(address['add_address_btn'])[1].click()
            sleep(0.2)
            self.input_clear_text(address['address_contact'], '收货人')
            self.is_click(address['address_city'])
            sleep(0.2)
            self.click_area()
            self.input_clear_text(address['address_detail'], '详细地址11111')
            self.input_clear_text(address['address_phone'], '13600136000')
            if default_type == 1:
                self.is_click(address['address_default'])
                log.info('当前地址设置为默认地址')
            self.is_click(address['address_submit'])
            address_num += 1
            log.info('当前新增地址次数:' + str(address_num) + ' 预计新增次数: ' + str(limit))
        log.info('-----------------------------------------------------')
