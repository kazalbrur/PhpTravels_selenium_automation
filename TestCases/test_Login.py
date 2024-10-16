import pytest

from pages.Login_POM import LoginPage
from Utilities.Logger import LogGenerator
from Utilities.ReadProperties import ReadConfig


class Test_Login_Page:
    url = ReadConfig.get_url()
    email = ReadConfig.get_email()
    pwd = ReadConfig.get_pwd()
    log = LogGenerator.log_gen()
    path = "Screenshots/"

    @pytest.mark.sanity
    def test_PageTitle_001(self, setup):
        self.driver = setup
        self.log.info("Starting test_PageTitle_001")
        self.log.info("Launching Browser")
        self.driver.get(self.url)
        self.log.info("Going to this URL-->" + self.url)
        if self.driver.title == "Administrators Login":
            self.log.info("Page Title Matched--test_PageTitle_001 is Passed")
            self.driver.save_screenshot(f"{self.path}test_PageTitle_001--Passed.png")
            self.log.info("Saving test_PageTitle_001--Passed Screenshot")
            assert True
        else:
            self.log.info("Page Title Didn't Match--test_PageTitle_001 is Failed")
            self.driver.save_screenshot(f"{self.path}test_PageTitle_001--Failed.png")
            self.log.info("Saving test_PageTitle_001--Failed Screenshot")
            assert False

    @pytest.mark.sanity
    def test_login_001(self, setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.log.info("Starting test_login_001")
        self.log.info("Launching Browser")
        self.driver.get(self.url)
        self.log.info("Going to this URL-->" + self.url)
        self.lp.enter_email(self.email)
        self.log.info("Entering Email-->" + self.email)
        self.lp.enter_pwd(self.pwd)
        self.log.info("Entering Password-->" + self.pwd)
        self.lp.click_login_button()
        self.log.info("Clicking on Login Button")
        if self.driver.title == "Dashboard":
            self.log.info("Page Title Matched--test_login_001 is Passed")
            self.driver.save_screenshot(f"{self.path}test_login_001--Passed.png")
            self.log.info("Saving test_login_001--Passed Screenshot")
            self.lp.click_menu()
            self.log.info("Clicking on Menu Button")
            self.lp.click_logout()
            self.log.info("Clicking on Logout Button")
            assert True
        else:
            self.log.info("Page Title Didn't Match--test_login_001 is Failed")
            self.driver.save_screenshot(f"{self.path}test_login_001--Failed.png")
            self.log.info("Saving test_login_001--Failed Screenshot")
            assert False
