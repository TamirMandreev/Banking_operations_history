from src.utils import data_validation, get_most_recent_transaction, account_masking
import pytest

list_dct = [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },{
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }, {
    "id": 939719570,
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  },
  {
    "id": 587085106,
    "state": "EXECUTED",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  }]

list_dct_expected = [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },{
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }]

def test_data_validation():
    assert data_validation(list_dct) == list_dct_expected


list_dct_2 = [{"state": "EXECUTED", "date": "2019-07-03T18:35:29.512364", "id": 1},
            {"state": "EXECUTED", "date": "2021-07-03T18:35:29.512364", "id": 2},
            {"state": "EXECUTED", "date": "2021-08-03T18:35:29.512364", "id": 3},
            {"state": "EXECUTED", "date": "2022-07-04T18:35:29.512364", "id": 4},
            {"state": "EXECUTED", "date": "2022-07-03T18:35:29.512364", "id": 5},
            {"state": "EXECUTED", "date": "2023-07-03T18:35:29.512364", "id": 6},
            {"state": "CANCELED", "date": "2024-07-06T18:35:29.512364", "id": 7}]

list_dct_expected_2 = [{"state": "EXECUTED", "date": "2023-07-03T18:35:29.512364", "id": 6},
                     {"state": "EXECUTED", "date": "2022-07-04T18:35:29.512364", "id": 4},
                     {"state": "EXECUTED", "date": "2022-07-03T18:35:29.512364", "id": 5},
                     {"state": "EXECUTED", "date": "2021-08-03T18:35:29.512364", "id": 3},
                     {"state": "EXECUTED", "date": "2021-07-03T18:35:29.512364", "id": 2}]
def test_get_most_recent_transaction():
    assert get_most_recent_transaction(list_dct_2) == list_dct_expected_2


def test_account_masking():
    assert account_masking("Visa Classic 6831982476737658") == 'Visa Classic 6831 98** **** 7658'
    assert account_masking('Счет 72082042523231456215') == 'Счет **6215'
    assert account_masking('Maestro 3928549031574026') == 'Maestro 3928 54** **** 4026'