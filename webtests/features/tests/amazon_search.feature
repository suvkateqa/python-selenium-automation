# Created by ekaterinasuvorova at 5/5/23
Feature: Amazon search tests

  Scenario Outline: User can search for a product on Amazon
    Given Open Amazon page
    When Input text <search_word>
    When Click on search button
    Then Verify that text <search_result> is shown
    Examples:
    |search_word  |search_result  |
    |coffee       |"coffee"       |
#    |table        |"table"        |
#    |mug          |"mug"          |


  Scenario: User can add a product to the cart
    Given Open Amazon page
    When Input text Tritan Farm to Table Pitcher
    When Click on search button
    And Click on the first product
    And Store product name and price
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product and price


  Scenario: Verify that user can see product names and images
    Given Open Amazon page
    When Input text coffee
    When Click on search button
    Then Verify that every product has a name and an image


  Scenario: User can select and search in a department
    Given Open Amazon page
    When Select department by alias audiabe
    When Input text Faust
    When Click on search button
    Then Verify books department is selected
#    Then Verify <department> department is selected
#    Examples:
#    |value        |department |
#    |stripbooks   |books      |
#    |audible      |audible    |








