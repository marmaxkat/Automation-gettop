# Created by inna at 4/6/21
Feature: # Sort by popularity
  # Enter feature description here

  Scenario: # Sort by popularity
    Given Open shop page
    When Sort products by alias popularity
    Then Verify products sorted by option Sort by popularity
    And Verify User can click through product pages
    And Verify User can reset to default sorting by alias menu_order
    And Verify products sorted by option Default sorting

  Scenario: # Url https://gettop.us/shop/?orderby=popularity opens a web page with products sorted by popularity
    Given Open /shop/?orderby=popularity page
    Then Verify products sorted by option Sort by popularity
