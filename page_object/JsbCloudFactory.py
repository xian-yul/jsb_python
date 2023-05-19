from common.readelement import Element
from page.webpage import WebPage
from utils import tool_util
from utils.log import Log
from utils.times import sleep

log = Log()

cloud = Element('JsbCloudFactory')
cloud_url = {'24_cloud_apply_for_home': 'http://192.168.101.24:8090/store/open/home',
             '24_cloud_apply_for': 'http://192.168.101.24:8090/store/open/open-factory',
             '24_cloud_apply_for_submit': 'http://192.168.101.24:8090/store/open/first-settle-in-factory-state',
             '20_cloud_apply_for_home': 'https://demo.jinsubao.cn/store/open/home',
             '20_cloud_apply_for': 'https://demo.jinsubao.cn/store/open/open-factory',
             '20_cloud_apply_for_submit': ''}


class JsbCloudFactory(WebPage):
    def user_cloud_factory_apply_for(self, serve, user_phone, name, contacts, area, employeesNum, deviceNum,
                                     mainProduct, address, remarks, workersNum, annualOutputValue, qualityCertification,
                                     systemCertification, specialTechnology, device_name, device_num, device_brand,
                                     device_model, patent_name, patent_patentNumber, device_addNum, patent_addNum,
                                     device_uploadNum, patent_uploadNum, device_imgPath, patent_imgPath):
        self.click_user_login(serve, user_phone)
        sleep(0.1)
        self.is_click(cloud['cloud_factory_apply_for'])
        sleep(0.1)
        self.win_handles('-1')
        sleep(0.1)
        try:
            if serve == '24':
                assert self.return_current_url() == cloud_url['24_cloud_apply_for_home']
            else:
                assert self.return_current_url() == cloud_url['20_cloud_apply_for_home']
            log.info('云工厂入驻 断言成功')
        except AssertionError:
            log.error('云工厂入驻 断言失败')
            self.fial_info()
        self.is_click(cloud['cloud_factory_apply_for_bg'])
        sleep(0.1)
        try:
            if serve == '24':
                assert self.return_current_url() == cloud_url['24_cloud_apply_for']
            else:
                assert self.return_current_url() == cloud_url['20_cloud_apply_for']
            log.info('填写云工厂资料 断言成功')
        except AssertionError:
            log.error('填写云工厂资料 断言失败')
            self.fial_info()
        self.script('400')
        self.input_clear_text(cloud['cloud_name_ipt'], name)
        self.is_click(cloud['cloud_establish_time'])
        sleep(0.1)
        self.is_click(cloud['cloud_establish_time_now'])
        self.input_clear_text(cloud['cloud_contacts_ipt'], contacts)
        self.input_clear_text(cloud['cloud_phone_ipt'], user_phone)
        self.input_clear_text(cloud['cloud_area_ipt'], area)
        self.input_clear_text(cloud['cloud_employeesNum_ipt'], employeesNum)
        self.input_clear_text(cloud['cloud_deviceNum_ipt'], deviceNum)
        self.input_clear_text(cloud['cloud_mainProduct_ipt'], mainProduct)
        self.is_click(cloud['cloud_city_span'])
        self.click_area()
        self.input_clear_text(cloud['cloud_address_textarea'], address)
        self.input_clear_text(cloud['cloud_remarks_textarea'], remarks)
        sleep(0.1)
        self.is_click(cloud['cloud_next_btn_btn'])
        log.info('综合描述填写完毕  进行下一步填写')
        sleep(0.1)
        self.input_clear_text(cloud['cloud_workersNum_ipt'], workersNum)
        self.input_clear_text(cloud['cloud_annualOutputValue_ipt'], annualOutputValue)
        self.is_click(cloud['cloud_raw__select_div'])
        sleep(0.1)
        self.find_elements(cloud['cloud_raw_li'])[0].click()
        self.input_clear_text(cloud['cloud_qualityCertification_ipt'], qualityCertification)
        self.input_clear_text(cloud['cloud_systemCertification_ipt'], systemCertification)
        self.input_clear_text(cloud['cloud_specialTechnology_ipt'], specialTechnology)
        self.is_click(cloud['cloud_next_btn_btn'])
        log.info('生产实力填写完毕  进行下一步填写')
        sleep(0.1)
        add_num = 1
        while add_num <= device_addNum:
            self.is_click(cloud['cloud_device_add_btn'])
            self.input_clear_text(cloud['cloud_device_name_ipt'], device_name + '__' + str(add_num))
            self.input_clear_text(cloud['cloud_device_num_ipt'], device_num)
            self.input_clear_text(cloud['cloud_device_brand_ipt'], device_brand + '__' + str(add_num))
            self.input_clear_text(cloud['cloud_device_model_ipt'], device_model + '__' + str(add_num))
            self.is_click(cloud['cloud_device_submit_btn'])
            log.info(
                f'当前添加设备次数为为 :{add_num}次, 预计添加 {device_addNum}次'.format(add_num,
                                                                                        device_addNum))
            add_num += 1
            sleep(0.1)
            if add_num == device_addNum:
                continue
        upload_num = 1
        while upload_num <= device_uploadNum:
            self.find_elements(cloud['upload'])[0].send_keys(device_imgPath)
            log.info(
                f'当前添加车间设备图片次数为 :{upload_num}次, 预计添加 {device_uploadNum}次'.format(upload_num,
                                                                                                    device_uploadNum))
            upload_num += 1
            sleep(0.2)
            if upload_num == device_uploadNum:
                continue
        self.is_click(cloud['cloud_next_btn_btn'])
        log.info('车间设备填写完毕  进行下一步填写')
        sleep(0.1)
        add_num = 1
        while add_num <= patent_addNum:
            self.is_click(cloud['cloud_device_add_btn'])
            self.input_clear_text(cloud['cloud_patent_name_ipt'], patent_name + '__' + str(add_num))
            self.input_clear_text(cloud['cloud_patent_patentNumber_ipt'], tool_util.random_number(4))
            self.is_click(cloud['cloud_device_submit_btn'])
            log.info(
                f'当前添加专利资质次数为 :{add_num}次, 预计添加 {patent_addNum}次'.format(add_num,
                                                                                          patent_addNum))
            add_num += 1
            sleep(0.1)
            if add_num == patent_addNum:
                continue
            upload_num = 1
        while upload_num <= patent_uploadNum:
            self.find_elements(cloud['upload'])[1].send_keys(patent_imgPath)
            log.info(
                f'当前添加专利资质图片次数为 :{upload_num}次, 预计添加 {patent_uploadNum}次'.format(upload_num,
                                                                                                    patent_uploadNum))
            upload_num += 1
            sleep(0.2)
            if upload_num == patent_uploadNum:
                continue
        self.is_click(cloud['cloud_next_btn_btn'])
        log.info('云工厂入驻审核提交')
        try:
            if serve == '24':
                assert self.return_current_url() == cloud_url['24_cloud_apply_for_submit']
            else:
                assert self.return_current_url() == cloud_url['20_cloud_apply_for_submit']
            log.info('工厂入驻提交审核 断言成功')
        except AssertionError:
            log.error('工厂提交审核 断言失败')
            self.fial_info()
        log.info('云工厂入驻提交成功')
