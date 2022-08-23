Feature: Login

    @test-data-from-excel
    Scenario Outline: Logging in on app
        Given I am at the login page 
        When  I fill the username textbox with value "<username>"
        And   I fill the password textbox with value "<password>"
        Then  Test login for "3" times

        Examples: 
            | username | password |
            

        