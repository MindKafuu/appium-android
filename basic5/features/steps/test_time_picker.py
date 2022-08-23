from behave import given, when, then

@given(u'I tap at the time button')
def tap_time_button(context):
    context.app.main_page.tap_time_button()

@when(u'I tap the hour textbox and wrtie "{hour}"')
def input_hour(context, hour):
    context.app.time_page.input_hour(hour)

@when(u'I tap the minute textbox and write "{minute}"')
def input_minute(context, minute):
    context.app.time_page.input_minute(minute)

@when(u'Enter ok button')
def tap_ok(context):
    context.app.main_page.tap_ok()

@then(u'The time is "{time}"')
def verify_time_picker(context, time):
    context.app.time_page.verify_time_picker(time)