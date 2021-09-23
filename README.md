## api-test-task
Ручное развёртывание:

> python3 -m venv venv
> source venv/bin/activate
> pip3 install -r requirements.txt
> python3 main.py

Развёртывание в контейнере через docker(как обычно):

> docker build ...
> docker run ...
> etc

## Если запускать на условном хостинге, то route для получения данных будет выглядеть следующим образом:

# Примеры для формирования запроса
>http://{SERVER ADDRES}/api/?site=openweathermap&city={CITY}&api_key={YOUR API_KEY} 
>http://{SERVER ADDRES}/api/?site=weatherbit&city={CITY}&key={YOUR API_KEY}

# На примере локалхоста
>http://127.0.0.1:5000/api/?site=openweathermap&city=Moscow&api_key=7d13853f3f6b5950f0545e63df61fb0d
>http://127.0.0.1:5000/api/?site=weatherbit&city=Moscow&key=2f2973413961474e8a2551a6ca4dda61

>Результатом GET запроса будут актуальные метео-данные с любого из метео-сайтов.