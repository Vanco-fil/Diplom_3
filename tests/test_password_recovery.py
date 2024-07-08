import allure
from pages.password_recovery_page import PasswordRecoveryPage


class TestPasswordRecovery:
    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    @allure.description("Проверяем возможность перехода по кнопке «Восстановить пароль»")
    def test_click_on_btn_recovery_page(self, driver):
        password_recovery = PasswordRecoveryPage(driver)
        password_recovery.go_to_personal_area()
        assert password_recovery.click_and_wait_recovery_button()

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    @allure.description("Проверяем возможность восстановить пароль по почте")
    def test_input_email_and_click_on_recovery_btn(self, driver):
        password_recovery = PasswordRecoveryPage(driver)
        password_recovery.go_to_personal_area()
        password_recovery.click_and_wait_recovery_button()
        assert password_recovery.input_email_and_click_recovery_btn()

    @allure.title("Клик по кнопке показать/скрыть пароль делая поле активным")
    @allure.description("Проверяем что после клика по иконке глаза инпут пароля подсвечивается")
    def test_click_password_visible_button(self, driver):
        password_recovery = PasswordRecoveryPage(driver)
        password_recovery.go_to_personal_area()
        password_recovery.click_and_wait_recovery_button()
        password_recovery.input_email_and_click_recovery_btn()
        password_recovery.input_password()
        assert password_recovery.click_on_eye_icon_password()
