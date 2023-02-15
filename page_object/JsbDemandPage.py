import allure

from common.readelement import Element
from page.webpage import WebPage
from utils.log import Log
from utils.times import sleep

demand = Element('JsbRawDemand')
log = Log()
user_demand_url = {'24_demand_list': 'http://192.168.101.24:8090/user-center/purchase-info/purchase-list',
                   '20_demand_list': 'https://demo.jinsubao.cn/user-center/purchase-info/purchase-list',
                   '24_purchase_demand': 'http://192.168.101.24:8090/user-center/purchase-info/purchase-form',
                   '24_market_information': 'http://192.168.101.24:8090/user-center/purchase-info/purchase-form',
                   '20_purchase_demand': 'https://demo.jinsubao.cn/user-center/purchase-info/purchase-form',
                   '20_market_information': 'https://demo.jinsubao.cn/user-center/purchase-info/purchase-form'}

seller_demand_url = {'24_demand_list': 'http://192.168.101.24:8070/product-manage/purchase-index/purchase-list',
                     '20_demand_list': 'https://slrdm.jinsubao.cn/product-manage/purchase-index/purchase-list',
                     '24_purchase_demand': 'http://192.168.101.24:8070/product-manage/purchase-form/1',
                     '20_purchase_demand': 'https://slrdm.jinsubao.cn/product-manage/purchase-form/1',
                     '24_market_information': 'http://192.168.101.24:8070/product-manage/purchase-form/2',
                     '20_market_information': 'https://slrdm.jinsubao.cn/product-manage/purchase-form/2'}


class JsbDemand(WebPage):

    def user_demand(self, serve, user_phone, release_type, title, content, img_path, video_path, seller_num, price,
                    num, limit, grade_number, add_type, number,circulation):
        demand_num = 1
        self.click_user_login(serve, user_phone)
        self.find_elements(demand['user_center'])[1].click()
        self.find_elements(demand['user_div_demand'])[10].click()
        sleep(0.2)
        self.find_elements(demand['user_demand_home'])[5].click()
        sleep(0.5)
        try:
            self.user_demand_judge(serve, 1)
            while demand_num <= limit:
                log.info('当前进行第' + str(demand_num) + '次添加')
                self.is_click(demand['user_demand_release'])
                self.is_click(demand['user_demand_release_agreement'])
                sleep(0.2)
                if release_type == 2:  # 市场信息
                    self.find_elements(demand['user_demand_release_type'])[0].click()
                    self.is_click(demand['user_demand_release_btn'])
                    sleep(0.2)
                    self.user_demand_judge(serve, 3)
                    self.goods_grade(grade_number, add_type, number,circulation)
                    self.user_market_information(title + '_______' + str(demand_num), content, img_path, video_path,
                                                 price,
                                                 num)
                    log.info('市场信息发布完毕')
                    sleep(0.3)
                    self.user_demand_judge(serve, 1)
                    log.info('买家供需资讯______市场信息发布成功')
                else:
                    self.is_click(demand['user_demand_release_btn'])
                    sleep(0.2)
                    self.user_demand_judge(serve, 2)
                    self.goods_grade(grade_number, add_type, number,circulation)
                    self.user_purchase_demand(title, content, img_path, video_path,
                                              seller_num,
                                              price, num)
                    # + '_______' + str(demand_num)
                    log.info('采购需求发布完毕')
                    sleep(0.3)
                    self.user_demand_judge(serve, 1)
                    log.info('买家供需资讯______采购需求发布成功')
                log.info('当前新增次数 : ' + str(demand_num) + '  预计新增次数  : ' + str(limit))
                demand_num += 1
                grade_number += 1
                log.info(
                    "----------------------------------------------------------------------------------------------")
        except:
            self.fial_info()

    def user_purchase_demand(self, title, content, img_path, video_path, seller_num, price, num):
        self.input_clear_text(demand['user_demand_title'], title)
        self.input_clear_text(demand['user_demand_content'], content)
        sleep(0.2)
        self.find_elements(demand['user_demand_upload'])[1].send_keys(img_path)
        sleep(0.5)
        # self.find_elements(demand['user_demand_upload'])[0].send_keys(video_path)
        self.input_clear_text(demand['user_demand_seller_num'], seller_num)
        self.script('5000')
        sleep(0.2)
        self.is_click(demand['user_demand_address'])
        sleep(0.2)
        self.click_area()
        self.input_clear_text(demand['user_demand_price'], price)
        self.input_clear_text(demand['user_demand_num'], num)
        self.is_click(demand['user_demand_submit'])

    def user_market_information(self, title, content, img_path, video_path, price, num):
        self.input_clear_text(demand['user_demand_title'], title)
        self.input_clear_text(demand['user_demand_content'], content)
        sleep(0.2)
        self.find_elements(demand['user_demand_upload'])[1].send_keys(img_path)
        sleep(0.5)
        self.find_elements(demand['user_demand_upload'])[0].send_keys(video_path)
        self.script('5000')
        sleep(0.2)
        self.is_click(demand['user_demand_address'])
        sleep(0.2)
        self.click_area()
        self.input_clear_text(demand['user_demand_price'], price)
        self.input_clear_text(demand['user_demand_num'], num)
        self.is_click(demand['user_demand_submit'])

    def user_demand_judge(self, serve, number):
        sleep(0.2)
        if number == 1:
            log.info('进入判断是否界面一致____供需列表')
            if serve == '24':
                assert self.return_current_url() == user_demand_url['24_demand_list']
            else:
                assert self.return_current_url() == user_demand_url['20_demand_list']
        elif number == 2:
            log.info('进入判断是否界面一致____采购需求发布')
            if serve == '24':
                assert self.return_current_url() == user_demand_url['24_purchase_demand']
            else:
                assert self.return_current_url() == user_demand_url['20_purchase_demand']
        elif number == 3:
            log.info('进入判断是否界面一致____市场信息发布')
            if serve == '24':
                assert self.return_current_url() == user_demand_url['24_market_information']
            else:
                assert self.return_current_url() == user_demand_url['20_market_information']

    def seller_demand(self, serve, seller_phone, release_type, title, content, img_path, video_path, seller_num, price,
                      num, limit,grade_number, add_type, number,circulation):
        demand_num = 1
        self.seller_phone_login(serve, seller_phone)
        self.find_elements(demand['seller_demand_home'])[0].click()
        sleep(0.2)
        self.find_elements(demand['seller_demand_list'])[4].click()
        sleep(0.5)
        try:
            self.seller_demand_judge(serve, 1)
            while demand_num <= limit:
                log.info('当前进行第' + str(demand_num) + '次添加')
                self.is_click(demand['seller_demand_release'])
                self.is_click(demand['seller_demand_release_agreement'])
                sleep(0.2)
                if release_type == 2:  # 市场信息
                    self.find_elements(demand['seller_demand_release_type'])[0].click()
                    self.is_click(demand['seller_demand_release_btn'])
                    sleep(0.2)
                    self.seller_demand_judge(serve, 3)
                    self.goods_grade(grade_number, add_type, number,circulation)
                    self.user_market_information(title + '_______' + str(demand_num), content, img_path, video_path,
                                                 price,
                                                 num)
                    log.info('市场信息发布完毕')
                    sleep(0.3)
                    self.seller_demand_judge(serve, 1)
                    log.info('卖家供需资讯______市场信息发布成功')
                else:
                    self.is_click(demand['seller_demand_release_btn'])
                    sleep(0.2)
                    self.seller_demand_judge(serve, 2)
                    self.goods_grade(grade_number, add_type, number,circulation)
                    self.user_purchase_demand(title + '_______' + str(demand_num), content, img_path, video_path,
                                              seller_num,
                                              price, num)
                    log.info('采购需求发布完毕')
                    sleep(0.3)
                    self.seller_demand_judge(serve, 1)
                    log.info('卖家供需资讯______采购需求发布成功')
                log.info('当前新增次数 : ' + str(demand_num) + '  预计新增次数  : ' + str(limit))
                demand_num += 1
                grade_number += 1
                log.info(
                    "----------------------------------------------------------------------------------------------")
        except:
            self.fial_info()

    def seller_purchase_demand(self, title, content, img_path, video_path, seller_num, price, num):
        self.input_clear_text(demand['seller_demand_title'], title)
        self.input_clear_text(demand['seller_demand_content'], content)
        sleep(0.2)
        self.find_elements(demand['seller_demand_upload'])[1].send_keys(img_path)
        sleep(0.5)
        self.find_elements(demand['seller_demand_upload'])[0].send_keys(video_path)
        self.input_clear_text(demand['seller_demand_seller_num'], seller_num)
        self.script('5000')
        sleep(0.2)
        self.is_click(demand['seller_demand_address'])
        sleep(0.2)
        self.click_area()
        self.input_clear_text(demand['seller_demand_price'], price)
        self.input_clear_text(demand['seller_demand_num'], num)
        self.is_click(demand['seller_demand_submit'])

    def seller_market_information(self, title, content, img_path, video_path, price, num):
        self.input_clear_text(demand['seller_demand_title'], title)
        self.input_clear_text(demand['seller_demand_content'], content)
        sleep(0.2)
        self.find_elements(demand['seller_demand_upload'])[1].send_keys(img_path)
        sleep(0.5)
        self.find_elements(demand['seller_demand_upload'])[0].send_keys(video_path)
        self.script('5000')
        sleep(0.2)
        self.is_click(demand['seller_demand_address'])
        sleep(0.2)
        self.click_area()
        self.input_clear_text(demand['seller_demand_price'], price)
        self.input_clear_text(demand['seller_demand_num'], num)
        self.is_click(demand['seller_demand_submit'])

    def seller_demand_judge(self, serve, number):
        if number == 1:
            log.info('进入判断是否界面一致____供需列表')
            if serve == '24':
                assert self.return_current_url() == seller_demand_url['24_demand_list']
            else:
                assert self.return_current_url() == seller_demand_url['20_demand_list']
        elif number == 2:
            log.info('进入判断是否界面一致____采购需求发布')
            if serve == '24':
                assert self.return_current_url() == seller_demand_url['24_purchase_demand']
            else:
                assert self.return_current_url() == seller_demand_url['20_purchase_demand']
        elif number == 3:
            log.info('进入判断是否界面一致____市场信息发布')
            if serve == '24':
                assert self.return_current_url() == seller_demand_url['24_market_information']
            else:
                assert self.return_current_url() == seller_demand_url['20_market_information']
