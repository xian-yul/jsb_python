from common.readelement import Element
from page.webpage import WebPage
from utils.log import Log

collage = Element('JsbCollage')
log = Log()


class JsbCollage(WebPage):

    def seller_collage_release(self, serve, seller_phone):
        self.seller_phone_login(serve, seller_phone)

    def user_collage_place_order(self, serve, user_phone):
        self.click_user_login(serve, user_phone)
