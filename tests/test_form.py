import time

import pytest
from selenium.webdriver.support.select import Select

from data.homepage_form_data import FormData
from pages.HomePage import HomePage
from util.BaseClass import BaseClass


class TestForm(BaseClass):
    def test_form_submission(self, get_data):
        homepage = HomePage(self.driver)
        homepage.get_name().send_keys(get_data["name"])
        homepage.get_email().send_keys(get_data["email"])
        homepage.get_checkbox().click()
        self.select_by_text(homepage.get_gender(), get_data["gender"])
        time.sleep(2)
        homepage.form_submit().click()
        time.sleep(5)
        submit_msg = homepage.get_success_message().text
        assert "Success" in submit_msg
        self.driver.refresh()

    # 1. Tuple = ()
    # 아래처럼 튜플 형태로 parameter를 입력할 경우 get_data[0], get_data[1] 같이 인덱스로 값 접근 가능
    # @pytest.fixture(params=[("Jake", "kimi@email.com", "Male"), ("Jodie", "jodie@email.com", "Female")])
    # def get_data(self, request):
    #     return request.param

    # 2. Dictionary = {} / 별도로 데이터 관리하는 파일 생성해서 호출
    @pytest.fixture(params=FormData.form_params)
    def get_data(self, request):
        return request.param
