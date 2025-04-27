# Unit/Locators.py

from selenium.webdriver.common.by import By

class Locators:
    username_textbox = (By.XPATH, "//input[@placeholder='Username']")
    password_textbox = (By.XPATH, "//input[@placeholder='Password']")
    login_button = (By.XPATH, "//button[@type='submit']")
    user_dropdown = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    logout_link = (By.LINK_TEXT, "Logout")
