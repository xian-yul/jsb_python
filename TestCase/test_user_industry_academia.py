#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

import pytest

from page_object.JsbPackagingMethod import JsbPackagingMethod
from utils.log import Log
from utils.tool_util import time_lag

log = Log()


class TestUserIndustryAcademia:

    def test_user_industry_academia(self, drivers):
        log.info('当前执行   买家端添加产学融合    ')
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        user = JsbPackagingMethod(drivers)
        serve = '24'
        limit = 1
        user_phone = '13500135000'
        industry_type = 3
        title = '产学融合标题'
        profiles = '产学融合概要'
        phone = '13600136000'
        detail = '产学融合详情'
        contacts = 'selenium'
        patent_number = 123456
        img_path = 'D:\资料\上传图片\yuanliao.png'
        video_path = 'D:\资料\原料.mp4'
        user.user_industry_academia_repeatedly(serve, user_phone, industry_type, title, profiles, phone, detail, contacts,
                                    img_path, video_path, patent_number,limit)
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_user_industry_academia.py'])
