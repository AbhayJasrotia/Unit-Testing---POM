# Unit/Pages/loginPage.py

from ..Locators import Locators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*Locators.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*Locators.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*Locators.login_button).click()
