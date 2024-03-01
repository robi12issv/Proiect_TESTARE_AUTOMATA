The project was written in Python, using the PyCharm IDE. I used the following libraries: 
selenium, behave, webdriver_manager, behave_html_formatter
which I installed from the terminal using the syntax "pip install <library name>". 
From the selenium library, I imported the following libraries: webdriver, Service, ChromeDriverManager, expected_conditions, WebDriverWait, By.

The project is structured into 3 main folders:

"utils", where the main class and its methods are defined, which are applied to each test performed on the site;

"pages", where Python files are stored containing the lines of code related to the classes and methods necessary for each test individually;

"steps", where BDD-type Python files are stored containing the steps related to the correct execution of each test.

The "features" folder also contains the Gerkin file "vexio.feature" from which the tests will be run.

For cloning the project, open your preferred IDE, and in the terminal, enter the command "git clone" followed by the project link, like this: git clone https://github.com/robi12issv/ProiectTESTARE_AUTOMATA.git
Reports can be accessed from the "Reports" folder. They are named after the "_step" file that was run. Additionally, new reports can be created using the following syntax in the terminal: behave -f behave_html_formatter:HTMLFormatter -o behave-report.html
The tests are run from the "vexio.feature" file. Each scenario will be tested individually through the "Run" function, which is implemented in each scenario. When running a test, it is important that all other "_steps" files and scenarios from "vexio.feature" are commented out. 
For example, to run the product comparison test, all "_steps" files except "comparison_steps" should be commented out, and all scenarios except "Scenario: The list contains only the correct type of products" (with the corresponding feature) should also be commented out.
Each scenario has a commented line that indicates which "_steps" and "_pages" files contain the code and steps for the scenario to run.

Explained scenarios:

Feature: Search a product on the main page

 # Scenario: Finding the product
            main_page -- search_steps
    Given I am on the main page
    When I enter the product name
    And I click the search button
    Then I should see all those products

    Navigates to the main page of the website, identifying the search bar, entering the name of the desired product, and searching for it, ultimately resulting in redirection to the product page.


    
  # Scenario: The list contains only the correct type of products
              products_page -- comparison_steps
    Given I am on the products page
    When I verify the number of the products
    Then I verify if there are incorrect products displayed

    Based on the details of each product, it will verify whether there are only products of the searched type on the page, or if there are additional products and how many there are.


    
 # Scenario: By price
             price_page -- price_steps
    Given I am on the product page
    When I type the inferior price
    And I type the superior price
    And I submit the request
    Then I should see the products in that range

    Both prices will be entered simultaneously, and then the "Aplicare filtru preț" button will be pressed.


  
 # Scenario: Introducing lower price first
            price_page -- price_steps
    Given I am on the product page
    When I type the inferior price
    And I submit the request
    And I type the superior price
    And I submit the request again
    Then I should see the products in that range

    First, the lower price limit will be entered, followed by pressing the "Apply Price Filter" button. Then, the upper price limit will be entered, and the "Apply Price Filter" button will be pressed again.

    
 # Scenario: Introducing higher price first
            price_page -- price_steps
    Given I am on the product page
    When I type the superior price
    And I submit the request
    And I type the inferior price
    And I submit the request again
    Then I should see the products in that range

    First, the upper price limit will be entered, followed by pressing the "Apply Price Filter" button. Then, the lower price limit will be entered, and the "Apply Price Filter" button will be pressed again.

    
 # Scenario: By brand                                                      
          brand_page -- brand_steps
    Given I am on the product page
    When I choose the brand
    Then I should see the products of that brand

    This scenario involves navigating to the page of the searched products, applying a brand filter, and verifying if after applying the filter, the page contains other products as well.
    

Feature: Adding products to cart

 # Scenario: Adding the product from the product page
          cart_page -- cart_steps
    Given I am on the chargers page
    When I find the suitable product
    And I add it to cart
    Then I see cart page
    
    It will navigate to the page with the searched products, then navigate to the product page, identify the add-to-cart button, and implement the action.


 # Scenario: Adding the product from all the products page    
            cart_page -- cart_steps
    Given I am on the chargers page
    When I add it to cart
    Then I see cart page

    This scenario tests, using the same methods, adding a product to the cart directly from the page with all the products found after the search.

 # Scenario: Adding to cart after brand sorting                              
          cart_brand_page -- cart_brand_steps
    Given I am on the chargers page
    When I sort the products
    And I find the suitable product
    And I add it to cart
    Then I see cart page

    The third scenario tests adding a product to the cart after filtering based on the brand of the products.
