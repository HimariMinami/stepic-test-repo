from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators():
    LOG_IN_FORM = (By.CSS_SELECTOR, "#login_form")

    REG_FORM = (By.CSS_SELECTOR, "#register_form")