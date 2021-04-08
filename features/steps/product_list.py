from behave import given, when, then


@when('Sort products by alias {alias}')
def select_sort_order(context, alias):
    context.app.product_list_page.select_sort_option(alias)


@then('Verify products sorted by option {option}')
def verify_sort_order(context, option):
    context.app.product_list_page.verify_sort_order(option)


@then('Verify User can click through product pages')
def verify_page_navigation(context):
    context.app.product_list_page.verify_page_navigation()


@then('Verify User can reset to default sorting by alias {alias}')
def reset_sort_order(context, alias):
    context.app.product_list_page.select_sort_option(alias)
