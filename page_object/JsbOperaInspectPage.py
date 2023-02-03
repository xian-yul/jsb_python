from common.readelement import Element
from page.webpage import WebPage
from utils.log import Log
from utils.times import sleep

inspect = Element('JsbOperaInspect')
log = Log()


class JsbOperaInspect(WebPage):

    def opera_inspect_goods(self, serve, opera_phone, inspect_type, limit):
        log.info('当前进入   运营商品审核')
        inspect_num = 1
        self.opera_skip_inspect(serve, opera_phone)
        self.find_elements(inspect['opera_list_inspect'])[0].click()
        sleep(0.2)
        if inspect_type == 2:
            log.info('进入制成品审核')
            self.find_elements(inspect['opera_goods_inspect_type'])[3].click()
        elif inspect_type == 3:
            log.info('进入船货审核')
            self.find_elements(inspect['opera_goods_inspect_type'])[5].click()
        try:
            btn_examine = self.find_elements(inspect['opera_list_inspect_btn'])
            if len(btn_examine) > 0:
                while inspect_num <= limit:
                    sleep(0.2)
                    self.find_elements(inspect['opera_list_inspect_btn'])[0].click()
                    sleep(0.2)
                    log.info('当前审核原料名称为: ' + self.find_elements(inspect['opera_goods_title'])[0].text)
                    self.script('10000')
                    self.is_click(inspect['opera_goods_inspect_btn'])
                    log.info('当前审核次数 : ' + str(inspect_num) + '  预计审核次数  : ' + str(limit))
                    inspect_num += 1
                    log.info('-------------------------------------------------------------------')
            else:
                log.info('暂无可审核原料')
            log.info('商品审核完毕')
        except:
            log.info('暂无可审核商品____退出测试')
            self.driver.quit()

    def opera_inspect_demand(self, serve, opera_phone, inspect_type, limit):
        log.info('当前进入   运营供需审核')
        inspect_num = 1
        self.opera_skip_inspect(serve, opera_phone)
        self.find_elements(inspect['opera_list_inspect'])[1].click()
        sleep(0.2)
        if inspect_type == 1:
            self.find_elements(inspect['opera_demand_inspect_type'])[3].click()
        try:
            btn_examine = self.find_elements(inspect['opera_list_inspect_btn'])
            if len(btn_examine) > 0:
                while inspect_num <= limit:
                    sleep(0.2)
                    self.find_elements(inspect['opera_list_inspect_btn'])[0].click()
                    sleep(0.2)
                    self.script('10000')
                    sleep(5)
                    self.find_elements(inspect['opera_demand_inspect_btn'])[1].click()
                    log.info('当前审核次数 : ' + str(inspect_num) + '  预计审核次数  : ' + str(limit))
                    inspect_num += 1
                    log.info('-------------------------------------------------------------------')
            else:
                log.info('暂无可审核供需')
            log.info('供需审核完毕')
        except:
            log.info('暂无可审核供需____退出测试')
            self.driver.quit()

    def opera_inspect_shop(self, serve, opera_phone, limit):
        log.info('当前进入   运营店铺审核')
        self.opera_skip_inspect(serve, opera_phone)
        self.find_elements(inspect['opera_list_inspect'])[2].click()

    def opera_inspect_wallet(self, serve, opera_phone, limit):
        log.info('当前进入   运营钱包审核')
        self.opera_skip_inspect(serve, opera_phone)
        self.find_elements(inspect['opera_list_inspect'])[3].click()

    def opera_inspect_industry(self, serve, opera_phone, limit):
        log.info('当前进入   运营产学融合审核')
        self.opera_skip_inspect(serve, opera_phone)
        self.find_elements(inspect['opera_list_inspect'])[4].click()

    def opera_inspect_consulting(self, serve, opera_phone, limit):
        log.info('当前进入   运营法律咨询审核')
        self.opera_skip_inspect(serve, opera_phone)
        self.find_elements(inspect['opera_list_inspect'])[5].click()

    def opera_skip_inspect(self, serve, opera_phone):
        self.opera_login(serve, opera_phone)
        self.find_elements(inspect['opera_list'])[4].click()
        sleep(0.2)

    def opera_inspect(self, serve, opera_phone, inspect_type, choice_type, limit):
        if choice_type == 1:
            self.opera_inspect_goods(serve, opera_phone, inspect_type, limit)
        elif choice_type == 2:
            self.opera_inspect_demand(serve, opera_phone, inspect_type, limit)
        elif choice_type == 3:
            self.opera_inspect_shop(serve, opera_phone, limit)
        elif choice_type == 4:
            self.opera_inspect_wallet(serve, opera_phone, limit)
        elif choice_type == 5:
            self.opera_inspect_industry(serve, opera_phone, limit)
        elif choice_type == 6:
            self.opera_inspect_consulting(serve, opera_phone, limit)
