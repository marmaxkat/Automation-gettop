# Created by inna at 4/8/21
Feature: # Product Category top navigation test
  # Enter feature description here

  Scenario: # User can see all items under IPHONE
    Given Open product-category/iphone page
    Then Verify User can see all items under IPHONE

  Scenario: #User can open each of the products under IPHONE category, and correct pages open
    Given Open Gettop main page
    When Hover on IPHONE link in top main menu
    Then Verify correct product page open under IPHONE