from behave import given, when, then

from pages.brand_page import BrandPage

# Scenario: By brand


# @given('I am on the product page')
# def step_impl(context):
#     context.page = BrandPage()
#     context.page.get_products(context.config.userdata['product_name'])
#
#
# @when('I choose the brand')
# def step_impl(context):
#     context.page.get_brand()
#
#
# @then('I should see the products of that brand')
# def step_impl(context):
#     context.page.brand_nr()
