import allure
from data import Url
from pages.password_recovery_page import PasswordRecoveryPage
from pages.personal_area_page import PersonalAreaPage


class TestPersonalArea:

    @allure.title("Переход по клику на «Личный кабинет»")
    @allure.description("Проверяем работу кнопки личного кабинета в хедере")
    def test_click_goto_personal_account(self, driver):
        password_recovery = PasswordRecoveryPage(driver)
        password_recovery.go_to_personal_area()
        assert password_recovery.get_current_url() == Url.LOGIN_PAGE

    @allure.title("Переход в раздел «История заказов»")
    @allure.description("Проверяем открытие страницы истории заказов у авторизованного пользователя")
    def test_click_goto_history_orders(self, driver, create_user):
        password_recovery = PasswordRecoveryPage(driver)
        personal_area = PersonalAreaPage(driver)
        password_recovery.go_to_personal_area()
        personal_area.authorization(create_user)
        password_recovery.go_to_personal_area()
        personal_area.open_history_orders()
        assert personal_area.get_current_url() == Url.HISTORY_PAGE

    @allure.title("Выход из аккаунта")
    @allure.description("Проверяем выход из аккаунта")
    def test_logout(self, driver, create_user):
        password_recovery = PasswordRecoveryPage(driver)
        personal_area = PersonalAreaPage(driver)
        password_recovery.go_to_personal_area()
        personal_area.authorization(create_user)
        password_recovery.go_to_personal_area()
        personal_area.logout()
        assert personal_area.get_current_url() == Url.LOGIN_PAGE
