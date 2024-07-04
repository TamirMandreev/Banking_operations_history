from operator import itemgetter
from datetime import datetime

def data_validation(data):
    '''
    Функция data_validation фильтрует список словарей.
    Возвращает список словарей, содержащие ключи state и date.
    :param data: list (список словарей)
    :return: correct_data list (список словарей)
    '''

    # Создать пустой список. В него будем складывать словари,
    # которые пройдут проверку.
    correct_data = []

    # Добавить в correct_data словари, в которых
    # имеются ключи state и date.
    for dct in data:
        if 'state' in dct and 'date' in dct:
            correct_data.append(dct)

    # Возвратить correct_data.
    return correct_data

def get_most_recent_transaction(data):
    '''
    Функция get_most_recent_transaction принимает на вход
    список словарей, сортирует его по ключам state и date и
    возвращает список из 5 последних операций, совершенных клиентом.
    :param data:
    :return:
    '''

    # Отсортировать список словарей data по значениям ключей
    # state и date.
    sorted_data = sorted(data, key=itemgetter('state', 'date'), reverse=True)

    # Получить 5 последних операций.
    most_recent_transaction = sorted_data[0:5]

    # Возвратить 5 последних операций.
    return most_recent_transaction

def show_most_recent_transactions(most_recent_transactions):
    '''
    Функция show_most_recent_transaction принимает на вход
    последние операции и выводит их на экран в формате
    # <дата перевода> <описание перевода>
    # <откуда> -> <куда>
    # <сумма перевода> <валюта>.
    :param most_recent_transactions: list (список словарей)
    :return:
    '''

    for transaction in most_recent_transactions:
        # Сохранить дату в формате день.месяц.год в переменную date.
        date = datetime.fromisoformat(transaction.get('date')).strftime('%d.%m.%Y')

        # Сохранить описание транзакции в переменную description.
        description = transaction.get('description')

        # Сохранить номер счета списания в переменную write_off_account.
        write_off_account = transaction.get('from')
        # Замаскировать номер счета.
        if write_off_account is not None:
            write_off_account_masked = account_masking(write_off_account)


        # Сохранить номер счета получателя в переменную account.
        account = transaction.get('to')
        # Замаскировать номер счета.
        account_masked = account_masking(account)

        # Сохранить сумму транзакции в переменную amount.
        amount  = transaction.get('operationAmount').get('amount')

        # Сохранить валюту перевода в переменную currency.
        currency = transaction.get('operationAmount').get('currency').get('code')

        if write_off_account is not None:
            print(f'{date} {description}\n'
                  f'{write_off_account_masked} -> {account_masked}\n'
                  f'{amount} {currency}')
            print()
        else:
            print(f'{date} {description}\n'
                  f'{account_masked}\n'
                  f'{amount} {currency}')
            print()

def account_masking(account):
    '''
    Функция account_masking принимает на вход номер счета в виде строки
    и возвращает его в замаскированном виде.
    Пример: 1. Счет **8381 2. Maestro 7810 84** **** 5568
    :param account: str
    :return: account str
    '''

    # Разделить строку по пробелам.
    split_string = account.split()

    # Если первое слово == "Счет", то замаскировать счет
    # по первому примеру.
    if split_string[0] == 'Счет':
        num_account = split_string[-1]
        masked_num_account = '**' + num_account[-4:]
        split_string[-1] = masked_num_account
        account = ' '.join(split_string)
        return account
    # Во всех других случаях замаскировать счет
    # по второму варианту.
    else:
        num_account = split_string[-1]
        masked_num_account = (num_account[0:4] + ' '
                              + num_account[4:6] + '**' + ' '
                              + '****' + ' ' + num_account[-4:])
        split_string[-1] = masked_num_account
        account = ' '.join(split_string)

        return account






