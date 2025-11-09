from behave import given, when, then
import os

# NOTE:
# - Do NOT create a WebDriver here.
# - environment.py creates: context.driver and context.app for every scenario.

@given('the user is on the main page "https://soft.reelly.io"')
def step_open_main_page(context):
    # Just navigate with the driver created in environment.py
    context.driver.get("https://soft.reelly.io")

@given('the user is logged into the application')
def step_login(context):
    """
    Use environment variables for credentials.
    Set them in your shell (Windows PowerShell example):
        $env:USER_EMAIL="you@example.com"
        $env:USER_PASSWORD="your_password"
    """
    email = os.getenv("USER_EMAIL", "marwan_ismael@ymail.com")   # <-- dev default (OK locally)
    password = os.getenv("USER_PASSWORD", "MARWANfawzi1987")     # <-- dev default (OK locally)
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
    # Do NOT quit here; environment.after_scenario will handle it.

@then('verify that the layout and elements are visible on mobile viewport')
def step_verify_mobile_layout(context):
    context.app.off_plan_page.verify_mobile_layout()
