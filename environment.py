from browser import Browser
from pages.home_page import Home_page_herokuap
from pages.login_page import Login_page_herokuap


def before_all(context):
    context.browser = Browser()
    context.home_page_object = Home_page_herokuap()
    context.login_page_object = Login_page_herokuap()


def after_all(context):
    context.browser.close()
