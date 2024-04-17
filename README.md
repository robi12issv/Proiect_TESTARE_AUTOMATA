# TESTED APPLICATION

### https://www.vexio.ro

I chose to test the Vexio website, an e-commerce site, because I've personally used it and found certain errors. The site has basic e-commerce functionalities, such as product search, filtering them using certain parameters, and adding them to the cart. More specifically, I tested the page displaying products resulting from searching for a specific item.

## LANGUAGE, IDE, BOOKSTORES

The project was written in Python, using the PyCharm IDE. I used the following libraries: `selenium`, `webdriver_manager`, `behave_html_formatter` which I installed from the terminal using the syntax `pip install <library name>`. From the selenium library, I imported the following libraries: `webdriver`, `Service`, `ChromeDriverManager`, `expected_conditions`, `WebDriverWait`, `By`.

## THE IMPORTANCE OF AUTOMATED TESTING

Automated testing expands the range of tests available to be executed on UX. It includes tools through which elements that the end customer cannot directly interact with can be tested, so they cannot be manually tested. Moreover, it allows for comparing the obtained results with theoretically correct results. Since automated testing involves writing methods in a programming language, once the code is written, unlimited tests can be performed in a short time, as there is no need to repeat the entire process manually.

## THE CHOSEN METHODOLOGY AND DESIGN PATTERN

I used BDD, that promotes teamwork by describing app behavior using simple language like Gherkin, improving communication and ensuring user expectations are met through automated tests reflecting specified behavior. For design pattern I used "POM" that offers advantages like modularity, reusability, readability, maintainability, enabling parallel execution, and fostering collaboration between developers and testers.

## THE PROJECT'S STRUCTURE:

The project is structured into 4 main folders:

- `utils`, where the main class and its methods are defined, which are applied to each test performed on the site;
- `pages`, where Python files are stored containing the lines of code related to the classes and methods necessary for each test individually;
- `steps` where BDD Python files are stored containing the steps corresponding to the correct execution of each test;
- `features` with the Gerkin files ".feature" that contain the features and scenarios that are to be tested.

## PROJECT USE INSTRUCTIONS

For cloning the project, open your preferred IDE and in the terminal, enter the command `git clone` followed by the project link, like this: `git clone https://github.com/robi12issv/Proiect_TESTARE_AUTOMATA.git`. 

Reports can be accessed from the "Reports" folder. They are named after the "_step" file that was run. Additionally, new reports can be created using the following syntax in the terminal: behave -f behave_html_formatter:HTMLFormatter -o behave-report.html. 
The reports are named after the feature number, scenario number, and the "_steps" file. For example: f1_s1_search_steps

The tests are run from the ".feature" fileS. Each scenario will be tested individually through the `Run` function, which is implemented in each scenario. When running a test, it is important that all other "_steps" files and scenarios from "vexio.feature" are commented out. 

For example, to run the product comparison test, all "_steps" files except "comparison_steps" should be commented out, and all scenarios except "Scenario: The list contains only the correct type of products" (with the corresponding feature) should also be commented out.

Each scenario has a commented line that indicates which `_steps` and `_pages` files contain the code and steps for the scenario to run.

## EXPLAINED SCENARIOS

   - Scenario: Finding the product
     Navigates to the main page of the website, identifying the search bar, entering the name of the desired product, and searching for it, ultimately resulting in redirection to the product page.
   - `Scenario Outline: Finding the product by incorrect name`: 
     Navigates to the main page of the website, identifying the search bar, entering the name of the desired product in diferent forms, both correct and incorrect.
   - `Scenario: The list contains only the correct type of products`: 
     Based on the details of each product, it will verify whether there are only products of the searched type on the page, or if there are additional products and how many there are.
   - `Scenario: By price`: 
     Both prices will be entered simultaneously, and then the "Aplicare filtru preț" button will be pressed.
   - `Scenario: Introducing lower price first`: 
     First, the lower price limit will be entered, followed by pressing the "Apply Price Filter" button. Then, the upper price limit will be entered, and the "Apply Price Filter" button will be pressed again.
   - `Scenario: Introducing higher price first`: 
     First, the upper price limit will be entered, followed by pressing the "Apply Price Filter" button. Then, the lower price limit will be entered, and the "Apply Price Filter" button will be pressed again.
   - `Scenario: By brand`:                                                       
     This scenario involves navigating to the page of the searched products, applying a brand filter, and verifying if after applying the filter, the page contains other products as well.
   - `Scenario: Adding the product from the product page`: 
     It will navigate to the page with the searched products, then navigate to the product page, identify the add-to-cart button, and implement the action.
   - `Scenario Outline: Adding the product from all the products page`:     
     This scenario adds a product to the cart directly from the products page and then compares page's title with the expectet page title.
   - `Scenario: Adding to cart after brand sorting`: 
     The third scenario tests adding a product to the cart after filtering based on the brand of the products.

## SCREENSHOTS WITH THE CODE

The relationship between ".feature" file, "_steps" file and "page" file:
<img width="1794" alt="image" src="https://github.com/robi12issv/Proiect_TESTARE_AUTOMATA/assets/160391019/f858e94c-53e0-4570-860b-af9fb8cb9d52">
