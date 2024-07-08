import allure
from helpers import generate_user_data
from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators as recovery_pass


class PasswordRecoveryPage(BasePage):

    @allure.title("Переходим в личный кабинет")
    def go_to_personal_area(self):
        self.wait_element_visibility(recovery_pass.MY_OFFICE_BUTTON)
        self.click_element(recovery_pass.MY_OFFICE_BUTTON)

    @allure.title("Переходим по кнопке 'Восстановить пароль'")
    def click_and_wait_recovery_button(self):
        self.wait_element_visibility(recovery_pass.RECOVERY_PASSWORD_LINK)
        self.click_element(recovery_pass.RECOVERY_PASSWORD_LINK)
        return self.find_element(recovery_pass.RECOVERY_PASSWORD_HEADER)

    @allure.title("Вводим емейл в поле ввода и тапаем по кнопке восстановления пароля")
    def input_email_and_click_recovery_btn(self):
        self.wait_element_visibility(recovery_pass.EMAIL_INPUT)
        self.click_element(recovery_pass.EMAIL_INPUT)
        user_data = generate_user_data()
        self.enter_text(recovery_pass.EMAIL_INPUT, user_data['email'])
        self.click_element(recovery_pass.RECOVERY_BUTTON)
        self.wait_element_visibility(recovery_pass.PASSWORD_INPUT)
        return self.find_element(recovery_pass.PASSWORD_INPUT)

    @allure.title("Вводим рандомный пароль в поле пароль")
    def input_password(self):
        self.wait_element_visibility(recovery_pass.PASSWORD_INPUT)
        user_data = generate_user_data()
        self.enter_text(recovery_pass.PASSWORD_INPUT, user_data['password'])

    @allure.step("Кликаем на иконку глаза рядом с инпутом пароля, чтобы сделать его видимым")
    def click_on_eye_icon_password(self):
        self.click_element(recovery_pass.EYE_BUTTON)
        return self.find_element(recovery_pass.VISIBLE_PASS_INPUT)
