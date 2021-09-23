#!/usr/bin/python3
from config import cfg
import requests


class DataFetcher():
    _city = ''
    _api_key = ''

    def __init__(self, city, api_key) -> None:
        self._city = city
        self._api_key = api_key

    def get_current_weather(self, site):
        '''
        Собирает url, делает запрос и получает данные с метео-сайта 
        '''
        if site == cfg.get('openweathermap'):
            response = requests.get(
                f"{cfg.get(site, 'base_pref')}{cfg.get(site, 'site')}?q={self._city}&appid={self._api_key}"
            )
            return response.text

        elif site == cfg.get('weatherbit'):
            response = requests.get(
                f"{cfg.get(site, 'base_pref')}{cfg.get(site, 'site')}?city={self._city}&key={self._api_key}"
            )
            return response.text
        else:
            raise ValueError("Bad site")
