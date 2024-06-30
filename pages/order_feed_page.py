import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators as order_locators


class OrderFeedPage(BasePage):

    @allure.step("Кликаем на заказ")
    def click_on_order(self):
        self.wait_element_visibility(order_locators.FIRST_ORDER)
        self.find_element(order_locators.FIRST_ORDER).click()
        self.wait_element_visibility(order_locators.MODAL_CONTAINER_ORDER)
        return self.find_element(order_locators.MODAL_CONTAINER_ORDER)

    @allure.step("Ищем все заказы")
    def all_order_text(self):
        self.wait_element_visibility(order_locators.ALL_ORDERS)
        return self.return_locators_text(order_locators.ALL_ORDERS)

    @allure.step("Число выполненных заказов за все время")
    def number_orders_all_time(self):
        self.wait_element_visibility(order_locators.ORDER_ALL_TIME)
        return self.get_text(order_locators.ORDER_ALL_TIME)

    @allure.step("Число выполненных заказов за сегодня")
    def number_orders_today(self):
        self.wait_element_visibility(order_locators.ORDER_TODAY_TIME)
        return self.get_text(order_locators.ORDER_TODAY_TIME)

    @allure.step("Проверяем полку с готовящимися заказами")
    def check_order_progress_section(self):
        self.wait_element_visibility(order_locators.ORDERS_PROGRESS_SECTION)
        return self.return_locators_text(order_locators.ORDERS_PROGRESS_SECTION)

    @allure.step("Создаем список всех готовящихся заказов")
    def return_locators_text(self, locator):
        all_locators = self.find_all_element(locator)
        locator_text = []
        for order in all_locators:
            locator_text.append(order.text)
        return locator_text
