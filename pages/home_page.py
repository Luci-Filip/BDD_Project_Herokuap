from selenium.webdriver.common.by import By
from pages.base_page import Base_page


class Home_page_herokuap(Base_page):
    FORM_AUTHENTICATION = (By.XPATH, "//a[@href='/login']")
    FRAMES = (By.XPATH, "//a[@href='/frames']")
    GEOLOCATION = (By.XPATH, "//a[@href='/geolocation']")

    def navigate_to_home_page(self):
        self.chrome.get("https://the-internet.herokuapp.com/")

    def click_on_form_authentication(self):
        self.chrome.find_element(*self.FORM_AUTHENTICATION).click()
        actual_url = self.chrome.current_url
        expected_url = 'https://the-internet.herokuapp.com/login'
        assert actual_url == expected_url, "The element is not clickable!"
        self.chrome.back()

    def click_on_frames(self):
        self.chrome.find_element(*self.FRAMES).click()
        actual_url = self.chrome.current_url
        expected_url = 'https://the-internet.herokuapp.com/frames'
        assert actual_url == expected_url, 'The element is not clickable!'
        self.chrome.back()

    def click_on_geolocation(self):
        self.chrome.find_element(*self.GEOLOCATION).click()
        actual_url = self.chrome.current_url
        expected_url = 'https://the-internet.herokuapp.com/geolocation'
        assert actual_url == expected_url, 'The element is not clickable!'
        self.chrome.back()

    def check_the_page(self):
        home_page_url = self.chrome.current_url
        expected_url = 'https://the-internet.herokuapp.com/'
        assert home_page_url == expected_url, "Something is wrong!"


