Feature: Profile Update

  Scenario: Update Profile Information
    Given the user is on the profile page
    When the user updates their information
    Then the profile is saved successfully
    And a success message is displayed

  Scenario: Invalid Profile Update
    Given the user is on the profile page
    When the user enters invalid information
    Then an error message is displayed
