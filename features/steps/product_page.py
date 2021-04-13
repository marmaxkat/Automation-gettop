from behave import given, when, then


@when('Click on Add to cart button')
def add_to_cart_btn_click(context):
    context.app.product_page.click_add_to_cart()


@when('Click on cart button')
def cart_btn_click(context):
    context.app.top_menu.click_cart()
