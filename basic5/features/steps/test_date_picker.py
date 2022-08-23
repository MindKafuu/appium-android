from behave import given, when, then

@given(u'I tap at the calendar')
def tap_calendar(context):
    context.app.main_page.tap_calendar()

@when(u'I pick the month with value "{month}"')
def select_month(context, month):
    context.app.calendar_page.select_month(month)

@when(u'I pick the year with value "{year}"')
def select_month(context, year):
    context.app.calendar_page.select_year(year)

@when(u'I pick the day with value "{day}"')
def select_month(context, day):
    context.app.calendar_page.select_day(day)

@when(u'I click ok button')
def tap_ok(context):
    context.app.main_page.tap_ok()

@then(u'The date is "{date_text}"')
def verify_date_picker(context, date_text):
    context.app.calendar_page.verify_date_picker(date_text)
