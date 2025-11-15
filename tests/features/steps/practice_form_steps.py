from behave import given, when, then
from src.utils.browser_factory import create_browser
from src.utils.faker_data import generate_user_data
from src.pages.practice_form_page import PracticeFormPage
from config.env_loader import load_environment

@given("I open the Practice Form page")
def step_open_form(context):
    config = load_environment()
    context.driver = create_browser()
    context.page = PracticeFormPage(context.driver)
    context.page.open(config["BASE_URL"])

@when("I fill the form with valid random data")
def step_fill_form(context):
    context.user_data = generate_user_data()
    context.page.fill_form(context.user_data)

@when("I submit the form")
def step_submit(context):
    context.page.submit_form()

@then("the confirmation modal should appear")
def step_modal(context):
    assert context.page.is_modal_open() is not None
    context.driver.quit()
