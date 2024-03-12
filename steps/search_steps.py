from behave import given, when, then

from pages.main_page import MainPage

# Scenario: Finding the product by correct name


@given('I am on the main page')
def step_impl(context):
    context.page = MainPage()
    context.page.load()


@when('I enter the product name')
def step_impl(context):
    context.page.enter_item(context.config.userdata['product_name'])


@when('I click the search button')
def step_impl(context):
    context.page.click_search_button()


@then('I should see all those products')
def step_impl(context):
    context.page.get_url_title()

# Scenario outline: Finding the product by incorrect name


@given('I am on the main page')
def step_impl(context):
    context.page = MainPage()
    context.page.load()


@when('I enter the "{product}"')
def step_impl(context, product: str):
    context.page.enter_product(product)


@when('I click the search button')
def step_impl(context):
    context.page.click_search_button()


@then('I should see all those products')
def step_impl(context):
    context.page.get_articles()

