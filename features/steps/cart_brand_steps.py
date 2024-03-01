# from behave import given, when, then
#
# from pages.cart_brand_page import TestPage
#
# #  Scenario: Adding the product from the product page
# #    Given I am on the chargers page
# #    When I find the suitable product
# #    And I add it to cart
# #    Then I see cart page
#
#
# @given('I am on the chargers page')
# def step_impl(context):
#     context.page = TestPage()
#     context.page.get_products(context.config.userdata['product_name'])
#
#
# @when('I sort the products')
# def step_impl(context):
#     context.page.get_brand()
#
#
# @when('I find the suitable product')
# def step_impl(context):
#     context.page.choose_product()
#
#
# @when('I add it to cart')
# def step_impl(context):
#     context.page.add_to_cart()
#
#
# @then('I see cart page')
# def step_impl(context):
#     context.page.cart_title()
