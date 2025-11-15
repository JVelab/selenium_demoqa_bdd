from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class PracticeFormPage(BasePage):

    URL = "/automation-practice-form"

    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    GENDER_MALE = (By.XPATH, "//label[text()='Male']")
    MOBILE = (By.ID, "userNumber")
    SUBMIT = (By.ID, "submit")
    MODAL_TITLE = (By.ID, "example-modal-sizes-title-lg")

    def open(self, base_url):
        self.driver.get(base_url + self.URL)

    def fill_form(self, data):
        self.send_keys(self.FIRST_NAME, data["first_name"])
        self.send_keys(self.LAST_NAME, data["last_name"])
        self.send_keys(self.EMAIL, data["email"])
        self.click(self.GENDER_MALE)
        self.send_keys(self.MOBILE, data["mobile"])

    def submit_form(self):
        self.click(self.SUBMIT)

    def is_modal_open(self):
        return self.is_visible(self.MODAL_TITLE)
