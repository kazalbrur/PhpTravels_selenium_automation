from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class Add_User:
    click_users_dropdown_xpath = (By.XPATH, "//button[normalize-space()='Users']")
    click_all_users_option_xpath = (By.XPATH, "//a[normalize-space()='All Users']")
    click_add_button_xpath = (By.XPATH, "//a[@class='xcrud-button xcrud-green xcrud-action']")
    text_status_dropdown_xpath = (By.XPATH, "/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr["
                                            "1]/td[2]/div/span/span[1]/span/span[1]")
    enter_firstname_xpath = (By.XPATH, "//input[@name='dXNlcnMuZmlyc3RfbmFtZQ--']")
    enter_lastname_xpath = (By.XPATH, "//input[@name='dXNlcnMubGFzdF9uYW1l']")
    enter_email_xpath = (By.XPATH, "//input[@name='dXNlcnMuZW1haWw-']")
    enter_password_xpath = (By.XPATH, "//input[@placeholder='enter password']")
    enter_phone_xpath = (By.XPATH, "//input[@name='dXNlcnMucGhvbmU-']")
    text_usertype_dropdown_xpath = (By.XPATH, "/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr["
                                              "7]/td[2]/span/span[1]/span/span[1]")
    text_currency_dropdown_xpath = (By.XPATH, "/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr["
                                              "8]/td[2]/span/span[1]/span/span[1]")
    click_save_button_xpath = (By.XPATH, "//a[@class='xcrud-button xcrud-purple xcrud-action']")
    text_save_status_check_CSS = (By.CSS_SELECTOR, "tbody tr:nth-child(1) td:nth-child(4)")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    def click_users_dropdown(self):
        ele = self.wait.until(ec.element_to_be_clickable(Add_User.click_users_dropdown_xpath))
        try:
            ele.click()
        except ElementClickInterceptedException: # type: ignore
            # Scroll to the element to make it clickable
            ActionChains(self.driver).move_to_element(ele).perform()
            ele.click()

    def click_all_users_option(self):
        ele = self.wait.until(ec.element_to_be_clickable(Add_User.click_all_users_option_xpath))
        ele.click()

    def click_add_button(self):
        ele = self.wait.until(ec.element_to_be_clickable(Add_User.click_add_button_xpath))
        ele.click()

    def dropdown_status(self):
        ele = self.wait.until(ec.element_to_be_clickable(Add_User.text_status_dropdown_xpath))
        ele.click()
        element = self.wait.until(ec.presence_of_element_located((By.XPATH, "//input[@aria-label='Search']")))
        element.send_keys("Enabled")
        element.send_keys(Keys.ARROW_DOWN)
        element.send_keys(Keys.ENTER)

    def enter_firstname(self, firstname):
        ele = self.wait.until(ec.presence_of_element_located(Add_User.enter_firstname_xpath))
        ele.send_keys(firstname)

    def enter_lastname(self, lastname):
        ele = self.wait.until(ec.presence_of_element_located(Add_User.enter_lastname_xpath))
        ele.send_keys(lastname)

    def enter_email(self, email):
        ele = self.wait.until(ec.presence_of_element_located(Add_User.enter_email_xpath))
        ele.send_keys(email)

    def enter_password(self, password):
        ele = self.wait.until(ec.presence_of_element_located(Add_User.enter_password_xpath))
        ele.send_keys(password)

    def enter_phone(self, phone):
        ele = self.wait.until(ec.presence_of_element_located(Add_User.enter_phone_xpath))
        ele.send_keys(phone)

    def dropdown_usertype(self):
        ele = self.wait.until(ec.element_to_be_clickable(Add_User.text_usertype_dropdown_xpath))
        ele.click()
        element = self.wait.until(ec.presence_of_element_located((By.XPATH, "//input[@aria-label='Search']")))
        element.send_keys("Admin")
        element.send_keys(Keys.ARROW_DOWN)
        element.send_keys(Keys.ENTER)

    def dropdown_currency(self):
        ele = self.wait.until(ec.element_to_be_clickable(Add_User.text_currency_dropdown_xpath))
        ele.click()
        element = self.wait.until(ec.presence_of_element_located((By.XPATH, "//input[@aria-label='Search']")))
        element.send_keys("USD")
        element.send_keys(Keys.ARROW_DOWN)
        element.send_keys(Keys.ENTER)

    def click_save(self):
        ele = self.wait.until(ec.element_to_be_clickable(Add_User.click_save_button_xpath))
        ele.click()

    def save_status_check(self):
        try:
            ele = self.wait.until(ec.presence_of_element_located(Add_User.text_save_status_check_CSS))
            if ele.text == "Rahul":
                return True
            else:
                return False
        except NoSuchElementException:
            return False
