import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scroll_google_maps_results(driver: WebDriver, pause_time=2, max_scrolls=50):
    """
    Scrolls the Google Maps sidebar (search results panel) to load more places.

    :param driver: Selenium WebDriver instance.
    :param pause_time: Time to wait after each scroll (in seconds).
    :param max_scrolls: Maximum number of scroll attempts.
    """
    try:
        # Wait for the scrollable div to appear
        scrollable_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="feed"]'))
        )

        for i in range(max_scrolls):
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
            time.sleep(pause_time)

            # Optional: Stop if no more loading indicator or new places
            # This can be enhanced based on your project needs.

        print("Scrolling finished.")

    except Exception as e:
        print(f"Error during Google Maps scroll: {e}")



def scroll_custom_div(driver: WebDriver, pause_time=2, max_scrolls=50):
    """
    Scrolls a custom div to load more content dynamically.

    :param driver: Selenium WebDriver instance.
    :param pause_time: Time to wait after each scroll (in seconds).
    :param max_scrolls: Maximum number of scroll attempts.
    """
    try:
        # Wait for the target div to be present
        scrollable_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, "div.bJzME:nth-child(2) > div:nth-child(1) > div:nth-child(1)"
            ))
        )

        last_scroll_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_div)

        for i in range(max_scrolls):
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
            time.sleep(pause_time)

            new_scroll_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_div)
            if new_scroll_height == last_scroll_height:
                print(f"No more content to scroll after {i + 1} scrolls.")
                break
            last_scroll_height = new_scroll_height

        print("Finished scrolling the custom div.")

    except Exception as e:
        print(f"Error during scrolling custom div: {e}")
