from selenium.webdriver.common.by import By


class OrderFeedLocators:

    # Первый заказ из списка заказов
    FIRST_ORDER = (By.XPATH, "//div/ul/li[1]")

    # Все заказы
    ALL_ORDERS = (By.XPATH, "//*[contains(@class, 'text text_type_digits-default')]")

    # Счетчик заказов "Выполнено за все время"
    ORDER_ALL_TIME = (By.XPATH, "//div/div[2]/p[2]")

    # Счетчик заказов "Выполнено за сегодня"
    ORDER_TODAY_TIME = (By.XPATH, "//p[contains(@class, 'text_type_main') and contains(text(), 'Выполнено за сегодня')]/following-sibling::p[contains(@class, 'text_type_digits-large')]")

    # Секция всех готовящихся заказов
    ORDERS_PROGRESS_SECTION = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]//li[contains(@class, 'text_type_digits-default')]")

    # Текст в секции готовящихся заказов
    ORDERS_PROGRESS_SECTION_TEXT = (By.XPATH, "//*[text() = 'Все текущие заказы готовы!']")

    # Модальное окно заказа с деталями
    MODAL_CONTAINER_ORDER = (By.XPATH, ".//div[contains(@class, 'Modal_orderBox__1xWdi')]")
