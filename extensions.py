import requests
import json

from config import keys


class ConvertionException(Exception):
    pass


class CoursesConverter:
    @staticmethod
    def convert(base: str, quote: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        '''По техническим причинам запрос к API, предоставленный в ТЗ работает только на базовую валюту EUR'''
        r = requests.get(
            f'http://api.exchangeratesapi.io/v1/latest?access_key=c60fc97ee87d676e043c909d5993e76f&base={base_ticker}&symbols={quote_ticker}')

        summ = round(json.loads(r.content)['rates'][keys[quote]] * amount, 2)

        return summ