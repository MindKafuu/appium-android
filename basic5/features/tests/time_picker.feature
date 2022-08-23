Feature: Time Picker

    Scenario: Pick time by write the time
        Given I tap at the time button 
        When  I tap the hour textbox and wrtie "11"
        And   I tap the minute textbox and write "11"
        And   Enter ok button
        Then  The time is "11:11" 