Feature: Testing login scenarios on herokuap login page

  Scenario: I want to complete the user and pass on herokuap login page and check success messages and logout
    Given Login page: I am on herokuap login page
    When Login page: I want to complete the username and password and login
    Then Login page / secure: I should be able to see the success messages and pres the logout button