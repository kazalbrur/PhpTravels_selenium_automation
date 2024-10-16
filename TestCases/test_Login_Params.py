import time

import pytest

from pages.Login_POM import LoginPage
from Utilities.Logger import LogGenerator
from Utilities.ReadProperties import ReadConfig


class Test_Login_Page_Param:
    url = ReadConfig.get_url()
    path = "Screenshots/"

    @pytest.mark.regression
    def test_login_param_001(self, setup, getDataForLogin):
        self.driver = setup
        self.log = LogGenerator.log_gen()
        self.lp = LoginPage(self.driver)
        self.log.info("Starting test_login_param_001")
        self.log.info("Launching Browser")
        self.driver.get(self.url)
        self.log.info("Going to this URL-->" + self.url)
        self.lp.enter_email(getDataForLogin[0])
        self.log.info("Entering Email-->" + getDataForLogin[0])
        self.lp.enter_pwd(getDataForLogin[1])
        self.log.info("Entering Password-->" + getDataForLogin[1])
        self.lp.click_login_button()
        self.log.info("Clicking on Login Button")

        status_list = []
        time.sleep(2)
        if self.driver.title == "Dashboard":
            if getDataForLogin[2] == "Pass":
                self.log.info("Page Title Matched--test_login_param_001 is Passed")
                self.driver.save_screenshot(f"{self.path}test_login_param_001--Passed.png")
                self.log.info("Saving test_login_param_001--Passed Screenshot")
                status_list.append("Pass")
                self.lp.click_menu()
                self.log.info("Clicking on Menu Button")
                self.lp.click_logout()
                self.log.info("Clicking on Logout Button")
            elif getDataForLogin[2] == "Fail":
                self.log.info("Page Title Didn't Match--test_login_param_001 is Failed")
                self.driver.save_screenshot(f"{self.path}test_login_param_001--Failed.png")
                self.log.info("Saving test_login_param_001--Failed Screenshot")
                status_list.append("Fail")
        else:
            if getDataForLogin[2] == "Pass":
                self.log.info("Page Title Didn't Match--test_login_param_001 is Failed")
                self.driver.save_screenshot(f"{self.path}test_login_param_001--Failed.png")
                self.log.info("Saving test_login_param_001--Failed Screenshot")
                status_list.append("Fail")
            elif getDataForLogin[2] == "Fail":
                self.log.info("Page Title Matched--test_login_param_001 is Passed")
                self.driver.save_screenshot(f"{self.path}test_login_param_001--Passed.png")
                self.log.info("Saving test_login_param_001--Passed Screenshot")
                status_list.append("Pass")
        if "Fail" not in status_list:
            self.log.info("test_login_param_001 is Passed")
            assert True
        else:
            self.log.info("test_login_param_001 is Failed")
            assert False
        self.log.info("test_login_param_001 is Completed")
