Feature: Practice Form
  As a QA engineer
  I want to automate the DemoQA Practice Form
  So I can demonstrate form handling with Selenium

  Scenario: Complete and submit practice form successfully
    Given I open the Practice Form page
    When I fill the form with valid random data
    And I submit the form
    Then the confirmation modal should appear