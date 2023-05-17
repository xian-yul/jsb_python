from common.readelement import Element
from page.webpage import WebPage
from utils.log import Log
from utils.times import sleep

log = Log()
auction = Element('JsbAuction')


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
                       start_time, end_time, buyerSuretyRatio, deliveryTime, additionalProvisions):
        self.seller_phone_login(serve, sellerPhone)
        self.is_click(auction['auction_li'])
        self.is_click(auction['auction_content'])
        sleep(0.1)
        self.find_elements(auction['auction_add_btn'])[1].click()
        self.goods_grade(grade_number, add_type, number, circulation)
        self.input_clear_text(auction['auction_grossQuantity_ipt'], grossQuantity)
        self.is_click(auction['auction_deliveryAreaName'])
        self.is_click(auction['auction_deliveryAreaName_whole'])
        self.find_elements(auction['auction_deliveryAreaName_determine'])[1].click()
        self.input_clear_text(auction['auction_startQuantity_ipt'], startQuantity)
        self.input_clear_text(auction['auction_quantityIncrease_ipt'], quantityIncrease)
        self.input_clear_text(auction['auction_maxQuotationUnit_ipt'], maxQuotationUnit)
        self.input_clear_text(auction['auction_startUnitPrice_ipt'], startUnitPrice)
        self.input_clear_text(auction['auction_upPrice_ipt'], upPrice)
        self.input_clear_text(auction['auction_maxUpPrice_ipt'], maxUpPrice)
        auction_time = self.find_elements(auction['auction_time_start'])
        auction_time[0].send_keys(start_time)
        sleep(0.1)
        auction_time[1].send_keys(end_time)
        sleep(0.1)
        self.input_clear_text(auction['auction_buyerSuretyRatio_ipt'], buyerSuretyRatio)
        self.input_clear_text(auction['auction_deliveryTime_ipt'], deliveryTime)
        self.input_clear_text(auction['auction_additionalProvisions_textarea'], additionalProvisions)
        self.is_click(auction['auction_submit_btn'])
