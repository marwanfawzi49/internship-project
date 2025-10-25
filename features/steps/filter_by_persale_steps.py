from behave import given, when, then
from selenium import webdriver
from features.app.application import Application
import os

@given('the user is on the main page "https://soft.reelly.io"')
def step_open_main_page(context):
    #context.driver = webdriver.Chrome()
    context.driver.get("https://soft.reelly.io")
    context.driver.maximize_window()


    context.app = Application(context.driver)


@given('the user is logged into the application')
def step_login(context):
    """
    Note:
    - Replace 'YOUR_USERNAME' and 'YOUR_PASSWORD' with valid credentials locally
      to verify login functionality.
    - In production or shared repositories, credentials should be supplied via
      environment variables (USER_EMAIL and USER_PASSWORD) for security reasons.
    """

    email = os.getenv("USER_EMAIL", "marwan_ismael@ymail.com")
    password = os.getenv("USER_PASSWORD", "MARWANfawzi1987")

    context.app.login_page.login(email, password)


@when('the user clicks on "Off-plan" from the left side menu')
def step_click_off_plan(context):
    context.app.off_plan_page.open_off_plan()


@then('the "Off-plan" page should open successfully')
def step_verify_off_plan(context):
    assert "Off-plan" in context.driver.page_source


@when('the user filters by sale status "Presale"')
def step_filter_presale(context):
    context.app.off_plan_page.filter_by_presale()


@then('only products with sale status "Presale" should be displayed')
def step_verify_presale(context):
    context.app.off_plan_page.verify_presale_results()
    context.driver.quit()
