from common.readelement import Element
from page.webpage import WebPage
from utils.log import Log
from utils.times import sleep
from utils.tool_util import random_number

register = Element('JsbUserRegister')
log = Log()

user_register = {'24_home': 'http://192.168.101.24:8090/shop/home', '20_home': 'https://demo.jinsubao.cn/',
                 '24_register': 'http://192.168.101.24:8090/user/register',
                 '20_register': 'https://demo.jinsubao.cn/user/register'}


class JsbUserRegister(WebPage):

    def user_register(self, serve, limit,phone,name):
        register_num = 1
        if serve == '24':
            self.driver.get(user_register['24_home'])
        else:
            self.driver.get(user_register['20_home'])
        sleep(0.2)
        while register_num <= limit:
            try:
                phone = '189' + random_number(8)
                name = '测试账号' + random_number(4)
                self.is_click(register['register_start'])
                log.info('点击免费注册按钮')
                sleep(0.3)
                self.win_handles('-1')
                sleep(0.1)
                if serve == '24':
                    assert self.return_current_url() == user_register['24_register']
                else:
                    sleep(0.2)
                    assert self.return_current_url() == user_register['20_register']
                log.info('注册断言判断成功,进行注册操作')
                self.input_clear_text(register['register_phone'], phone)
                self.input_clear_text(register['register_name'], name)
                self.is_click(register['register_code'])
                sleep(0.1)
                self.input_clear_text(register['register_code_text'], 666666)
                self.is_click(register['register_agreement'])
                self.is_click(register['register_btn'])
                log.info('提交注册')
                sleep(0.1)
                self.win_handles('-1')
                sleep(0.4)
                log.info('提示领取新人券弹窗 刷新跳过')
                self.refresh()
                self.is_click(register['register_over'])
                log.info('退出登录')
                # log.info('当前注册次数 : ' + str(register_num) + "  目标注册 :" + str(limit))
                log.info('当前注册次数 : {register_num} , 目标注册 : {limit}'.format(register_num=str(register_num),
                                                                                     limit=str(limit)))
                register_num += 1
            except AssertionError:
                log.error('断言判断错误')
                self.fial_info()
        log.info('注册完成')
