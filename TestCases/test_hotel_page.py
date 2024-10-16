from datetime import datetime, timedelta
import pytest

from pages.hotel_page import HOTELTRAVEL
from Utilities.Logger import LogGenerator

class Test_HotelSearch:
    log = LogGenerator.log_gen()
    path = "Screenshots/"

    @pytest.mark.sanity
    def test_hotel_search(self, setup):
        # Initialize the page object and log the start of the test
        self.log.info("Starting test_hotel_search")
        self.hotel_page = HOTELTRAVEL(setup)
        
        # Load the page
        self.log.info("Loading the hotel booking page")
        self.hotel_page.load_page()
        
        # Select the hotel search dropdown and type "Barcelona"
        self.log.info("Selecting hotel search and entering 'Barcelona'")
        self.hotel_page.select_hotel()
        self.hotel_page.type_hotel("Dubai")
        self.hotel_page.click_select_hotel()
        
        # Select the check-in and check-out dates
        self.log.info("Selecting check-in and check-out dates")
        check_in_date = datetime(2024, 10, 16)
        check_out_date = datetime(2024, 10, 17)
        
        self.hotel_page.select_check_in()
        self.hotel_page.date_in(check_in_date.strftime("%m/%d/%Y"))
        self.hotel_page.select_check_out()
        self.hotel_page.date_out(check_out_date.strftime("%m/%d/%Y"))

        # Submit the hotel search
        self.log.info("Submitting the hotel search form")
        self.hotel_page.click_submit()

        # Assert that the search results contain "SEARCH HOTELS IN BARCELONA"
        self.log.info("Verifying the search result for 'Dubai'")
        result = self.hotel_page.get_result()
        if "SEARCH HOTELS IN BARCELONA" in result:
            self.log.info("Hotel search result matched—test_hotel_search Passed")
            self.hotel_page.browser.save_screenshot(f"{self.path}test_hotel_search--Passed.png")
            assert True
        else:
            self.log.error("Hotel search result did not match—test_hotel_search Failed")
            self.hotel_page.browser.save_screenshot(f"{self.path}test_hotel_search--Failed.png")
            assert False
