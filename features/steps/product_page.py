from behave import given, when, then



@given('Open {query} page')
def open_product_page(context, query):
    context.app.product_page.open_product_page(query)


@when('Click on Add to cart button')
def add_to_cart_btn_click(context):
    context.app.product_page.click_add_to_cart()


@when('Click on cart button')
def cart_btn_click(context):
    context.app.product_page.click_cart()
