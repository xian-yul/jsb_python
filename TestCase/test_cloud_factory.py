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
        user_phone = '13000000001'
        name = '自动化入驻'  # 工厂名称
        contacts = '厂长'  # 联系人
        area = '5000'  # 面积
        employeesNum = '500'  # 员工人数
        deviceNum = '1000'  # 加工设备
        mainProduct = '荧光粉'  # 主营商品
        address = '不是工厂地址'  # 工厂地址
        remarks = '不是工厂简介'  # 简介
        workersNum = '500'  # 生产人数
        annualOutputValue = '1000'  # 年产值
        qualityCertification = ''  # 生产质量
        systemCertification = ''  # 管理体系
        specialTechnology = ''  # 特殊工艺
        device_name = '设备'  # 设备名称
        device_num = '500'  # 设备数量
        device_brand = '品牌'  # 设备品牌
        device_model = '型号'  # 设备型号
        device_addNum = 2  # 车间设备添加次数
        patent_addNum = 3  # 专利资质添加次数
        patent_name = '专利'  # 专利名称
        patent_patentNumber = 'S1401'  # 专利号
        device_uploadNum = 2  # 车间设备上传图片次数 , device_imgPath, patent_imgPath
        patent_uploadNum = 3  # 专利资质上传图片次数
        device_imgPath = 'D:\\资料\\dxb.jpg'  # 车间设备图片url
        patent_imgPath = 'D:\\资料\\czh.jpg'  # 专利资质图片url
        cloudFactory = JsbCloudFactory(drivers)
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        cloudFactory.user_cloud_factory_apply_for(serve, user_phone, name, contacts, area, employeesNum, deviceNum,
                                                  mainProduct, address, remarks, workersNum, annualOutputValue,
                                                  qualityCertification,
                                                  systemCertification, specialTechnology, device_name, device_num,
                                                  device_brand,
                                                  device_model, patent_name, patent_patentNumber, device_addNum,
                                                  patent_addNum, device_uploadNum, patent_uploadNum, device_imgPath,
                                                  patent_imgPath)
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_cloud_factory.py'])
