Feature: Amazon customer service page tests

  Scenario: UI elements are present
    Given Open Customer Service page
    Then Verify Issue card container present
    And Verify Search our help library header present
    And Verify Search our help library field present
    And Verify All help topics header present
    And Verify Recommended topics container present


  Scenario: Issue Card container has correct amount of links
    Given Open Customer Service page
    Then Verify Issue card container has 10 links


  Scenario: Recommended Topics has correct amount of links
    Given Open Customer Service page
    Then Verify Recommended Topics container has 11 links