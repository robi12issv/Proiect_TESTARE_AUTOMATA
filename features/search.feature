# Created by robi at 15.02.2024

Feature: Search a product on the main page

   #main_page -- search_steps
 Scenario: Finding the product by correct name
   Given I am on the main page
   When I enter the product name
   And I click the search button
   Then I should see all those products

   #main_page -- search_steps
 Scenario Outline: Finding the product by incorrect name
   Given I am on the main page
   When I enter the "<product>"
   And I click the search button
   Then I should see all those products

   Examples:
     | product        |
     | incarcator140w |
     | incarcaor 140w |
     | incarcator 140 |
