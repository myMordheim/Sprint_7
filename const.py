class Endpoints:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru'
    LOGIN = f'{MAIN_URL}/api/v1/courier/login'
    CREATE = f'{MAIN_URL}/api/v1/courier'
    DELETE = f'{MAIN_URL}/api/v1/courier/:id'
    GET_ORDERS_COUNT = f'{MAIN_URL}/api/v1/courier/:id/ordersCount'
    FINISH_ORDER = f'{MAIN_URL}/api/v1/orders/finish/:id'
    CANCEL_ORDER = f'{MAIN_URL}/api/v1/orders/cancel'
    GET_ORDERS = f'{MAIN_URL}/api/v1/orders'
    GET_TRACK = f'{MAIN_URL}/api/v1/orders/track'
    ACCEPT_TRACK = f'{MAIN_URL}/api/v1/orders/accept/:id'
    CREATE_ORDER = f'{MAIN_URL}/api/v1/orders'


class Response_message:
    positive_create = '{"ok":true}'
    double_courier_exception = '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
    missing_input = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
    missing_cred = '{"code":400,"message":"Недостаточно данных для входа"}'
    wrong_cred = '{"code":404,"message":"Учетная запись не найдена"}'
