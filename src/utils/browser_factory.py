from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from config.env_loader import load_environment
import os


def create_browser():
    config = load_environment()

    # Chrome
    if config["BROWSER"] == "chrome":
        options = Options()
        if config["HEADLESS"]:
            options.add_argument("--headless=new")

        # Fix: get real binary instead of THIRD_PARTY_NOTICES.
        driver_path = ChromeDriverManager().install()

        # Replace NOTICE file if wrongly selected
        if "THIRD_PARTY" in driver_path:
            correct_dir = os.path.dirname(driver_path)
            driver_path = f"{correct_dir}/chromedriver"

        service = ChromeService(driver_path)
        driver = webdriver.Chrome(service=service, options=options)
        
    # Edge
    elif config["BROWSER"] == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)

    # Browser no soportado
    else:
        raise Exception(f"Browser '{config['BROWSER']}' not supported")

    driver.maximize_window()
    return driver
