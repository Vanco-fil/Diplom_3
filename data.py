class Url:
    URL = 'https://stellarburgers.nomoreparties.site'
    LOGIN_PAGE = f'{URL}/login'
    HISTORY_PAGE = f'{URL}/account/order-history'
    FEED_PAGE = f'{URL}/feed'


class Ingredients:
    FLUOR_BUN = "61c0c5a71d1f82001bdaaa6d"
    BIO_CUTLET = '61c0c5a71d1f82001bdaaa71'
    SAUCE_SPICY = '61c0c5a71d1f82001bdaaa72'
    INVALID_HASH = '11c1c1a11d1f11001bdaaa1'


class API:
    PAGE = 'https://stellarburgers.nomoreparties.site'
    CREATE_USER = f'{PAGE}/api/auth/register'
    CREATE_ORDER = f'{PAGE}/api/orders'
    DELETE_DATA = f'{PAGE}/api/auth/user'
