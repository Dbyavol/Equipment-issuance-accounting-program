import json
from . import db_api
from alternative.alternative_board_finder import find_alternative_board

def validate_location(request_data: dict) -> int:
    """
    Проверяет существование указанной аудитории в базе данных.
    
    :param request_data: Словарь с данными запроса
    :return: ID аудитории, если найдена
    :raises ValueError: Если аудитория не найдена
    """
    location = request_data.get('Аудитория')
    for loc in db_api.fetch_location():
        if location == loc.get('name'):
            return loc.get('id')
    raise ValueError("Аудитория не найдена")

def validate_hardware(request_data: dict):
    """
    Проверяет наличие указанной платы в базе данных.
    
    :param request_data: Словарь с данными запроса
    :return: ID найденной платы и требуемое количество либо альтернативная плата
    :raises TypeError: Если плата или альтернативы не найдены
    """
    hardware_name, quantity = request_data.get('Плата'), request_data.get('Количество')
    try:
        hardwares, hardware, hardware_id, available = check_availability(hardware_name, quantity)
    except TypeError:
        raise TypeError("Не найдена плата с таким названием!")
    
    if available:
        return hardware_id, quantity
    
    alternative_board_name = find_alternative_board(hardware, hardwares)
    if alternative_board_name:
        _, _, _, alternative_available = check_availability(alternative_board_name, quantity)
        if alternative_available:
            return alternative_board_name
    raise TypeError("Не найдено альтернативных плат!")

def validate_user(request_data: dict) -> dict:
    """
    Проверяет существование пользователя в базе данных, при необходимости создаёт нового.
    
    :param request_data: Словарь с данными запроса
    :return: Данные пользователя
    """
    firstname, lastname = request_data.get('Имя'), request_data.get('Фамилия')
    response = db_api.fetch_user(firstname, lastname)
    
    if response.status_code == 200 and not response.json():
        return create_user(firstname, lastname, request_data.get('Отчество'), request_data.get('Почта'), request_data.get('Телефон'))
    return response.json()[0]

def create_user(fname: str, lname: str, patronymic: str, email: str, phone: str) -> dict:
    """
    Создаёт нового пользователя в базе данных.
    
    :param fname: Имя пользователя
    :param lname: Фамилия пользователя
    :param patronymic: Отчество пользователя
    :param email: Электронная почта пользователя
    :param phone: Телефон пользователя
    :return: Данные созданного пользователя
    """
    user_data = {
        "active": True, "type": "user", "first_name": fname, "last_name": lname,
        "patronymic": patronymic, "image_link": "https://cdn4.iconfinder.com/data/icons/student-ui/1173/student_profile-512.png",
        "email": email, "phone": phone, "card_id": "string", "card_key": "string", "comment": ""
    }
    print("User was added to database")
    return db_api.post_user(json.dumps(user_data, ensure_ascii=False))

def check_availability(hardware_name: str, quantity: int) -> tuple:
    """
    Проверяет наличие указанной платы в базе данных.
    
    :param hardware_name: Название платы
    :param quantity: Требуемое количество
    :return: Кортеж (список плат, конкретная плата, ID платы, доступность)
    :raises TypeError: Если плата отсутствует в базе
    """
    hardwares, stock = db_api.fetch_hardware(), db_api.fetch_stock()
    
    for hw in hardwares:
        if hw.get('name') == hardware_name:
            hw_id = hw.get('id')
            break
    else:
        raise TypeError("Ошибка: Плата не найдена")
    
    available_total = sum(st.get('available_total', 0) for st in stock if st.get('hardware') == hw_id)
    return hardwares, hw, hw_id, available_total >= quantity