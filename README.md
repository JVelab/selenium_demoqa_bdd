# Selenium DemoQA BDD Automation

[![Python](https://img.shields.io/badge/python-3.14-blue)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/selenium-4.21-green)](https://www.selenium.dev/)
[![Behave](https://img.shields.io/badge/BDD-Behave-orange)](https://behave.readthedocs.io/)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

## 🚀 Autor

**GitHub:** [JVelab](https://github.com/JVelab)
**Proyecto:** Automatización de pruebas del sitio [DemoQA](https://demoqa.com) usando Selenium, BDD y pytest.

---

## 📌 Descripción

Este proyecto tiene como objetivo automatizar el **Practice Form** de DemoQA, mostrando:

* Uso de **Page Object Model (POM)**.
* Automatización con **Selenium 4**.
* Framework **BDD con Behave** y lenguaje **Gherkin**.
* Tests funcionales con **pytest**.
* Soporte de **entornos** (dev, staging, prod) usando `.env`.
* Manejo de datos aleatorios con **Faker**.

Es un proyecto pensado para **demostrar habilidades a reclutadores** de QA y automatización.

---

## 🗂 Estructura del proyecto

```
selenium_demoqa_bdd/
│
├── config/               # Configuración de entornos y base config
├── drivers/              # Drivers descargados por webdriver-manager
├── logs/                 # Logs de ejecución
├── reports/              # Reportes y screenshots
├── src/
│   ├── pages/            # Page Objects
│   ├── utils/            # Helpers (browser, faker, waits, screenshots)
│   └── steps/            # Steps definitions para BDD
├── tests/
│   ├── features/         # Archivos Gherkin (.feature)
│   └── pytest/           # Tests pytest
├── .env                  # Entorno actual
├── requirements.txt
└── README.md
```

---

## 🧪 Tests planeados

### 1️⃣ Completados hasta ahora

* **Practice Form**

  * Abrir la página del formulario
  * Llenar datos aleatorios (Faker)
  * Seleccionar género y número de teléfono
  * Submit del formulario
  * Verificar modal de confirmación

### 2️⃣ Pendientes

* Validación de errores de campos obligatorios
* Selección de fecha de nacimiento y calendario
* Selección de hobbies y selección múltiple
* Automatización de otros componentes de DemoQA (Checkboxes, Radio Buttons, Select Menu, Alerts)
* Integración con reportes HTML y screenshots automáticos
* Etiquetas BDD para **smoke**, **regression** y pruebas de **CI/CD**

---

## ⚙️ Tecnologías

* Python 3.14
* Selenium 4.21
* Behave 1.2.6 (BDD / Gherkin)
* pytest 8.2.2
* WebDriver Manager 4.0.1
* Faker 24.9.0
* python-dotenv 1.0.1

---

## 🏃 Cómo ejecutar

### 1. Clonar el proyecto

```bash
git clone https://github.com/JVelab/selenium_demoqa_bdd.git
cd selenium_demoqa_bdd
```

### 2. Instalar dependencias

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Ejecutar tests BDD (Behave)

```bash
behave tests/features/practice_form.feature
```

### 4. Ejecutar tests pytest

```bash
PYTHONPATH=.:$PYTHONPATH pytest -v --disable-warnings
```

> O usar `pytest.ini` configurado para que reconozca `src/`.

---

## ⚡ Notas importantes

* Los tests están preparados para funcionar en **Chrome y Edge**, incluyendo **modo headless**.
* Los datos del formulario se generan de manera aleatoria usando Faker.
* Se recomienda ejecutar los tests en un entorno limpio con Chrome actualizado.
* En macOS ARM puede ser necesario dar permisos al `chromedriver`:

```bash
chmod +x ~/.wdm/drivers/chromedriver/mac64/*/chromedriver-mac-arm64/chromedriver
xattr -d com.apple.quarantine ~/.wdm/drivers/chromedriver/mac64/*/chromedriver-mac-arm64/chromedriver
```

---

## 📈 Próximos pasos

* Captura automática de **screenshots en fallos**
* Integración de **reportes HTML**
* Pipeline de **CI/CD con GitHub Actions**
* Automatización de más formularios y widgets de DemoQA

---

## 🔗 Links útiles

* [DemoQA](https://demoqa.com)
* [Selenium](https://www.selenium.dev/)
* [Behave](https://behave.readthedocs.io/)
* [Faker](https://faker.readthedocs.io/en/master/)

---

**Proyecto desarrollado por JVelab**
