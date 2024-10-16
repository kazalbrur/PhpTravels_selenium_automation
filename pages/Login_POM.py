from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    text_email_xpath = (By.XPATH, '//*[@id="email"]')
    text_password_xpath = (By.XPATH, '//*[@id="password"]')
    click_login_xpath = (By.XPATH, '//*[@id="submit"]')
    click_menu_xpath = (By.XPATH, "//a[@id='dropdownUser1']")
    click_logout_xpath = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def enter_email(self, email):
        element = self.wait.until(ec.presence_of_element_located(LoginPage.text_email_xpath))
        element.send_keys(email)

    def enter_pwd(self, pwd):
        element = self.wait.until(ec.presence_of_element_located(LoginPage.text_password_xpath))
        element.send_keys(pwd)

    def click_login_button(self):
        element = self.wait.until(ec.element_to_be_clickable(LoginPage.click_login_xpath))
        element.click()

    def click_menu(self):
        element = self.wait.until(ec.element_to_be_clickable(LoginPage.click_menu_xpath))
        element.click()

    def click_logout(self):
        element = self.wait.until(ec.element_to_be_clickable(LoginPage.click_logout_xpath))
        element.click()
