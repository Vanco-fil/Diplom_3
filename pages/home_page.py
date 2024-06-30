import allure
from pages.base_page import BasePage
from locators.home_locators import HomeLocators as home_locators


class HomePage(BasePage):

    @allure.step("Кликаем на кнопку «Конструктор»")
    def click_on_construct(self):
        self.wait_element_visibility(home_locators.MY_CONSTRUCTOR)
        self.click_element(home_locators.MY_CONSTRUCTOR)
        return self.find_element(home_locators.CONSTRUCTOR_TITLE)

    @allure.step("Кликаем на кнопку «Лента заказов»")
    def click_on_order_list_button(self):
        self.wait_element_visibility(home_locators.ORDER_LIST_BUTTON)
        self.click_element(home_locators.ORDER_LIST_BUTTON)
        return self.get_current_url()

    @allure.step("Кликаем на ингрeдиент на главной странице")
    def click_on_ingredient(self):
        self.click_element(home_locators.BUN)
        self.wait_element_visibility(home_locators.MODAL_INGREDIENT)
        return self.find_element(home_locators.MODAL_INGREDIENT)

    @allure.step("Кликаем на кнопку закрытия модального окна")
    def click_on_close_modal(self):
        self.click_element(home_locators.CLOSE_MODAL_BUTTON)
        self.wait_not_visibility_element(home_locators.MODAL_INGREDIENT)
        return self.find_element(home_locators.CLOSE_MODAL_BUTTON)

    @allure.step("Добавить ингредиент в заказ")
    def add_ingredient_in_order(self):
        self.wait_element_visibility(home_locators.COUNTER_BUN)
        counter = self.get_text(home_locators.COUNTER_BUN)
        self.drag_and_drop(home_locators.BUN, home_locators.ADDITION_AREA_INGREDIENT)
        new_counter = self.get_text(home_locators.COUNTER_BUN)
        return counter, new_counter

    @allure.step("Кликаем на кнопку «Оформить заказ»")
    def click_create_order_btn(self):
        self.wait_element_visibility(home_locators.CREATE_ORDER_BUTTON)
        self.click_element(home_locators.CREATE_ORDER_BUTTON)
        self.wait_element_visibility(home_locators.CREATE_ORDER_MODAL)
        return self.find_element(home_locators.CREATE_ORDER_MODAL)
