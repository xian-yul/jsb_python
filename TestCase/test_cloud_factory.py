import time
import allure
import pytest

from page_object.JsbCloudFactory import JsbCloudFactory
from utils.log import Log
from utils.tool_util import time_lag

log = Log()


@allure.feature('执行买家云工厂入驻')
class TestCloudFactory:

    @allure.title('买家云工厂入驻')
    def test_cloud_factory(self, drivers):
        log.info('当前执行   云工厂入驻数据填写   ')
        serve = '24'
        user_phone = ''
        name = ''  # 工厂名称
        contacts = ''  # 联系人
        area = ''  # 面积
        employeesNum = ''  # 员工人数
        deviceNum = ''  # 加工设备
        mainProduct = ''  # 主营商品
        address = ''  # 工厂地址
        remarks = ''  # 简介
        workersNum = ''  # 生产人数
        annualOutputValue = ''  # 年产值
        qualityCertification = ''  # 生产质量
        systemCertification = ''  # 管理体系
        specialTechnology = ''  # 特殊工艺
        device_name = ''  # 设备名称
        device_num = ''  # 设备数量
        device_brand = ''  # 设备品牌
        device_model = ''  # 设备型号
        patent_name = ''  # 专利名称
        patent_patentNumber = ''  # 专利号
        cloudFactory = JsbCloudFactory(drivers)
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        cloudFactory.user_cloud_factory_apply_for(serve, user_phone, name, contacts, area, employeesNum, deviceNum,
                                                  mainProduct, address, remarks, workersNum, annualOutputValue,
                                                  qualityCertification,
                                                  systemCertification, specialTechnology, device_name, device_num,
                                                  device_brand,
                                                  device_model, patent_name, patent_patentNumber)
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_cloud_factory.py'])
