from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class HOTELTRAVEL:
    SELECT_HOTEL_SEARCH = (By.ID, "select2-hotels_city-container")
    SEARCH_HOTEL = (By.CLASS_NAME, "select2-search__field")
    SELECT_CHECK_IN = (By.ID, "checkin")
    DATES_IN = (By.CSS_SELECTOR, "#checkin")
    SELECT_CHECK_OUT = (By.ID, "checkout")
    DATES_OUT = (By.CSS_SELECTOR, "#checkout")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "#submit")
    RESULT = (By.CLASS_NAME, "sec__title_list")
    URL = "https://phptravels.net"

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)

    def load_page(self):
        self.browser.get(self.URL)
        self.wait.until(EC.title_contains("PHPTRAVELS"))

    def select_hotel(self):
        try:
            element = self.wait.until(EC.element_to_be_clickable(self.SELECT_HOTEL_SEARCH))
            element.click()
        except TimeoutException:
            print("Timeout occurred while selecting the hotel search element")

    def type_hotel(self, hotel):
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.SEARCH_HOTEL))
            element.send_keys(hotel)
        except TimeoutException:
            print("Timeout occurred while typing the hotel name")

    def click_select_hotel(self):
        self.browser.find_element(*self.SEARCH_HOTEL).send_keys(Keys.ENTER)

    def select_check_in(self):
        self.browser.find_element(*self.SELECT_CHECK_IN).click()

    def date_in(self, date):
        check_in = self.browser.find_element(*self.DATES_IN)
        check_in.clear()
        check_in.send_keys(date)

    def select_check_out(self):
        self.browser.find_element(*self.SELECT_CHECK_OUT).click()

    def date_out(self, date):
        check_out = self.browser.find_element(*self.DATES_OUT)
        check_out.clear()
        check_out.send_keys(date)

    def click_submit(self):
        try:
            submit_button = self.wait.until(EC.element_to_be_clickable(self.BUTTON_SUBMIT))
            submit_button.click()
        except TimeoutException:
            print("Timeout occurred while clicking the submit button")

    def get_result(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.RESULT)).text
        except TimeoutException:
            print("Timeout occurred while getting the search result")
            return None