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
user_collage = {'24_collage_list': 'http://192.168.101.24:8090/raw/groupPurchase', '20_collage_list': '',
                '24_collage_order_place': 'http://192.168.101.24:8090/order/pre/place', '20_collage_order_place': '',
                '24_collage_detail': 'http://192.168.101.24:8090/raw/centralizedDetails', '20_collage_detail': ''}


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
                if delivery_method == 1:  # 集采交货方式判断   1配送
                    self.input_clear_text(collage['collage_deliveryPrice'], delivery_price)
                else:
                    self.find_elements(collage['collage_deliver_method'])[1].click()
                    self.input_clear_text(collage['collage_selfMentionPrice'], delivery_price)
                self.input_clear_text(collage['collage_deliveryDays'], delivery_day)
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
        collage_limit = 0
        self.click_user_login(serve, user_phone)
        self.find_elements(collage['collage_market_li'])[0].click()
        self.find_elements(collage['collage_menu'])[1].click()
        sleep(0.2)
        try:
            if serve == '24':
                assert self.return_current_url() == user_collage['24_collage_list']
            else:
                assert self.return_current_url() == user_collage['20_collage_list']
            log.info('集采信息列表界面断言成功')
            sleep(0.1)
            self.input_clear_text(collage['collage_search_text'], purchase_goods)
            sleep(0.1)
            self.is_click(collage['collage_search_btn'])
            log.info('搜索商品名称 : ' + purchase_goods)
            sleep(0.1)
            collage_goods = self.find_elements(collage['collage_goods'])
            if len(collage_goods) > 0:
                log.info('集采商品数量共有' + str(len(collage_goods)) + "个")
                collage_goods[0].click()
                self.win_handles('-1')
                sleep(0.5)
                if serve == '24':
                    assert set(user_collage['24_collage_detail']).issubset(set(self.return_current_url()))
                else:
                    assert set(user_collage['20_collage_detail']).issubset(set(self.return_current_url()))
                log.info('集采信息详情界面断言成功')
                lowest_num = self.find_elements(collage['collage_detail_number'])[0].text
                lowest_num = lowest_num[:-1]  # 得到的值为 3吨  通过截取 取到 3
                surplus_num = self.find_element(collage['collage_surplus_num']).text
                surplus_num = surplus_num[6:-2]  # 得到的值为 （剩余集采：988吨）  通过截取 取到 998
                if purchase_num > int(lowest_num):
                    self.input_clear_text(collage['collage_buy_num'], purchase_num)
                else:
                    self.input_clear_text(collage['collage_buy_num'], int(lowest_num))
                if purchase_num > int(surplus_num):
                    self.input_clear_text(collage['collage_buy_num'], int(surplus_num))
                self.is_click(collage['collage_order_place'])  # 点击一键集采
                sleep()
                if serve == '24':
                    assert self.return_current_url() == user_collage['24_collage_order_place']
                else:
                    assert self.return_current_url() == user_collage['20_collage_order_place']
                log.info('集采确认订单界面断言成功')
                self.script('10000')
                if self.find_element(collage['collage_order_affirm']).is_enabled():
                    self.is_click(collage['collage_order_affirm'])
                else:
                    while not self.find_element(collage['collage_order_affirm']).is_enabled():
                        sleep(3)
                        if self.find_element(collage['collage_order_affirm']).is_enabled():
                            sleep(0.2)
                            self.is_click(collage['collage_order_affirm'])
                            log.info('订单提交')
                            break
                collage_limit += 1
            else:
                log.info('当前无集采商品可进行下单操作')
        except Exception as e:
            log.error(e)
            self.fial_info()

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
