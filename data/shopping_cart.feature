Feature: Shopping Cart Management

  Scenario: Add Item to Cart
    Given the user is on the product page
    When the user clicks the add to cart button
    Then the item is added to the shopping cart

  Scenario: Remove Item from Cart
    Given the user is viewing the shopping cart
    When the user clicks the remove button
    Then the item is removed from the shopping cart
