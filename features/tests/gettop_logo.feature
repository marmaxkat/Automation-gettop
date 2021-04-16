# Created by inna at 4/1/21
Feature: # Gettop logo test
  # Enter feature description here

  Scenario: # GetTop logo is clickable and takes to https://gettop.us/
    Given Open Gettop main page
    When Click on first link in top main menu
    And Click on logo
    Then Gettop main page opened

