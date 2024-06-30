import allure

from pages.home_page import HomePage
from pages.order_feed_page import OrderFeedPage
from pages.password_recovery_page import PasswordRecoveryPage
from pages.personal_area_page import PersonalAreaPage


class TestOrderFeed:

    @allure.title("Отображение деталей заказа при клике на него")
    @allure.description("Проверяем, что при клике на заказ откроется всплывающее окно с деталями")
    def test_click_on_order(self, driver):
        home = HomePage(driver)
        order_feed = OrderFeedPage(driver)
        home.click_on_order_list_button()
        assert order_feed.click_on_order()

    @allure.title("Отображение заказов пользователя в «История заказов»")
    @allure.description("Проверяем, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_user_order_in_list_order(self, driver, create_user):
        home = HomePage(driver)
        order_feed = OrderFeedPage(driver)
        personal_area = PersonalAreaPage(driver)
        password_recovery = PasswordRecoveryPage(driver)
        password_recovery.go_to_personal_area()
        number = personal_area.auth_and_change_order(create_user)
        number = '#0' + number[-1]
        home.click_on_order_list_button()
        order_texts = order_feed.all_order_text()
        assert number in order_texts

    @allure.title("Проверка счетчика заказа за все время")
    @allure.description("Проверяем работу счетчика выполненных заказов за все время заказов")
    def test_checking_orders_counter_all_time(self, driver, create_user):
        home = HomePage(driver)
        order_feed = OrderFeedPage(driver)
        personal_area = PersonalAreaPage(driver)
        password_recovery = PasswordRecoveryPage(driver)
        home.click_on_order_list_button()
        counter_orders = order_feed.number_orders_all_time()
        password_recovery.go_to_personal_area()
        personal_area.auth_and_change_order(create_user)
        home.click_on_order_list_button()
        new_counter_orders = order_feed.number_orders_all_time()
        assert int(new_counter_orders) > int(counter_orders)

    @allure.title("Проверка счетчика заказа за сегодня")
    @allure.description("Проверяем работу счетчика выполненных заказов за сегодня")
    def test_checking_order_counter_today(self, driver, create_user):
        home = HomePage(driver)
        order_feed = OrderFeedPage(driver)
        personal_area = PersonalAreaPage(driver)
        password_recovery = PasswordRecoveryPage(driver)
        home.click_on_order_list_button()
        counter_orders = order_feed.number_orders_today()
        password_recovery.go_to_personal_area()
        personal_area.auth_and_change_order(create_user)
        home.click_on_order_list_button()
        new_counter_orders = order_feed.number_orders_today()
        assert int(new_counter_orders) > int(counter_orders)

    @allure.title("Оформленный заказаз появляется в разделе 'В работе'")
    @allure.description("Проверяем, что после оформления заказа его номер появляется в разделе готовящихся заказов 'В работе'")
    def test_check_create_order_progress_section(self, driver, create_user):
        home = HomePage(driver)
        order_feed = OrderFeedPage(driver)
        personal_area = PersonalAreaPage(driver)
        password_recovery = PasswordRecoveryPage(driver)
        password_recovery.go_to_personal_area()
        number = personal_area.auth_and_change_order(create_user)
        number = '0' + number[-1]
        home.click_on_order_list_button()
        order_feed.all_order_text()
        order_number = order_feed.check_order_progress_section()
        assert number in order_number
