from common.readelement import Element
from page.webpage import WebPage
from utils.log import Log
from utils.times import sleep

log = Log()
auction = Element('JsbAuction')
auction_url = {'24_auction_apply_from': 'http://192.168.101.24:8070/competitive-auction/auct-apply-form',
               '24_auction_list': 'http://192.168.101.24:8070/competitive-auction/auct-apply', '20_auction_list': '',
               '20_auction_apply_from': ''}


class JsbAuction(WebPage):
    def seller_auction_apply_for(self, serve, sellerPhone):
        self.seller_phone_login(serve, sellerPhone)
        self.is_click(auction['auction_li'])
        sleep(0.1)
        self.is_click(auction['auction_apply_for'])
        self.is_click(auction['auction_agreement_ipt'])
        self.is_click(auction['auction_submit_btn'])
        log.info('提交竞拍申请')

    def seller_auction(self, serve, grade_number, add_type, number, circulation, sellerPhone, grossQuantity,
                       startQuantity, quantityIncrease, maxQuotationUnit, startUnitPrice, upPrice, maxUpPrice,
                       start_time, end_time, buyerSuretyRatio, deliveryTime, additionalProvisions, is_vehicle,
                       vehicle_stock, delivery_type, limit):
        self.seller_phone_login(serve, sellerPhone)
        self.is_click(auction['auction_li'])
        self.is_click(auction['auction_content'])
        sleep(0.1)
        try:
            if serve == '24':
                assert self.return_current_url() == auction_url['24_auction_list']
            else:
                assert self.return_current_url() == auction_url['20_auction_list']
            log.info('进入竞拍内容列表  断言成功')
        except AssertionError:
            log.error('竞拍内容列表 断言失败')
            self.fial_info()
        add_num = 1
        while add_num <= limit:
            self.find_elements(auction['auction_add_btn'])[1].click()
            sleep(0.3)
            try:
                if serve == '24':
                    assert self.return_current_url() == auction_url['24_auction_apply_from']
                else:
                    assert self.return_current_url() == auction_url['20_auction_apply_from']
                log.info('进入发布竞拍界面  断言成功')
            except AssertionError:
                log.error('发布竞拍界面 断言失败')
                self.fial_info()
            if is_vehicle == 1:
                self.is_click(auction['auction_switch_vehicle'])
                self.input_clear_text(auction['auction_vehicle_stock'], vehicle_stock)
            self.goods_grade(grade_number, add_type, number, circulation)
            self.input_clear_text(auction['auction_grossQuantity_ipt'], grossQuantity)
            if delivery_type == 1:
                self.is_click(auction['auction_deliveryAreaName'])
                self.is_click(auction['auction_deliveryAreaName_whole'])
                self.find_elements(auction['auction_deliveryAreaName_determine'])[1].click()
            else:
                self.find_elements(auction['auction_drop_down_select'])[0].click()
                self.find_elements(auction['auction_delivery_type'])[0].click()
            self.input_clear_text(auction['auction_startQuantity_ipt'], startQuantity)
            self.input_clear_text(auction['auction_quantityIncrease_ipt'], quantityIncrease)
            self.input_clear_text(auction['auction_maxQuotationUnit_ipt'], maxQuotationUnit)
            self.input_clear_text(auction['auction_startUnitPrice_ipt'], startUnitPrice)
            self.input_clear_text(auction['auction_upPrice_ipt'], upPrice)
            self.input_clear_text(auction['auction_maxUpPrice_ipt'], maxUpPrice)
            auction_time = self.find_elements(auction['auction_time_start'])
            auction_time[0].click()
            sleep(0.1)
            self.find_elements(auction['auction_time_start_select'])[3].click()
            sleep(0.1)
            self.is_click(auction['auction_time_ok_btn'])
            auction_time[1].click()
            sleep(0.1)
            self.find_elements(auction['auction_time_start_select'])[2].click()
            sleep(0.1)
            self.is_click(auction['auction_time_ok_btn'])
            sleep(0.1)
            self.input_clear_text(auction['auction_buyerSuretyRatio_ipt'], buyerSuretyRatio)
            self.input_clear_text(auction['auction_deliveryTime_ipt'], deliveryTime)
            self.script('200')
            self.input_clear_text(auction['auction_additionalProvisions_textarea'], additionalProvisions)
            self.is_click(auction['auction_submit_btn'])
            sleep(0.1)
            try:
                if serve == '24':
                    assert self.return_current_url() == auction_url['24_auction_list']
                else:
                    assert self.return_current_url() == auction_url['20_auction_list']
                log.info('竞拍内容发布成功  断言成功')
            except AssertionError:
                log.error('竞拍内容发布 断言失败')
                self.fial_info()
            log.info(f'当前添加次数 {add_num}次, 预计添加次数 {limit}次'.format(add_num, limit))
            add_num += 1
            grade_number += 1
        log.info('竞拍内容发布完毕')
