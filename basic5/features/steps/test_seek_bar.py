from behave import given, when, then

@given(u'I am at the seek bar')
def tap_time_button(context):
    pass

@when(u'I drag the range with value "{left}" and "{right}"')
def drag_seek_bar(context, left, right):
    context.app.seek_bar_page.drag_seek_bar(left, right)

@then(u'The left is "{left}"')
def verify_left_seek_bar(context, left):
    context.app.seek_bar_page.verify_left_seek_bar(left)

@then(u'The right is "{right}"')
def verify_right_seek_bar(context, right):
    context.app.seek_bar_page.verify_right_seek_bar(right)