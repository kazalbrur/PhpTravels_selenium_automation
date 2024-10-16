import time

import pytest

from pages.Login_POM import LoginPage
from Utilities import XLutils
from Utilities.Logger import LogGenerator
from Utilities.ReadProperties import ReadConfig
from Utilities.XLutils import getRowCount


class Test_Login_Page_DDT:
    url = ReadConfig.get_url()
    xlpath = "TestData/LoginScenarios.xlsx"
    sspath = "Screenshots/"
    log = LogGenerator.log_gen()

    @pytest.mark.regression
    def test_login_ddt_001(self, setup):
        self.driver = setup
        self.log.info("Starting test_login_ddt_001")
        self.log.info("Launching Browser")
        self.lp = LoginPage(self.driver)
        self.rowcount = getRowCount(self.xlpath, "Sheet1")
        self.driver.get(self.url)
        self.log.info("Going to this URL-->" + self.url)

        status_list = []
        for row in range(2, self.rowcount + 1):
            self.email = XLutils.readData(self.xlpath, "Sheet1", row, 2)
            self.pwd = XLutils.readData(self.xlpath, "Sheet1", row, 3)
            self.expected_result = XLutils.readData(self.xlpath, "Sheet1", row, 4)
            self.scenario = XLutils.readData(self.xlpath, "Sheet1", row, 6)
            self.lp.enter_email(self.email)
            self.log.info("Entering Email-->" + self.email)
            self.lp.enter_pwd(self.pwd)
            self.log.info("Entering Password-->" + self.pwd)
            self.lp.click_login_button()
            self.log.info("Clicking on Login Button")
            time.sleep(3)
            if self.driver.title == "Dashboard":
                if self.expected_result == "Pass":
                    XLutils.writeData(self.xlpath, "Sheet1", row, 5, "Pass")
                    status_list.append("Pass")
                    self.log.info("Page Title Matched--test_login_ddt_001 is Passed")
                    self.driver.save_screenshot(f"{self.sspath}test_login_ddt_001--{self.scenario}--Passed.png")
                    self.log.info("Saving test_login_ddt_001--Passed Screenshot")
                    self.lp.click_menu()
                    self.log.info("Clicking on Menu Button")
                    self.lp.click_logout()
                    self.log.info("Clicking on Logout Button")
                elif self.expected_result == "Fail":
                    XLutils.writeData(self.xlpath, "Sheet1", row, 5, "Fail")
                    status_list.append("Fail")
                    self.log.info("Page Title Matched--test_login_ddt_001 is Failed")
                    self.driver.save_screenshot(f"{self.sspath}test_login_ddt_001--{self.scenario}--Failed.png")
                    self.log.info("Saving test_login_ddt_001--Failed Screenshot")
            else:
                if self.expected_result == "Pass":
                    XLutils.writeData(self.xlpath, "Sheet1", row, 5, "Fail")
                    status_list.append("Fail")
                    self.log.info("Page Title Didn't Match--test_login_ddt_001 is Failed")
                    self.driver.save_screenshot(f"{self.sspath}test_login_ddt_001--{self.scenario}--Failed.png")
                    self.log.info("Saving test_login_ddt_001--Failed Screenshot")
                elif self.expected_result == "Fail":
                    XLutils.writeData(self.xlpath, "Sheet1", row, 5, "Pass")
                    status_list.append("Pass")
                    self.log.info("Page Title Didn't Match--test_login_ddt_001 is Passed")
                    self.driver.save_screenshot(f"{self.sspath}test_login_ddt_001--{self.scenario}--Passed.png")
                    self.log.info("Saving test_login_ddt_001--Passed Screenshot")
        print(status_list)
        if "Pass" not in status_list:
            self.log.info("test_login_ddt_001 is Failed")
            assert False
        else:
            self.log.info("test_login_ddt_001 is Passed")
            assert True
        self.log.info("test_login_ddt_001 is Completed")
