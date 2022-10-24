from selenium.webdriver.common.by import By

from common.readelement import Element
from page.webpage import WebPage
from utils.log import Log
from utils.times import sleep

opera = Element('operation')
log = Log()

opera_url = {'24_login': 'http://192.168.101.24:8050/user/login?redirect=%2Fdashboard',
             '20_login': 'https://admdm.jinsubao.cn/user/login?redirect=%2F',
             '20_home': 'https://admdm.jinsubao.cn/dashboard', '24_home': 'http://192.168.101.24:8050/dashboard'}


class JsbOperationPage(WebPage):

    def opera_end_title(self, serve):
        sleep()
        log.info('判断当前所在端是否为运营端')
        try:
            assert self.element_text(opera['运营端标题']) == '金塑宝 运营管理后台'
            log.info('标题校验成功')
            if serve == '24':
                assert self.driver.current_url == opera_url['24_login']
            else:
                assert self.driver.current_url == opera_url['20_login']
        except AssertionError:
            self.fial_info()

    def opera_login(self, serve, opera_phone):
        if serve == '24':
            self.driver.get(opera_url['24_login'])
        else:
            self.driver.get(opera_url['20_login'])
        self.opera_end_title(serve)
        self.input_text(opera['运营端登录手机号'], opera_phone)
        self.is_click(opera['运营端发送验证码'])
        self.is_click(opera['运营端点击登录'])
        try:
            if serve == '24':
                assert self.driver.current_url == opera_url['24_home']
            else:
                assert self.driver.current_url == opera_url['20_home']
            log.info('登录成功')
            log.info('登陆人姓名: ' + self.element_text(opera['运营端登陆人姓名']))
        except:
            self.fial_info()

    def opera_goods_examine(self, serve, opera_phone,code,limit):
        self.opera_login(serve, opera_phone)
        self.driver.find_element(By.XPATH, "//span[text()='运营审核']").click()
        sleep(0.5)
        self.driver.find_elements(By.CLASS_NAME, "ant-menu-item")[1].click()
        log.info('进入商品审核界面')
        if code == 1:
            self.is_click(opera['制成品审核类型'])
        sleep(0.2)
        examine = 0
        try:
            btn_examine = self.find_elements(opera['审核按钮判断存在'])
            if len(btn_examine) > 0:
                while examine < limit:
                    btn_examine = self.find_elements(opera['审核按钮判断存在'])
                    if len(btn_examine) < 0:
                        log.info('无可审核商品  退出审核测试')
                    sleep()
                    self.driver.find_elements(By.CLASS_NAME, 'ant-space-item')[2].click()
                    sleep(0.5)
                    self.script('10000')
                    self.driver.find_element(By.XPATH,
                                             "// button[@class='ant-btn ant-btn-primary']").click()
                    examine += 1
                    log.info('当前审核次数 : ' + str(examine) + '  预计审核次数  : ' + str(limit))
            else:
                log.info('暂无可审核原料')
        except:
            log.info('暂无可审核商品____退出测试')
            self.driver.quit()
