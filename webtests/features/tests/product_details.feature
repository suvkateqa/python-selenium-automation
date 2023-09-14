Feature: Tests for product page

  Scenario Outline: User can select colors
    Given Open Amazon product <product_id> page
    Then Verify user can click through colors and expects <expected_colors> with locator <locator>


    Examples:
    | product_id | expected_colors                                                   | locator |
    | B08JHKQPBV |  ['Army Green','Black', 'Brown', 'Burgundy']                      | COLOR_OPTIONS_TOP |
    | B07BJKRR25 | ['Black', 'Blue, Over Dye', 'Bright White', 'Dark Blue Vintage']  | COLOR_OPTIONS_JEANS |

