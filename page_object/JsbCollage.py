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

opera_collage = {'24_collage_list': 'http://192.168.101.24:8050/operateManage/table',
                 '20_collage_list': 'https://admdm.jinsubao.cn/operateManage/table',
                 '24_collage_inspect': 'http://192.168.101.24:8050/operateManage/collection-info-details/',
                 '20_collage_inspect': 'https://admdm.jinsubao.cn/operateManage/collection-info-details/'}
seller_collage = {'24_collage_list': 'http://192.168.101.24:8070/centralized-purchase/table',
                  '20_collage_list': 'https://slrdm.jinsubao.cn/centralized-purchase/table',
                  '24_collage_release': 'http://192.168.101.24:8070/centralized-purchase/publish-collection-from',
                  '20_collage_release': 'https://slrdm.jinsubao.cn/centralized-purchase/publish-collection-from'}
user_collage = {'24_collage_list': 'http://192.168.101.24:8090/raw/group-purchase',
                '20_collage_list': 'https://demo.jinsubao.cn/raw/group-purchase',
                '24_collage_order_place': 'http://192.168.101.24:8090/order/pre/place', '20_collage_order_place': '',
                '24_collage_detail': 'http://192.168.101.24:8090/raw/centralized-details/',
                '20_collage_detail': 'https://demo.jinsubao.cn/raw/centralized-details/',
                '24_collage_order_pay_front_money': 'http://192.168.101.24:8090/order/pay/',
                '20_collage_order_pay_front_money': '',
                '24_collage_order_list': 'http://192.168.101.24:8090/user-center/my-order-list',
                '20_collage_order_list': ''}


class JsbCollage(WebPage):

    def seller_collage_release(self, serve, seller_phone, minimum, add_type, circulation, goodsNumber,
                               delivery_method, collage_num, overflow_num, delivery_day, delivery_price,
                               deposit, describe, limit, brand, start_time, end_time):
        add_num = 0
        self.seller_phone_login(serve, seller_phone)
        self.is_click(collage['collage_seller_li'])
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
                # self.find_elements(collage['collage_contract'])[0].click()
                # sleep(0.1)
                # self.find_elements(collage['collage_contract_li'])[-1].click()
                self.input_clear_text(collage['collage_purchaseNum'], collage_num)
                self.input_clear_text(collage['collage_overflow'], overflow_num)
                self.script('10000')
                if delivery_method == 1:  # 集采交货方式判断   1配送
                    self.input_clear_text(collage['collage_deliveryPrice'], delivery_price)
                    self.is_click(collage['collage_deliveryAreaName'])
                    sleep(0.1)
                    self.is_click(collage['collage_deliveryAreaName_whole'])
                    self.is_click(collage['collage_deliveryAreaName_btn'])
                else:
                    self.find_elements(collage['collage_deliver_method'])[1].click()
                    self.input_clear_text(collage['collage_selfMentionPrice'], delivery_price)
                self.input_clear_text(collage['collage_deliveryDays'], delivery_day)
                self.input_clear_text(collage['collage_handlesRate'], deposit)
                self.find_elements(collage['collage_start_time'])[0].click()
                sleep(0.1)
                collage_time = self.find_elements(collage['collage_start_time_start'])
                collage_time[0].send_keys(start_time)
                # self.inputs_clear_text(collage['collage_start_time_start'], 0, start_time)
                sleep(0.1)
                collage_time[1].send_keys(end_time)
                # self.inputs_clear_text(collage['collage_start_time_end'], 1, end_time)
                # self.is_click(collage['collage_start_time_btn']) #..集采选择日期有问题
                self.is_click(collage['collage_remark'])
                self.input_clear_text(collage['collage_remark'], describe)
                sleep(0.2)
                self.find_elements(collage['collage_submit_btn'])[0].click()
                sleep(0.3)
                log.info('当前新增次数 : ' + str(add_num) + '  预计新增次数  : ' + str(limit))
                add_num += 1
                goodsNumber += 1
                sleep(0.2)
                if serve == '24':
                    assert self.return_current_url() == seller_collage['24_collage_list']
                else:
                    assert self.return_current_url() == seller_collage['20_collage_list']
                log.info('集采信息发布后界面断言判断成功')
            log.info('新增集采信息完毕,已新增 ' + str(add_num))
        except AssertionError:
            log.error('断言失败')
            self.fial_info()

    def user_collage_place_order(self, serve, user_phone, purchase_num, purchase_goods, limit):
        collage_limit = 0
        self.click_user_login(serve, user_phone)
        while collage_limit < limit:
            if collage_limit > 0:
                self.find_elements(collage['collage_market_li'])[1].click()
            else:
                self.find_elements(collage['collage_market_li'])[0].click()
            sleep(0.1)
            self.find_elements(collage['collage_menu'])[1].click()
            sleep(0.2)
            try:
                if serve == '24':
                    assert self.return_current_url() == user_collage['24_collage_list']
                else:
                    assert self.return_current_url() == user_collage['20_collage_list']
                log.info('集采信息列表界面断言成功')
                sleep(0.1)
                # self.find_elements(collage['collage_status'])[1].click()
                # sleep(0.2) #状态筛选
                # self.is_click(collage['collage_status_li'])
                self.input_clear_text(collage['collage_search_text'], purchase_goods)
                sleep(0.1)
                self.is_click(collage['collage_search_btn'])
                log.info('搜索商品名称 : ' + purchase_goods)
                sleep(0.1)
                flag = self.getElementExistance(collage['collage_goods'])
                sleep(0.2)
                if flag:
                    collage_goods = self.find_elements(collage['collage_goods'])
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
                    log.info(
                        f'当前集采最低采购为 :{lowest_num}吨, 剩余集采量为 :{surplus_num}吨'.format(lowest_num,
                                                                                                    surplus_num))
                    if purchase_num > int(lowest_num):
                        self.input_clear_text(collage['collage_buy_num'], purchase_num)
                    else:
                        self.input_clear_text(collage['collage_buy_num'], int(lowest_num))
                    if purchase_num > int(surplus_num):
                        self.input_clear_text(collage['collage_buy_num'], int(surplus_num))
                    sleep(0.1)
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
                    sleep(0.1)
                    if serve == '24':
                        assert self.return_current_url == user_collage['24_collage_order_list']
                    else:
                        assert self.return_current_url == user_collage['24_collage_order_list']
                    log.info('跳转到订单列表断言成功')
                    log.info('进行签署集采合同')
                    self.is_click(collage['collage_order_sign'])
                    self.find_elements(collage['collage_sign_btn'])[-1].click()
                    self.signing_contract()
                    self.find_elements(collage['collage_order_pay_front_money'])[0].click()
                    sleep(0.1)
                    log.info('进入集采支付定金页面')
                    if serve == '24':
                        assert set(user_collage['24_collage_order_pay_front_money']).issubset(
                            set(self.return_current_url()))
                    else:
                        assert set(user_collage['24_collage_order_pay_front_money']).issubset(
                            set(self.return_current_url()))
                    log.info('支付定金页面断言成功')
                    self.input_clear_text(collage['collage_pay_password'], 666666)
                    self.is_click(collage['collage_pay_btn'])
                    sleep()
                    log.info(
                        f'当前下单次数 : {collage_limit}, 预计下单次数{limit}'.format(str(collage_limit), str(limit)))
                    collage_limit += 1
                else:
                    log.info('当前无集采商品可进行下单操作')
                    self.driver.quit()
            except Exception as e:
                log.error(e)
                self.fial_info()
            log.info('执行完毕')

    def opera_collage_inspect(self, serve, opera_phone, inspect_type, reject_reason, limit):
        inspect_num = 0
        self.opera_login(serve, opera_phone)
        self.is_click(collage['collage_li'])
        self.is_click(collage['collage_info_li'])
        try:
            if serve == '24':
                assert self.return_current_url() == opera_collage['24_collage_list']
            else:
                assert self.return_current_url() == opera_collage['20_collage_list']
            log.info('集采信息列表断言判断成功')
            sleep(0.1)
            while inspect_num < limit:
                self.opera_transverse_scrollto()  # 控制滚动条滚动
                sleep(0.2)
                try:
                    inspect_element = self.driver.find_elements(By.CLASS_NAME, 'w-button-group-item')
                    log.info(f'当前列表共有{inspect_element}条待审核数据'.format(str(len(inspect_element))))
                    if len(inspect_element) >= 1:
                        inspect_element[-1].click()
                        sleep(0.1)
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
                        log.info(f'当前审核次数 : {inspect_num} , 预计审核次数 : {limit}'.format(str(inspect_num),
                                                                                                 str(limit)))
                        inspect_num += 1
                    else:
                        log.info('无审核数据')
                        self.driver.quit()
                except NoSuchElementException:
                    log.info('未找到审核按钮 无审核数据 出现异常')
                    self.fial_info()
            log.info(f'审核集采信息完毕,已审核 {inspect_num}'.format(str(inspect_num)))
        except AssertionError:
            log.error('断言失败')
            self.fial_info()
