from behave import given, when, then

from pages.price_page import PricePage


#  Scenario: Introducing both prices


@given('I am on the product page')
def step_impl(context):
    context.page = PricePage()
    context.page.get_products(context.config.userdata['product_name'])


@when('I type the inferior price')
def step_impl(context):
    context.page.lower_price(context.config.userdata['lower_price'])


@when('I type the superior price')
def step_impl(context):
    context.page.upper_price(context.config.userdata['upper_price'])


@when('I submit the request')
def step_impl(context):
    context.page.price_box()


@then('I should see the products in that range')
def step_impl(context):
    context.page.get_product_prices()


#  Scenario: Introducing lower price first

@given('I am on the product page')
def step_impl(context):
    context.page = PricePage()
    context.page.get_products(context.config.userdata['product_name'])


@when('I type the inferior price')
def step_impl(context):
    context.page.lower_price(context.config.userdata['lower_price'])


@when('I submit the request')
def step_impl(context):
    context.page.price_box()


@when('I type the superior price')
def step_impl(context):
    context.page.upper_price(context.config.userdata['upper_price'])


@when('I submit the request again')
def step_impl(context):
    context.page.price_box()


@then('I should see the products in that range')
def step_impl(context):
    context.page.get_product_prices()


# Scenario: Introducing higher price first


@given('I am on the product page')
def step_impl(context):
    context.page = PricePage()
    context.page.get_products(context.config.userdata['product_name'])


@when('I type the superior price')
def step_impl(context):
    context.page.upper_price(context.config.userdata['upper_price'])


@when('I submit the request')
def step_impl(context):
    context.page.price_box()


@when('I type the inferior price')
def step_impl(context):
    context.page.lower_price(context.config.userdata['lower_price'])


@when('I submit the request again')
def step_impl(context):
    context.page.price_box()


@then('I should see the products in that range')
def step_impl(context):
    context.page.get_product_prices()

