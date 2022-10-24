#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pytest

from page_object.JsbUserPage import JsbUserPage
from utils.log import Log

log = Log()


class TestUserRegister:

    def test_user_register(self, drivers):
        log.info('当前执行   用户注册    ')
        user = JsbUserPage(drivers)
        serve = '24'
        limit = 10
        user.user_register(serve, limit)


if __name__ == '__main__':
    pytest.main(['TestCase/test_user_register.py'])
