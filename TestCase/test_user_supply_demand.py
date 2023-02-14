#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import time

import allure
import pytest

from page_object.JsbDemandPage import JsbDemand
from utils.log import Log
from utils.tool_util import time_lag

log = Log()
user_url = {'24': 'http://192.168.101.24:8090/shop/home', '20': 'https://demo.jinsubao.cn/'}
seller_url = {'24': 'http://192.168.101.24:8070/user/login', '20': 'https://slrdm.jinsubao.cn/'}


@allure.feature('买家发布供需资讯')
class TestUserSupplyDemand:

    @allure.title('买家发布供需资讯流程')
    @allure.description(
        '1.进行判断买家当前要进行操作的环境 2.进行买家登录,跳转买家的用户中心 - 供需资讯列表 进行发布 3.发布时会进行判断当前发布的类型是市场信息还是采购需求')
    def test_user_supply(self, drivers):
        log.info('当前执行   买家发布供需    ')
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        demand = JsbDemand(drivers)
        serve = '24'
        # user_phone = '18912340003'
        user_phone = '13500135000'
        limit = 1
        title = '出售原料 原厂原包'
        seller_num = 8
        price = 7800
        num = 10
        release_type = 1  # 2市场信息  1采购需求
        video_path = 'D:\\资料\\video.mp4'
        content = '出售原厂原包原料'
        img_path = 'D:\\资料\\raw.png'
        grade_number = 0
        add_type = 1
        number = 'pp'
        circulation = 1
        demand.user_demand(serve, user_phone, release_type, title, content, img_path, video_path, seller_num, price,
                           num, limit, grade_number, add_type, number, circulation)
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(["./test_user_supply_demand.py",
                 "-sv", "--alluredir", "./reports/temp_user_demand"])
    os.system("allure generate ./report/temp_user_demand -o ./reports/html --clean")
