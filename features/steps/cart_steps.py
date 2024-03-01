# from behave import given, when, then
#
# from pages.cart_page import CartPage
#
# #  Scenario: Adding the product from the product page
#
#
# @given('I am on the chargers page')
# def step_impl(context):
#     context.page = CartPage()
#     context.page.get_products(context.config.userdata['product_name'])
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
#
#
# #  Scenario: Adding the product from all the products page
#
# @given('I am on the chargers page')
# def step_impl(context):
#     context.page = CartPage()
#     context.page.get_products(context.config.userdata['product_name'])
#
#
# @when('I add it to cart')
# def step_impl(context):
#     context.page.add_2_to_cart()
#
#
# @then('I see cart page')
# def step_impl(context):
#     context.page.cart_title()
