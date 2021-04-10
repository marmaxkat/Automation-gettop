from behave import given, when, then

@when('Hover on {category} link in top main menu')
def top_menu_hover(context, category):
    context.app.top_menu.top_menu_hover(category)


@then('Verify correct product page open under {query}')
def verify_correct_page_open(context, query):
    context.app.product_page.verify_correct_page_open(query)