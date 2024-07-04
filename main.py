# Это backend часть виджета,
# который показывает 5 последних
# успешных банковских операций клиента.

import json
from pprint import pprint
from utils import (data_validation, get_most_recent_transaction,
                   show_most_recent_transactions)


# Главная функция.
def main():

    # Открыть json файл в режиме чтения в переменную file.
    with open('operations.json', 'r') as file:
        # Загрузить содержимое file в переменную data.
        data = json.load(file)

    # Проверить данные на наличие ключей date и state.
    # Прошедшие проверку данные поместить в переменную correct_data.
    correct_data = data_validation(data)

    # Получить 5 последних выполненных операций.
    most_recent_transactions = get_most_recent_transaction(correct_data)

    # Вывести на экран 5 последних транзакций в формате
    # <дата перевода> <описание перевода>
    # <откуда> -> <куда>
    # <сумма перевода> <валюта>.
    show_most_recent_transactions(most_recent_transactions)


if __name__ == '__main__':
    main()