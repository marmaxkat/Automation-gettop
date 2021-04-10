from selenium.webdriver.common.by import By
from behave import given, when, then


@when("Click on first link in top main menu")
def click_menu(context):
    context.app.top_menu.click_first_link_top_menu()


@when("Click on logo")
def click_logo(context):
    context.app.top_menu.click_logo()


@then("Gettop main page opened")
def verify_main_page_opened(context):
    context.app.top_menu.verify_main_page_opened()
