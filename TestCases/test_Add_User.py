import pytest

from pages.Add_User_POM import Add_User
from pages.Login_POM import LoginPage
from Utilities.Logger import LogGenerator
from Utilities.ReadProperties import ReadConfig


class Test_Add_User:
    url = ReadConfig.get_url()
    email = ReadConfig.get_email()
    pwd = ReadConfig.get_pwd()
    path = "Screenshots/"

    @pytest.mark.sanity
    def test_Add_User_001(self, setup):
        self.driver = setup
        self.log = LogGenerator.log_gen()
        self.lp = LoginPage(self.driver)
        self.au = Add_User(self.driver)

        self.log.info("Starting test_Add_User_001")
        self.log.info("Launching Browser")
        self.driver.get(self.url)
        self.log.info("Going to this URL-->" + self.url)
        self.lp.enter_email(self.email)
        self.log.info("Entering Email-->" + self.email)
        self.lp.enter_pwd(self.pwd)
        self.log.info("Entering Password-->" + self.pwd)
        self.lp.click_login_button()
        self.log.info("Clicking on Login Button")

        self.au.click_users_dropdown()
        self.log.info("Clicking on Users Dropdown")
        self.au.click_all_users_option()
        self.log.info("Clicking on All Users Option")
        self.au.click_add_button()
        self.log.info("Clicking on Add Button")
        self.au.dropdown_status()
        self.log.info("Choosing 'Enabled' on status Dropdown")
        self.au.enter_firstname("Rahul")
        self.log.info("Entering User's FirstName")
        self.au.enter_lastname("Dravid")
        self.log.info("Entering User's LastName")
        self.au.enter_email("RahulDravid@phptravels.com")
        self.log.info("Entering User's EmailID")
        self.au.enter_password("admin")
        self.log.info("Entering User's Password")
        self.au.enter_phone("6265787990")
        self.log.info("Entering User's Phone Number")
        self.au.dropdown_usertype()
        self.log.info("Choosing 'Admin' on UserType Dropdown")
        self.au.dropdown_currency()
        self.log.info("Choosing 'USD' on Currency Dropdown")
        self.au.click_save()
        self.log.info("Clicking on save Button")

        if self.au.save_status_check():
            self.log.info("test_Add_User_001 is Passed")
            self.driver.save_screenshot(f"{self.path}test_Add_User_001--Passed.png")
            self.log.info("Taking test_Add_User_001--Passed Screenshot")
            assert True
        else:
            self.log.info("test_Add_User_001 is Failed")
            self.driver.save_screenshot(f"{self.path}test_Add_User_001--Failed.png")
            self.log.info("Taking test_Add_User_001--Failed Screenshot")
            assert False
        self.log.info("test_Add_User_001 is Completed")
