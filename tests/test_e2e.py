import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class TestOne:

    def test_e2e(self, setup):
        setup.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
        time.sleep(2)
        results = self.driver.find_elements(By.XPATH, "//div[@class='products']/div")

        assert len(results) > 0

        for result in results:
            result.find_element(By.XPATH, "div/button").click()  # Chaining

        self.driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

        self.driver.find_element(By.XPATH, "//button[normalize-space()='PROCEED TO CHECKOUT']").click()

        self.driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")

        self.driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "promoInfo")))

        print(self.driver.find_element(By.CLASS_NAME, "promoInfo").text)

        # SUM Validation
        prices = self.driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")

        sum = 0
        for price in prices:
            sum += int(price.text)

        print(sum)

        assert sum == int(self.driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

