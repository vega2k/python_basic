import unittest                 # unittest 모듈 탑재
from Chapter15 import common    # 단위테스트 대상 모듈인 common 모듈 탑재


class CommonTestCase(unittest.TestCase):    # 단위테스트용 클래스, 인자값 주의
    def test_email_validation_check(self):  # 단위테스트용 메소드
        # 단위테스트 대상 함수 호출 (False 기대)
        self.assertFalse(common.email_validation_check('#@c#o@gmail*om'))
        # 단위테스트 대상 함수 호출 (True 기대)
        self.assertTrue(common.email_validation_check('isi.cho@gmail.com'))
