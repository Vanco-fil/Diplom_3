import allure
from helpers import created_orders
from pages.base_page import BasePage
from locators.personal_area_locators import PersonalAreaLocators as lk


class PersonalAreaPage(BasePage):

    @allure.step("Авторизуемся пользователем")
    def authorization(self, create_user):
        user_date, resp = create_user
        self.enter_text(lk.EMAIL_INPUT, user_date['email'])
        self.enter_text(lk.PASSWORD_INPUT, user_date['password'])
        self.click_element(lk.LOGIN_BUTTON)
        self.wait_element_visibility(lk.CREATE_ORDER_BUTTON)
        return user_date['email'], user_date['password']

    @allure.step("Авторизоваться и сделать заказ")
    def auth_and_change_order(self, create_user):
        user_date, resp = create_user
        email, password = self.authorization(create_user)
        number = created_orders(resp)
        number = str(number.json()['order']['number'])
        return email, password, number

    @allure.title("Переход по истории заказов")
    def open_history_orders(self):
        self.wait_element_visibility(lk.HISTORY_ORDER)
        self.click_element(lk.HISTORY_ORDER)
        self.wait_element_visibility(lk.HISTORY_ORDER)

    @allure.step("Выход из аккаунта")
    def logout(self):
        self.wait_element_visibility(lk.LOGOUT_BUTTON)
        self.click_element(lk.LOGOUT_BUTTON)
        self.wait_element_visibility(lk.LOGIN_BUTTON)
