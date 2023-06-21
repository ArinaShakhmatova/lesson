import requests
import xml.etree.ElementTree as ET
from contextlib import contextmanager
from datetime import datetime
URL = "http://www.cbr.ru/scripts/XML_daily.asp"
# Valid currency codes
valid_codes = ['USD', 'EUR', 'GBP', 'JPY', 'CHF', 'CNY']
@contextmanager
def get_currency_rate(currency_id):
    today = datetime.today().strftime("%d/%m/%Y")
    url = f"{URL}?date_req={today}"
    response = requests.get(url)
    xml = ET.fromstring(response.content)
    valute = xml.find(f"./Valute[CharCode='{currency_id}']")
    if valute:
        rate = float(valute.find('Value').text.replace(",", "."))
        yield f"(1 шт.) {valute.find('Name').text} стоит(ят) {rate:.4f} руб."
    else:
        yield f"Ошибка: валюта {currency_id} не найдена"
currency_id = input("Введите код валюты: ")
if currency_id not in valid_codes:
    print("Неверный код валюты")
else:
    with get_currency_rate(currency_id) as rate:
        print(rate)