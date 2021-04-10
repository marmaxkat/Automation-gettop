from behave import given, when, then


@given("Open Gettop main page")
def open_gettop(context):
    context.app.top_menu.open_main_page()


@given('Open {query} page')
def open_product_page(context, query):
    context.app.product_page.open_product_page(query)


