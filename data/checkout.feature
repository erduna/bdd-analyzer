Feature: Checkout Process

  Scenario: Successful Checkout
    Given the user has items in the shopping cart
    When the user proceeds to checkout
    Then the order confirmation page is displayed

  Scenario: Checkout with Empty Cart
    Given the user is on the shopping cart page
    When the user tries to proceed to checkout
    Then an error message is displayed
