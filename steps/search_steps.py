import time
from behave import given, when, then

from pages.main_page import MainPage

# Scenario: Finding the product by correct name


# @given('I am on the main page')
# def step_impl(context):
#     context.page = MainPage()
#     context.page.load()
#
#
# @when('I enter the product name')
# def step_impl(context):
#     context.page.search_item(context.config.userdata['product_name'])
#
#
# @when('I click the search button')
# def step_impl(context):
#     context.page.search_button()
#
#
# @then('I should see all those products')
# def step_impl(context):
#     context.page.get_url_title()

# Scenario: Finding the product by incorrect name (without space)


@given('I am on the main page')
def step_impl(context):
    context.page = MainPage()
    context.page.load()
    time.sleep(3)


@when('I enter the product name')
def step_impl(context):
    context.page.search_item(context.config.userdata['product_name_2'])


@when('I click the search button')
def step_impl(context):
    context.page.search_button()


@then('I should see all those products')
def step_impl(context):
    context.page.get_url_title()
#
# # Scenario: Finding the product by incorrect name (misspelled)
#
#
# @given('I am on the main page')
# def step_impl(context):
#     context.page = MainPage()
#     context.page.load()
#
#
# @when('I enter the product name')
# def step_impl(context):
#     context.page.search_item(context.config.userdata['product_name_3'])
#
#
# @when('I click the search button')
# def step_impl(context):
#     context.page.search_button()
#
#
# @then('I should see all those products')
# def step_impl(context):
#     context.page.get_url_title()
