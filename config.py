#!/usr/bin/python3


class Config():
    FLASK_DEBUG_MODE = True
    
    data = {
        'openweathermap': {
            'site': 'api.openweathermap.org/data/2.5/weather',
            'site_name': '"openweathermap"',
            'base_pref': 'http://',
        },
        'weatherbit': {
            'site': 'api.weatherbit.io/v2.0/current',
            'site_name': '"weatherbit"',
            'base_pref': 'https://',
        },
    }

    def get(self, site, key=''):
        if key != '':
            return self.data.get(site).get(key)
        
        if key == '' and self.data.get(site) != None:
            return site
        else:
            raise ValueError("This site doesn't exist")

# Export Config instance
cfg = Config()
