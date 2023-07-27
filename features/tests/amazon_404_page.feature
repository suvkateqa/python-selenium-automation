Feature: Test for 404 page

  Scenario: User is able to navigate to amazon blog page from
    Given Open Amazon product B08JHKQPBV11111 page
    And Store original window
    When Click on a dog image
    And Switch to new window
    Then Verify blog is opened
    And Close blog
    And Return to the original window

