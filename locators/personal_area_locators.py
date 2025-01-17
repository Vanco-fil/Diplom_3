from selenium.webdriver.common.by import By


class PersonalAreaLocators:

    # Поле ввода пароля
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")

    # Поле ввода емейла
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/../input")

    # Кнопка "Войти"
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")

    # Кнопка "Оформить заказ"
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    # Кнопка "История заказов"
    HISTORY_ORDER = (By.XPATH, "//a[text()='История заказов']")

    # Кнопка "Выход"
    LOGOUT_BUTTON = By.XPATH, "//button[text()='Выход']"
    