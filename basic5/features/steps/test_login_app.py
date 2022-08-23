from behave import given, when, then

@given(u'I am at the login page')
def test_login(context):
    pass

@when(u'I fill the username textbox with value "{username}"')
def input_username(context, username):
    context.app.login_page.input_username(username)

@when(u'I fill the password textbox with value "{password}"')
def input_password(context, password):
    context.app.login_page.input_password(password)

@then(u'Test login for "{round:d}" times')
def verify_login(context, round):
    for i in range(round):
        context.app.main_page.tap_submit_button()
        context.app.login_page.verify_login(i + 1)
        context.app.main_page.tap_OK_button()






