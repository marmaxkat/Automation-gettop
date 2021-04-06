# Created by inna at 4/2/21
Feature: # Checkout tests
  # Enter feature description here

  Scenario: # User can fill out checkout form and go back to Cart by clicking 'Shopping Cart'
    Given Open iphone-se page
    When Click on Add to cart button
    And Click on cart button
    And Click on checkout button
    Then Verify User can fill out checkout form
    And Click on cart button


  Scenario: # User can select country
    Given Open iphone-se page
    When  Click on Add to cart button
    And Click on cart button
    And Click on checkout button
    Then Select country


  Scenario: # Required fields test
    Given Open iphone-se page
    When  Click on Add to cart button
    And Click on cart button
    And Click on checkout button
    And Click Place Order button
    Then Verify User cannot leave 7 required fields blank
    Then Verify User sees correct error messages