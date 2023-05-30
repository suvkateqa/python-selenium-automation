Feature: Amazon main page tests

  Scenario: User can see hamburger menu
    Given Open Amazon page
    Then Verify hamburger menu icon present


    Scenario: Footer and header has correct amount of links
      Given Open Amazon page
      Then Verify that footer has 36 links
      Then Verify that header has 29 links


    Scenario: Bestseller page has correct amount of links
      Given Open BestSellers page
      Then Verify that Bestsellers page has 5 links