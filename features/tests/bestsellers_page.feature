Feature: Access links on BestSellers page


  Scenario: BestSellers links are available on BestSellers page
    Given Open BestSeller page
    Then Verify BestSellers page has <expected_links> links