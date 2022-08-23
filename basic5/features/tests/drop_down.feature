Feature: Drop Down

    Scenario Outline: select option of drop down
        Given I tap the drop down
        When  I select "<option>"
        Then  The option is "<option>"

        Examples:
            | option |
            | One    | 
            | Two    |
            | Free  |
            | Four   |