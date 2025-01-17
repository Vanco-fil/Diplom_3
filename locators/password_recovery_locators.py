from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:

    # Текст кнопки "Личный Кабинет"
    MY_OFFICE_BUTTON = (By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX']/p[text() ='Личный Кабинет']")

    # Кликабельный текст "Восстановить пароль"
    RECOVERY_PASSWORD_LINK = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']")

    # Текст заголовка страницы "Восстановления пароля"
    RECOVERY_PASSWORD_HEADER = (By.XPATH, "//h2[text()='Восстановление пароля']")

    # Кнопка "Восстановить"
    RECOVERY_BUTTON = (By.XPATH, "//button[text()='Восстановить']")

    # Поле ввода для пароля
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")

    # Поле ввода для емейла
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/../input")

    # Иконка глаза рядом с полем ввода пароля
    EYE_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon') and contains(@class, 'input__icon-action')]")

    # Статус видимости у поля с паролем
    VISIBLE_PASS_INPUT = (By.XPATH, "//div[contains(@class, 'input_status_active')]")
