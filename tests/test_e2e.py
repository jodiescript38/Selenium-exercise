import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.CheckoutPage import CheckoutPage
from pages.HomePage import HomePage
from util.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()

        homePage = HomePage(self.driver)
        homePage.shop_items().click()

        checkoutPage = CheckoutPage(self.driver)
        cards = checkoutPage.get_card_titles()

        log.info("Load all product cards...")

        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(f"Card: {cardText}")
            if cardText == "Blackberry":
                checkoutPage.get_card_footer()[i].click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

        time.sleep(2)
        confirmPage = checkoutPage.checkout_items()
        time.sleep(2)
        self.driver.find_element(By.ID, "country").send_keys("ind")
        time.sleep(2)

        self.verify_link_presence("India")
        log.info("END OF TEST.")



