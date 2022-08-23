Feature: Date Picker

    Scenario: Pick a date on calendar
        Given I tap at the calendar 
        When  I pick the month with value "ธันวาคม"
        And   I pick the year with value "2002"
        And   I pick the day with value "17"
        And   I click ok button
        Then  The date is "17 Dec, 2002" 