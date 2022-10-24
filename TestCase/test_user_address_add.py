#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pytest

from page_object.JsbUserPage import JsbUserPage
from utils.log import Log

log = Log()
user_url = {'24': 'http://192.168.101.24:8090/shop/home', '20': 'https://demo.jinsubao.cn/'}
seller_url = {'24': 'http://192.168.101.24:8070/user/login', '20': 'https://slrdm.jinsubao.cn/'}


class TestUserAddress:

    def test_user_address_add(self, drivers):
        log.info('当前执行   买家收货地址新增    ')
        user = JsbUserPage(drivers)
        serve = '20'
        user_phone = '18912340003'
        recipient_name = 'zzzz收件人'
        address_name = 'zzzz详细地址'
        contact_phone = '13600136000'
        post_code = '560123'
        fixed_telephone = '865636446'
        default_type = 1
        limit = 50
        user.user_address_add(serve, user_phone, recipient_name, address_name, contact_phone, post_code,
                              fixed_telephone, default_type,
                              limit)


if __name__ == '__main__':
    pytest.main(['TestCase/test_user_address_add.py'])
