"""
Configuración base para la automatización de pruebas con Selenium y BDD.
Este archivo NO debe contener datos sensibles.
"""

from config.env_loader import load_environment


class BaseConfig:
    def __init__(self):
        # Cargar configuración del entorno (dev, staging, prod)
        env_config = load_environment()

        # Variables de entorno
        self.ENV = env_config["ENV"]
        self.BASE_URL = env_config["BASE_URL"]
        self.BROWSER = env_config["BROWSER"]
        self.HEADLESS = env_config["HEADLESS"]

        # Configuración global predeterminada
        self.IMPLICIT_WAIT = 3
        self.EXPLICIT_WAIT = 10
        self.SCREENSHOTS_PATH = "reports/screenshots/"
        self.LOG_PATH = "logs/test.log"
        self.REPORTS_PATH = "reports/"

        # Timeouts específicos
        self.PAGE_LOAD_TIMEOUT = 15
        self.SCRIPT_TIMEOUT = 10

        # Metadata para reportes o integración CI/CD
        self.PROJECT_NAME = "DemoQA Selenium BDD Automation"
        self.AUTHOR = "JVelab"
        self.VERSION = "1.0.0"

    def __repr__(self):
        return (
            f"<BaseConfig ENV={self.ENV}, BASE_URL={self.BASE_URL}, "
            f"BROWSER={self.BROWSER}, HEADLESS={self.HEADLESS}>"
        )


# Instancia lista para importar desde cualquier módulo
config = BaseConfig()
