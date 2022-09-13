from behave import *


@given('Login page: I am on herokuap login page')
def step_impl(context):
    context.login_page_object.navigate_to_login_page()


@when("Login page: I want to complete the username and password and login")
def step_impl(context):
    context.login_page_object.complete_username_password()


@then('Login page / secure: I should be able to see the success messages and pres the logout button')
def step_impl(context):
    context.login_page_object.click_login_check_messages_logout()
