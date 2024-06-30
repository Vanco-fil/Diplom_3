## Дипломный проект. Задание 3: веб-приложение

### Тестируем UI сайта [Stellar Burgers](https://stellarburgers.nomoreparties.site)

### Структура проекта

- `conftest` - Cтартовая фикстура на два браузера(Chrome, Firefox), генерация данных для создание пользователя, после теста пользователь удаляется. 
- `tests` - Пакет, содержащий тесты
- `data` - Содержит cтатические данные для тестов
- `allure_results` - Содержит отчеты по тестированию 
- `helpers` - Содержит вспомогательные методы, которые помогают генерировать данные
- `pages` - Содержит классы с методами для тестов

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Можно установить в ручную библиотеки pytest,  requests и allure-pytest**

>  `$ pip install pytest`
> 
>  `$ pip install allure-pytest`
> 
>  `$ pip install requests` 

**Запустить все автотесты**

>  `$ pytest tests`

**Генерация отчета в формате веб-страницы**

>  `$ allure serve allure_results `