from behave import given, when, then


@when('Click Place Order button')
def place_order_btn_click(context):
    context.app.checkout_page.place_order_btn_click()

@then('Verify User can fill out checkout form')
def verify_fields_active(context):
    context.app.checkout_page.verify_active_fields()


@then('Click on cart button')
def cart_btn_click(context):
    context.app.checkout_page.click_cart()


@then('Select country')
def select_country(context):
    context.app.checkout_page.select_country()


@then('Verify User cannot leave {query} required fields blank')
def verify_reqired_fields(context, query):
    context.app.checkout_page.invalid_fields(query)


@then('Verify User sees correct error messages')
def verify_error_messages(context):
    context.app.checkout_page.verify_error_messages()
