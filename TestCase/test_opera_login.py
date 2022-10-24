#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pytest

from page_object.JsbOperationPage import JsbOperationPage
from utils.log import Log

log = Log()


class TestOperaLogin:

    def test_opera_login(self, drivers):
        log.info('当前执行   运营端登录    ')
        opera = JsbOperationPage(drivers)
        serve = '24_login'
        opera_phone = '13600136000'
        opera.opera_login(serve, opera_phone)


if __name__ == '__main__':
    pytest.main(['-v', '--html=opera_login_report.html', 'test_opera_login.py'])
