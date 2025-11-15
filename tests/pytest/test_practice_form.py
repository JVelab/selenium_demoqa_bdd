from src.utils.browser_factory import create_browser
from src.utils.faker_data import generate_user_data
from src.pages.practice_form_page import PracticeFormPage
from config.env_loader import load_environment


def test_practice_form():
    config = load_environment()
    driver = create_browser()
    page = PracticeFormPage(driver)

    page.open(config["BASE_URL"])
    data = generate_user_data()
    page.fill_form(data)
    page.submit_form()

    assert page.is_modal_open() is not None

    driver.quit()
