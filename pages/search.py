"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ZooplaSearchPage:
    # URL

    URL = 'https://www.zoopla.co.uk/'

    # Locators

    SEARCH_INPUT = (By.ID, 'search-input-location')
    COOKIES_FORM = (By.CSS_SELECTOR, ".ui-cookie-consent-main")
    ACCEPT_COOKIES = (By.CSS_SELECTOR, ".ui-cookie-accept-all-medium-large")

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def load(self):
        self.browser.get(self.URL)

    def annoying(self):
        if self.browser.find_element(*self.COOKIES_FORM):
            cookie_accept = self.browser.find_element(*self.ACCEPT_COOKIES)
            cookie_accept.click()
        else:
            raise Exception('still showing annoying cookies')

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
