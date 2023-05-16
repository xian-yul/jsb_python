from common.readelement import Element
from page.webpage import WebPage
from utils.log import Log
from utils.times import sleep

log = Log()

cloud = Element('jsbCloudFactory')


class JsbCloudFactory(WebPage):
    def user_cloud_factory_apply_for(self, serve, user_phone, name, contacts, area, employeesNum, deviceNum,
                                     mainProduct, address, remarks, workersNum, annualOutputValue, qualityCertification,
                                     systemCertification, specialTechnology, device_name, device_num, device_brand,
                                     device_model, patent_name, patent_patentNumber):
        self.click_user_login(serve, user_phone)
        self.is_click(cloud['cloud_factory_apply_for'])
        self.is_click(cloud['cloud_factory_apply_for_bg'])
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
        self.input_clear_text(cloud['cloud_qualityCertification_ipt'], qualityCertification)
        self.input_clear_text(cloud['cloud_systemCertification_ipt'], systemCertification)
        self.input_clear_text(cloud['cloud_specialTechnology_ipt'], specialTechnology)
        self.is_click(cloud['cloud_raw__select_div'])
        sleep(0.1)
        self.find_elements(cloud['cloud_raw_li'])[0].click()
        self.is_click(cloud['cloud_next_btn_btn'])
        log.info('生产实力填写完毕  进行下一步填写')
        sleep(0.1)
        self.is_click(cloud['cloud_device_add_btn'])
        self.input_clear_text(cloud['cloud_device_name_ipt'], device_name)
        self.input_clear_text(cloud['cloud_device_num_ipt'], device_num)
        self.input_clear_text(cloud['cloud_device_brand_ipt'], device_brand)
        self.input_clear_text(cloud['cloud_device_model_ipt'], device_model)
        self.is_click(cloud['cloud_device_submit_btn'])
        sleep(0.1)
        log.info('车间设备填写完毕  进行下一步填写')
        sleep(0.1)
        self.is_click(cloud['cloud_device_add_btn'])
        self.input_clear_text(cloud['cloud_patent_name_ipt'], patent_name)
        self.input_clear_text(cloud['cloud_patent_patentNumber_ipt'], patent_patentNumber)
        self.is_click(cloud['cloud_device_submit_btn'])
        sleep(0.1)
        self.is_click(cloud['cloud_next_btn_btn'])
        log.info('云工厂入驻审核提交')
