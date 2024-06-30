from selenium.webdriver.common.by import By


class HomeLocators:

    # Кнопка "Конструктор" на главной странице
    MY_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")

    # Заголовок "Соберите бургер" на главной странице
    CONSTRUCTOR_TITLE = (By.CSS_SELECTOR, "h1.text.text_type_main-large.mb-5.mt-10")

    # Кнопка "Лента заказов" на главной странице
    ORDER_LIST_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")

    # Заголовок страницы с заказами
    HEADER_ORDER_LIST = (By.XPATH, "//h1[text()='Лента заказов']")

    # Карточка булки на странице конструктора
    BUN = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")

    # Модальное окно с деталями ингредиента
    MODAL_INGREDIENT = (By.XPATH, "//h2[text()='Детали ингредиента']")

    # Крестик закрытия модального окна
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class, 'close')]")

    # Область добавления ингредиентов
    ADDITION_AREA_INGREDIENT = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__29Cd7')]")

    # Контейнер ингредиента
    COUNTER_BUN = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")

    # Кнопка "Оформить заказ"
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    # Модальное окно подтверждения заказа
    CREATE_ORDER_MODAL = (By.CLASS_NAME, "Modal_modal__container__Wo2l_")
