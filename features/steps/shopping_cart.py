from behave import given, when, then

@when('Click on checkout button')
def click_checkout_btn(context):
    context.app.shopping_cart.checkout_btn_clock()