# Unit/Tests/test_login_logout.py

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Unit.Pages.loginPage import LoginPage
from Unit.Pages.homePage import HomePage
import HtmlTestRunner
import time

class LoginLogoutTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def test_login_and_logout(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        time.sleep(5)
        login_page = LoginPage(self.driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        time.sleep(5)
        login_page.click_login()
        time.sleep(5)
        home_page = HomePage(self.driver)
        home_page.click_user_dropdown()
        home_page.click_logout()

        # Assertion after logout (check if Username field is displayed again)
        #self.assertTrue(self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").is_displayed())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Abhay/Desktop/Selenium/Unit/Reports'))
