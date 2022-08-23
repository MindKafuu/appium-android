from behave import given, when, then

'''
Scenario Outline: select option of drop down
        Given I tap the drop down
        When  I select "<option>"
        Then  The option is "<option>"
'''

@given(u'I tap the drop down')
def tap_drop_down(context):
    context.app.main_page.tap_drop_down()

@when(u'I select "{option}"')
def select_option(context, option):
    context.app.drop_down_page.select_option(option)

@then(u'The option is "{option}"')
def verify_drop_down(context, option):
    context.app.drop_down_page.verify_drop_down(option)