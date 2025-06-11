from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException

from config import USER_AGENT
from helper import (
    Helper,
    DriverHelper,
    ElementChecker,
    scroll_google_maps_results
)

class MainParser(Helper):
    def __init__(self,start_page=0, stop_page=0, location=''):
        # Initialize Firefox options
        self.options = webdriver.FirefoxOptions()
        self.options.set_preference("general.useragent.override",
                                    USER_AGENT)  # Set custom user agent to avoid detection as a bot
        self.options.set_preference("dom.webdriver.enabled", False)  # Disable WebDriver detection
        self.options.set_preference("intl.accept_languages", 'en-us')  # Set language WebDriver
        self.options.set_preference("dom.webnotifications.enabled", False)  # Disable WebDriver notifications

        self.service = Service(executable_path='GeckoDriver/geckodriver.exe')  # Path to WebDriver

        self.driver = webdriver.Firefox(service=self.service,
                                        options=self.options)  # Create a new instance of the Firefox WebDriver with the specified options

        self.start_page = start_page
        self.stop_page = stop_page
        self.location = location
        self.driver_helper = DriverHelper(driver=self.driver)
        self.checker = ElementChecker(driver=self.driver)

        self.get_location_info()


    def get_location_info(self):
        try:
            self.random_pause_code(start=1, stop=6)
            self.driver_helper.send_by_url(url=f'https://www.google.com/maps/search/{self.location}')
            scroll_google_maps_results(driver=self.driver, pause_time=4, max_scrolls=11)
            if self.checker.class_exists(class_name='ecceSd'):
                link = self.driver.find_element(By.CLASS_NAME,'ecceSd').find_elements(By.TAG_NAME, 'a')
                href = [href.get_attribute('href') for href in link if 'place' in href.get_attribute('href')]
                self.create_directory(name_directory=self.location.capitalize())
                self.create_file_from_list(
                    data_list=href,
                    filename=f'{self.location.capitalize()}/links.txt'

                )

        except NoSuchElementException:
            self.random_pause_code(start=1, stop=6)
        return self.driver_helper.close_driver()


def main():
    return MainParser(
        location='your location'
    )


if __name__ == '__main__':
    main()
