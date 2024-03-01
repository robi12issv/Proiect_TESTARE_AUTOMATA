## Created by robi at 15.02.2024

Feature: Search a product on the main page

#      #main_page -- search_steps
#  Scenario: Finding the product by correct name
#    Given I am on the main page
#    When I enter the product name
#    And I click the search button
#    Then I should see all those products

      #main_page -- search_steps
  Scenario: Finding the product by incorrect name (without space)
    Given I am on the main page
    When I enter the product name
    And I click the search button
    Then I should see all those products
#
#      #main_page -- search_steps
#  Scenario: Finding the product by incorrect name (misspelled)
#    Given I am on the main page
#    When I enter the product name
#    And I click the search button
#    Then I should see all those products
#
#Feature: Filtering the products
#
#      #products_page -- comparison_steps
#  Scenario: The list contains only the correct type of products
#    Given I am on the products page
#    When I verify the number of the products
#    Then I verify if there are incorrect products displayed
#
#    #price_page -- price_steps
#  Scenario: By price
#    Given I am on the product page
#    When I type the inferior price
#    And I type the superior price
#    And I submit the request
#    Then I should see the products in that range
#
#    #price_page -- price_steps
#  Scenario: Introducing lower price first
#    Given I am on the product page
#    When I type the inferior price
#    And I submit the request
#    And I type the superior price
#    And I submit the request again
#    Then I should see the products in that range
#
#    #price_page -- price_steps
#  Scenario: Introducing higher price first
#    Given I am on the product page
#    When I type the superior price
#    And I submit the request
#    And I type the inferior price
#    And I submit the request again
#    Then I should see the products in that range
#
#    #brand_page -- brand_steps
#  Scenario: By brand
#    Given I am on the product page
#    When I choose the brand
#    Then I should see the products of that brand
#
#Feature: Adding products to cart
#
#     #cart_page -- cart_steps
#  Scenario: Adding the product from the product page
#    Given I am on the chargers page
#    When I find the suitable product
#    And I add it to cart
#    Then I see cart page
#
#   #cart_page -- cart_steps
#  Scenario: Adding the product from all the products page
#    Given I am on the chargers page
#    When I add it to cart
#    Then I see cart page
#
#    #cart_brand_page -- cart_brand_steps
#  Scenario: Adding to cart after brand sorting
#    Given I am on the chargers page
#    When I sort the products
#    And I find the suitable product
#    And I add it to cart
#    Then I see cart page