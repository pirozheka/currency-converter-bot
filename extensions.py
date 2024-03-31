import requests
import json
from config import API_KEY, currencies

class APIException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def get_price(base, quote, amount):
        #Убираем большие буквы
        try: 
            base_currency = base.lower()
        except ValueError:
            raise APIException(f'Наименование валюты должно быть строкой')
        
        try:
            quote_currency = quote.lower()
        except ValueError:
            raise APIException(f'Наименование валюты должно быть строкой')

        #Проверка корректности введенных данных
            #Если введены одинаковые валюты: 
        if quote_currency == base_currency:
            raise APIException(f'Невозможно перевести одинаковые валюты: {base}.')
        
            #Если введена валюта, которой нет в списке доступных для перевода валют:
        try:
            base_ticker = currencies[base_currency]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')
        
        try:
            quote_ticker = currencies[quote_currency]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

            #Если введено не число:
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')    
                     
        #Формирование запроса к API из документации
        url = f'https://api.apilayer.com/exchangerates_data/convert?to={quote_ticker}&from={base_ticker}&amount={amount}'
        payload = {}
        headers = {
            "apikey": API_KEY
        }
        response = requests.request("GET", url, headers=headers, data = payload)

        #Вытаскиваем значение result из словаря
        total_amount = json.loads(response.content)['result']

        #Возвращаем округленное значение
        return round(total_amount, 2)

