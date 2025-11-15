from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        # ocultar banners fijos si existen
        try:
            self.driver.execute_script("document.querySelector('footer').style.display='none';")
            self.driver.execute_script("document.querySelector('#fixedban').style.display='none';")
        except:
            pass
        # scroll al elemento
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # click seguro
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
