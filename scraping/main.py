import requests
import time

from bs4 import BeautifulSoup

def get_by_class(tags, class_name):
    for tag in tags.find_all():
        if class_name in tag.get('class', ''):
            return tag

def get_forecast(day):
    forecast = dict()
    weather_data = get_by_class(day, 'short')

    forecast['condition'] = get_by_class(weather_data, 'wx-text').text
    forecast['high'] = get_by_class(weather_data, 'wx-high').text
    forecast['low'] = get_by_class(weather_data, 'wx-low').text
    forecast['precip'] = get_by_class(weather_data, 'wx-precip').text

    date = get_by_class(day, 'dateTime').get('data-time')
    date = time.gmtime(int(date[0:-3])) #because of random extra zeros
    forecast['date'] = time.strftime("%x", date)

    return forecast

def get_daily_forecasts():
    response = requests.get("http://katu.com/weather")
    response.raise_for_status()
    html = BeautifulSoup(response.text, 'html.parser')

    return [div for div in html.find_all('div')
            if 'daily-forecast' in div.get('class', '')]

if __name__ == '__main__':
    print(f'''
    __________________  ____  ___
    \______   \______ \ \   \/  /
     |     ___/|    |  \ \     /
     |    |    |    `   \/     \ 
     |____|   /_______  /___/\  \   WEATHER
                      \/      \_/''')
    daily_forecasts = get_daily_forecasts()

    for day in daily_forecasts:
        forecast = get_forecast(day)
        print(f'''{"-" * 30}
Forecast for {forecast['date']}:
    {forecast['condition']}
    High: {forecast['high']}
    Low: {forecast['low']}
    Chance of Precip: {forecast['precip']}''')

# wx-cur-icon: daily_conditions
#
