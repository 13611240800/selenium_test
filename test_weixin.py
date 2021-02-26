import json
from time import sleep

from selenium import webdriver


class TestWeixin:
    def setup(self):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=chrome_arg)
        # chrome - -remote - debugging - port = 9222
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_login_weixin(self):
        '''
        基于复用浏览器后的基本操作，对调试程序用处大
        :return:
        '''
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        # self.driver.find_element_by_xpath('//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        # self.driver.find_element_by_xpath('//*[@id="wework_admin.loginpage_wx_$"]/main/div[2]/a').click()
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()
        self.driver.find_element_by_xpath('//*[@id="member_list"]/tr/td[1]/input').click()
        self.driver.find_element_by_xpath('//*[@id="js_contacts48"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]').click()
        sleep(3)
        # //*[@id="js_contacts48"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]
        self.driver.find_element_by_xpath('//*[@id="js_contacts49"]/div/div[1]/div/div[1]/a/i').click()
        self.driver.find_element_by_xpath('//*[@id="js_contacts49"]/div/div[1]/ul/li[1]/a').click()
        self.driver.find_element_by_xpath('//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[1]/input').send_keys(
            'ww2')
        self.driver.find_element_by_xpath(
            '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[3]/a/span[2]').click()
        self.driver.find_element_by_xpath('//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[3]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]').click()

    def test_safe_cookie(self):
        '''
        存入cookie
        :return:
        '''
        cookie = self.driver.get_cookies()
        with open('cookiefile.txt', 'w', encoding='utf-8') as f:
            json.dump(cookie, f)

    def test_cookie_login(self):
        '''
        利用cookie进行登录
        :return:
        '''
        # 1.拿到登陆后的cookie，登陆前的cookie没用
        # 2.浏览器处于复用状态
        # cookie=self.driver.get_cookies()
        # print(cookie)
        # 3.拿到cookie后，可以不用复用浏览器来登录.cookie有超时时间，不是总有效，需要和开发约定好
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')
        # cookie=[{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'neaRBdr32Us8RSAxVeYoCQja_r3Z5swYrPFcktwk3w7SzsK_4Q-oHlmpT2jaJfUj26Pvj_ecAFvZ_VELOfb4CaSVplmVemmZyBB-a2DOp_FCOIFajSG3pQEMZ13ltC7k3X1KDENp4VQpfIoXMdKj_fscBxFGBgel4xIxF4du7Menb6BjA51pWWPJSP5l-FTeL0gGP5JYy6MipJAcwfjmiu89rAssrTWJunJeOa1l0qrUCwAiYwSz-IUehADGcSBSLUzyotjamBkHjKkrZ9vX4A'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688854058555305'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688854058555305'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325058090305'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 't-rwvWNEj0aYFNUbJnfa6QIkTDVdn217YAmZq4WbVIm7bf-RFe3V3vRLEZjD5D9R'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a7844880'}, {'domain': 'work.weixin.qq.com', 'expiry': 1614328094, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '5l7nm0f'}, {'domain': '.qq.com', 'expiry': 1614407361, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1718644946.1614257101'}, {'domain': '.qq.com', 'expiry': 1677392961, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.528056376.1614257101'}, {'domain': '.work.weixin.qq.com', 'expiry': 1645792926, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1645852681, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1614257100,1614316682'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '4979417036'}, {'domain': '.work.weixin.qq.com', 'expiry': 1616914246, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1614316682'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '21118062471077703'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '5701655552'}, {'domain': '.qq.com', 'expiry': 2147483652, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'fb7f4148901f753ebd857f83f9337b118b08fbd9c38a2523b004cf78d4db905d'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'ZGQY206WPe'}]
        # 读取cookie
        with open('cookiefile.txt', 'r', encoding='utf-8') as f:
            cookie = json.load(f)
        for i in cookie:
            self.driver.add_cookie(i)
        self.driver.refresh()
