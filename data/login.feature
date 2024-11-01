Feature: User Login

  Scenario: Successful Login
    Given the user is on the login page
    When the user enters valid credentials
    Then the user is redirected to the dashboard

  Scenario: Unsuccessful Login
    Given the user is on the login page
    When the user enters invalid credentials
    Then an error message is displayed
