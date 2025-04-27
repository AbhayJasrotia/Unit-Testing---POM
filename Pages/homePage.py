# Unit/Pages/homePage.py

from ..Locators import Locators
import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_user_dropdown(self):
        self.driver.find_element(*Locators.user_dropdown).click()
        time.sleep(2)  # (small wait so dropdown opens)

    def click_logout(self):
        self.driver.find_element(*Locators.logout_link).click()
