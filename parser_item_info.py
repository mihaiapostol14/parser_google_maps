import json
import os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

from config import USER_AGENT
from helper import (
    Helper,
    DriverHelper,
    ElementChecker,
    scroll_custom_div
)


class ParserItemInfo(Helper):
    def __init__(self,source_file=''):
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
        self.source_file = source_file
        self.driver_helper = DriverHelper(driver=self.driver)
        self.checker = ElementChecker(driver=self.driver)

        # self.remove_duplicate(
        #     default=f"{self.source_file.split("/")[0]}/cars_Unsorted_link.txt",
        #     sorted_filename=f"{self.source_file.split("/")[0]}/cars_Sorted_link.txt",
        # )

        self.iter_by_item()

    def iter_by_item(self):
        try:
            with open(self.source_file, mode='r') as file:
                urls = file.read().split()
                for url in urls:
                    self.random_pause_code(start=1, stop=4)
                    self.driver_helper.send_by_url(url=url)
                    self.save_to_json()
        except FileNotFoundError:
            self.driver_helper.close_driver()
            print('File not found')

    def get_title(self):
        self.random_pause_code(start=1, stop=6)
        try:
            if self.checker.class_exists(class_name='DUwDvf'):
                return self.driver.find_element(By.CLASS_NAME, 'DUwDvf').text
            else:
                print('Title class not found.')
        except NoSuchElementException:
            print('Title element not found.')
            self.random_pause_code(start=1, stop=6)
            return self.driver_helper.close_driver()


    def save_to_json(self):
        scroll_custom_div(driver=self.driver, pause_time=6, max_scrolls=2)
        try:
            if self.checker.class_exists(class_name='Io6YTe'):
                elements = self.driver.find_elements(By.CLASS_NAME, 'Io6YTe')
                values = [el.text for el in elements]
                keys = ['address', 'website', 'phone', 'code plus']

                data_dict = {'title': self.get_title()}
                data_dict.update(dict(zip(keys, values[:len(keys)])))

                # Prepare save path
                base_name = os.path.splitext(os.path.basename(self.source_file))[0]
                folder = os.path.dirname(self.source_file)
                json_path = os.path.join(folder, f"{base_name}.json")

                # Append to existing JSON array or create a new one
                if os.path.exists(json_path):
                    with open(file=json_path, mode='r+', encoding='utf-8') as file:
                        try:
                            existing_data = json.load(file)
                        except json.JSONDecodeError:
                            existing_data = []

                        existing_data.append(data_dict)
                        file.seek(0)
                        json.dump(existing_data, file, indent=4, ensure_ascii=False)
                        file.truncate()
                else:
                    with open(file=json_path, mode='w', encoding='utf-8') as file:
                        json.dump([data_dict], file, indent=4, ensure_ascii=False)

            else:
                print('Data class not found.')

        except NoSuchElementException:
            print('Main data element not found.')
            self.random_pause_code(start=1, stop=6)
        return self.driver_helper.close_driver()




def main():
    return ParserItemInfo(
        source_file='Farmacia/links.txt'
    )


if __name__ == '__main__':
    main()
