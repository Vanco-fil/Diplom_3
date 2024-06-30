import allure
from data import Url
from pages.home_page import HomePage
from pages.password_recovery_page import PasswordRecoveryPage
from pages.personal_area_page import PersonalAreaPage


class TestHome:

    @allure.title("Переход по клику на «Конструктор»")
    @allure.description("Проверяем возможность перехода по кнопке «Конструктор»")
    def test_click_button_construct(self, driver):
        home = HomePage(driver)
        password_recovery = PasswordRecoveryPage(driver)
        password_recovery.go_to_personal_area()
        assert home.click_on_construct()

    @allure.title("Переход по клику на «Лента заказов»")
    @allure.description("Проверяем возможность перехода на страницу ленты заказов")
    def test_click_button_list_order(self, driver):
        home = HomePage(driver)
        home.click_on_order_list_button()
        assert home.get_current_url() == Url.FEED_PAGE

    @allure.title("Открытие модального окна при клике на ингредиент")
    @allure.description("Проверяем, что при клике на ингредиент, появится всплывающее окно с деталями")
    def test_click_on_ingredient(self, driver):
        home = HomePage(driver)
        assert home.click_on_ingredient()

    @allure.title("Закрытие модального окна ингредиента")
    @allure.description("Проверяем закрытия модального окна кликом на крестик")
    def test_click_close_btn_modal(self, driver):
        home = HomePage(driver)
        home.click_on_ingredient()
        assert home.click_on_close_modal()

    @allure.title("Добавление ингредиента в заказ")
    @allure.description("Проверяем, что при добавлении ингредиента в заказ счетчик кол-ва увеличивается")
    def test_check_counter_ingredients(self, driver):
        home = HomePage(driver)
        counter = home.add_ingredient_in_order()
        assert int(counter[0]) == 0 and int(counter[1]) == 2

    @allure.title("Залогиненный пользователь оформляет заказ")
    @allure.description("Проверяем, что есть возможность оформить заказ авторизованным пользователем")
    def test_create_order_authorized_user(self, driver, create_user):
        home = HomePage(driver)
        personal_area = PersonalAreaPage(driver)
        password_recovery = PasswordRecoveryPage(driver)
        password_recovery.go_to_personal_area()
        personal_area.authorization(create_user)
        home.add_ingredient_in_order()
        assert home.click_create_order_btn()
