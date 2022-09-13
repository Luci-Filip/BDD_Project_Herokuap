from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Base_page


class Login_page_herokuap(Base_page):
    USERNAME = (By.XPATH, "//input[@id='username']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@class='radius']")
    SUCCESS_MESSAGES = (By.XPATH, "//div[@id='flash']")
    LOGOUT_BUTTON = (By.XPATH, "//a[@href='/logout']")

    def navigate_to_login_page(self):
        self.chrome.get('https://the-internet.herokuapp.com/login')

    def complete_username_password(self):
        self.chrome.find_element(*self.USERNAME).send_keys("tomsmith")
        self.chrome.find_element(*self.PASSWORD).send_keys("SuperSecretPassword!")

    def click_login_check_messages_logout(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        success_messages = self.chrome.find_element(*self.SUCCESS_MESSAGES)
        assert success_messages.is_displayed(), "The messages is not displayed!"
        logout_button = self.chrome.find_element(*self.LOGOUT_BUTTON)
        assert logout_button.is_displayed(), "The logout button is not displayed!"
        logout_button.click()
        sleep(2)
