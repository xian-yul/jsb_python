from common.readelement import Element
from page.webpage import WebPage
from utils.log import Log
from utils.times import sleep
from utils.tool_util import random_number

register = Element('JsbUserConsignmentLetter')
log = Log()


class JsbUserConsignmentLetter(WebPage):

    def user_sign_entrust(self, serve, seller_phone, user_phone, limit):
        log.info()
