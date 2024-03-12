Feature: Adding products to cart

   #cart_page -- cart_steps
  Scenario: Adding the product from the product page
    Given I am on the chargers page
    When I find the suitable product
    And I add it to cart
    Then I see cart page

   #cart_page -- cart_steps
 Scenario Outline: Adding the product from the products page
   Given I am on the chargers page
   When I add it to cart
   Then I verify "<pg_title>"

   Examples:
     | pg_title                   |
     | Nu uita sa trimiti comanda |
     | Just a moment...           |

   #cart_page -- cart_steps
 Scenario: Adding to cart after brand sorting
   Given I am on the chargers page
   When I sort the products
   And I find the suitable product
   And I add it to cart
   Then I see cart page