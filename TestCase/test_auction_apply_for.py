import time
import allure
import pytest

from page_object.JsbAuction import JsbAuction
from utils.log import Log
from utils.tool_util import time_lag

log = Log()


@allure.feature('执行卖家申请竞拍资格')
class TestAuctionApplyFor:

    @allure.title('卖家申请竞拍资格')
    def test_auction_apply_for(self, drivers):
        log.info('当前执行   申请竞拍资格   ')
        serve = '24'
        sellerPhone= '13000000005'
        auction = JsbAuction(drivers)
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        auction.seller_auction_apply_for(serve, sellerPhone)
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_auction_apply_for.py'])
