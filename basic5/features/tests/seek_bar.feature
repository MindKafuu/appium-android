Feature: Seek Bar

    Scenario: select range with seek bar
        Given I am at the seek bar
        When  I drag the range with value "80" and "100"
        Then  The left is "80"
        And   The right is "100"