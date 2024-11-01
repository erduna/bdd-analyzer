Feature: User Registration

  Scenario: Successful Registration
    Given the user navigates to the registration page
    When the user fills in all required fields
    Then the user is redirected to the welcome page

  Scenario: Registration with Missing Fields
    Given the user navigates to the registration page
    When the user leaves a required field empty
    Then an error message is displayed
