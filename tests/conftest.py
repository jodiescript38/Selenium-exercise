import os

import pytest
import pytest_html
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    driver.get("https://rahulshettyacademy.com/angularpractice")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # driver = item.funcargs.get("driver")
        driver = getattr(item.instance, "driver", None)

        print(driver.current_url)

        if driver:
            print("###### DRIVER EXISTS")
            os.makedirs("reports/screenshots", exist_ok=True)

            file_name = f"reports/screenshots/{item.name}.png"
            driver.save_screenshot(file_name)

            extra = getattr(report, "extra", [])
            extra.append(pytest_html.extras.image(f"screenshots/{item.name}.png"))
            report.extra = extra