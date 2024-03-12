Feature: Filtering the products

   #products_page -- comparison_steps
 Scenario: The list contains only the correct type of products
   Given I am on the products page
   When I verify the number of the products
   Then I verify if there are incorrect products displayed

   #price_page -- price_steps
 Scenario: By price
   Given I am on the product page
   When I type the inferior price
   And I type the superior price
   And I submit the request
   Then I should see the products in that range

   #price_page -- price_steps
 Scenario: Introducing lower price first
   Given I am on the product page
   When I type the inferior price
   And I submit the request
   And I type the superior price
   And I submit the request again
   Then I should see the products in that range

   #price_page -- price_steps
 Scenario: Introducing higher price first
   Given I am on the product page
   When I type the superior price
   And I submit the request
   And I type the inferior price
   And I submit the request again
   Then I should see the products in that range

   #brand_page -- brand_steps
 Scenario: By brand
   Given I am on the product page
   When I choose the brand
   Then I should see the products of that brand
