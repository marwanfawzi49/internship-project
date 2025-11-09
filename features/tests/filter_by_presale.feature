 Feature: Filter properties by Presale status
  As a user
  I want to filter properties by their sale status
  So that I can view only properties that are in Presale status

  Background:
    Given the user is on the main page "https://soft.reelly.io"
    And the user is logged into the application

  Scenario: User filters properties by Presale status
    When the user clicks on "Off-plan" from the left side menu
    Then the "Off-plan" page should open successfully
    When the user filters by sale status "Presale"
    Then only products with sale status "Presale" should be displayed

  @mobile
  Scenario: User filters properties by Presale status on mobile
    Given the user is on the main page "https://soft.reelly.io"
    And the user is logged into the application
    When the user clicks on "Off-plan" from the left side menu
    Then the "Off-plan" page should open successfully
    When the user filters by sale status "Presale"
    Then only products with sale status "Presale" should be displayed
    And verify that the layout and elements are visible on mobile viewport
