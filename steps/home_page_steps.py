from behave import *


@Given("Home page: I am on herokuap heme page")
def step_impl(context):
    context.home_page_object.navigate_to_home_page()


@When("Home page: I want to click on Form Authentication and Frames and Geolocation")
def step_impl(context):
    context.home_page_object.click_on_form_authentication()
    context.home_page_object.click_on_frames()
    context.home_page_object.click_on_geolocation()


@Then("Home page: I should be back on the home page")
def step_impl(context):
    context.home_page_object.check_the_page()

