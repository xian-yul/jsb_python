from telnetlib import EC

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from common.readelement import Element
from page.webpage import WebPage
from utils.log import Log
from utils.times import sleep

collage = Element('JsbCollage')
log = Log()

opera_collage = {'24_collage_list': 'http://192.168.101.24:8050/central-purchase/table', '20_collage_list': '',
                 '24_collage_inspect': 'http://192.168.101.24:8050/central-purchase/collection-info-details',
                 '20_collage_inspect': ''}
seller_collage = {'24_collage_list': 'http://192.168.101.24:8070/centralized-purchase/table', '20_collage_list': '',
                  '24_collage_release': 'http://192.168.101.24:8070/centralized-purchase/publish-collection-from',
                  '20_collage_release': ''}


class JsbCollage(WebPage):

    def seller_collage_release(self, serve, seller_phone, minimum, add_type, circulation, goodsNumber,
                               delivery_method, collage_num, overflow_num, delivery_day, delivery_price,
                               deposit, describe, limit, brand, max_day):
        add_num = 0
        self.seller_phone_login(serve, seller_phone)
        self.is_click(collage['collage_li'])
        self.is_click(collage['collage_info_li'])
        try:
            if serve == '24':
                assert self.return_current_url() == seller_collage['24_collage_list']
            else:
                assert self.return_current_url() == seller_collage['20_collage_list']
            log.info('集采信息界面断言判断成功')
            while add_num < limit:
                self.is_click(collage['collage_release_btn'])
                sleep(0.1)
                if serve == '24':
                    assert self.return_current_url() == seller_collage['24_collage_release']
                else:
                    assert self.return_current_url() == seller_collage['20_collage_release']
                log.info('集采信息发布界面断言判断成功')
                self.goods_grade(goodsNumber, add_type, brand, circulation)
                self.input_clear_text(collage['collage_minPurchase'], minimum)
                self.find_elements(collage['collage_contract'])[0].click()
                self.find_elements(collage['collage_contract_li'])[0].click()
                self.input_clear_text(collage['collage_purchaseNum'], collage_num)
                self.input_clear_text(collage['collage_overflow'], overflow_num)
                self.input_clear_text(collage['collage_deliveryDays'], delivery_day)
                if delivery_method == 1:
                    self.input_clear_text(collage['collage_deliveryPrice'], delivery_price)
                else:
                    self.input_clear_text(collage['collage_selfMentionPrice'], delivery_price)
                self.input_clear_text(collage['collage_handlesRate'], deposit)
                self.find_elements(collage['collage_start_time'])[0].click()
                sleep(0.1)
                self.find_elements(collage['collage_start_time_start'])[0].click()
                sleep(0.2)
                if max_day == 1:  # 集采时间的最长 最短
                    self.find_elements(collage['collage_start_time_end'])[0].click()
                else:
                    self.find_elements(collage['collage_start_time_end'])[-1].click()
                self.is_click(collage['collage_start_time_btn'])
                self.script('10000')
                self.is_click(collage['collage_deliveryAreaName'])
                sleep(0.1)
                self.is_click(collage['collage_deliveryAreaName_whole'])
                self.is_click(collage['collage_deliveryAreaName_btn'])
                self.input_clear_text(collage['collage_remark'], describe)
                sleep(0.2)
                self.find_elements(collage['collage_submit_btn'])[0].click()
                sleep(0.3)
                log.info('当前新增次数 : ' + str(add_num) + '  预计新增次数  : ' + str(limit))
                add_num += 1
                goodsNumber += 1
            log.info('新增集采信息完毕,已新增 ' + str(add_num))
        except AssertionError:
            log.error('断言失败')
            self.fial_info()

    def user_collage_place_order(self, serve, user_phone, purchase_num, purchase_goods, limit):
        self.click_user_login(serve, user_phone)

    def opera_collage_inspect(self, serve, opera_phone, inspect_type, reject_reason, limit):
        inspect_num = 0
        self.opera_login(serve, opera_phone)
        self.is_click(collage['collage_li'])
        self.is_click(collage['collage_info_li'])
        try:
            if serve == '24':
                assert self.return_current_url() == seller_collage['24_collage_list']
            else:
                assert self.return_current_url() == seller_collage['20_collage_list']
            log.info('集采信息列表断言判断成功')
            sleep(0.1)
            while inspect_num < limit:
                self.opera_transverse_scrollto()  # 控制滚动条滚动
                sleep(0.2)
                try:
                    inspect_element = self.driver.find_elements(By.CLASS_NAME, 'w-button-group-item')
                    log.info('当前列表共有' + str(len(inspect_element)) + '条待审核数据')
                    if len(inspect_element) >= 1:
                        inspect_element[-1].click()
                        if serve == '24':
                            assert set(opera_collage['24_collage_inspect']).issubset(set(self.return_current_url()))
                        else:
                            assert set(opera_collage['20_collage_inspect']).issubset(set(self.return_current_url()))
                        log.info('集采信息审核界面断言判断成功')
                        if inspect_type == 1:  # 1通过 2驳回
                            self.is_click(collage['collage_inspect_adopt'])
                        else:
                            self.is_click(collage['collage_inspect_reject'])
                            self.input_clear_text(collage['collage_inspect_reject_reason'], reject_reason)
                        log.info('当前审核次数 : ' + str(inspect_num) + '  预计审核次数  : ' + str(limit))
                        inspect_num += 1
                    else:
                        log.info('无审核数据')
                        self.driver.quit()
                except NoSuchElementException:
                    log.info('未找到审核按钮 无审核数据 出现异常')
                    self.fial_info()
            log.info('审核集采信息完毕,已审核 ' + str(inspect_num))
        except AssertionError:
            log.error('断言失败')
            self.fial_info()
