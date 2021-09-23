#!/usr/bin/python3
import json
from pathlib import Path
from flask import Flask, request
from config import cfg
from DataFetcher import DataFetcher


app = Flask(__name__)


def get_current_weather(site, city, api_key):
    '''
    Создаёт экземпляр класса DataFetcher, и вызывает метод для получение данных о погоде, \
    затем конвертирует и сохраняет ответ  
    '''
    df = DataFetcher(city, api_key)
    res = df.get_current_weather(site)
    jsoned_data = json.loads(res)
    with open(f'data/{site}_{city}.json', 'w') as outfile:
        json.dump(jsoned_data, outfile)

    return res


def add_info(string, site):
    '''
    Дополнительно указывает тот сайт, с которого была получена информация
    '''
    formatted_string = f'''{string[:-1]},"Data from": {cfg.get(site, 'site_name')}}}'''
    return json.loads(formatted_string)


@app.route('/api/', methods=['GET'])
def api():
    '''
    Получает запрос, парсит параметры, \
    вызывает метод для получения данных с переданными параметрами  
    '''
    dict_args = request.args.to_dict()
    site = dict_args.get('site')
    city = dict_args.get('city')

    if site == cfg.get('openweathermap'):
        api_key = dict_args.get('api_key')

    if site == cfg.get('weatherbit'):
        api_key = dict_args.get('key')

    if site and city and api_key:
        # Проверяем наличие файла с данными, при отсутствии - создаём и заполняем
        file_path = f'data/{site}_{city}.json'
        if Path(file_path).exists():
            with open(file_path) as json_file:
                res = json.load(json_file)
        else:
            res = add_info(
                get_current_weather(
                    site=site,
                    city=city,
                    api_key=api_key),
                site=site
            )
        return res

    raise ValueError("Params error")


if __name__ == '__main__':
    app.run(debug=cfg.FLASK_DEBUG_MODE)
