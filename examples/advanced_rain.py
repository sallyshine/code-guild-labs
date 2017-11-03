import datetime
import itertools
from collections import namedtuple

import requests
from bs4 import BeautifulSoup


RainDataPoint = namedtuple('RainDataPoint', 'date, total, hourly')

class RainDataParser:
    @staticmethod
    def get_raw_data(file_name):
        with open(file_name, 'r') as rain_file:
            raw_data = rain_file.readlines()
            raw_data = [line.strip() for line in raw_data]

        for index, line in enumerate(raw_data):
            if set(line) == set('-'):
                raw_data = raw_data[index + 1::]

        data = list()
        for line in raw_data:
            line = line.split(' ')
            line = [string for string in line if string is not '']

            if '-' in line:
                continue

            data.append(line)

        return data

    @staticmethod
    def parse_data(data):
        data_points = list()

        for day in data:
            data_point_date = datetime.datetime.strptime(day[0], '%d-%b-%Y')
            data_point_total = int(day[1])
            data_point_hourly = [int(hour) for hour in day[2::]]  # Gets the 24 hour totals as ints.

            point = RainDataPoint(
                date=data_point_date,
                total=data_point_total,
                hourly=data_point_hourly
                )

            data_points.append(point)

        return data_points

if __name__ == '__main__':
    data = RainDataParser.get_raw_data('sample.rain')
    data_points = RainDataParser.parse_data(data)

    rainiest_day = max(data_points, key=lambda d: d.date)
    print(rainiest_day)

    # Must sort by the attribute you want to groupby.
    data_points = sorted(data_points, key=lambda d: d.date)
    for year, data in itertools.groupby(data_points, key=lambda d: d.date.year):
        print(year, sum(day.total for day in data))


    # The rainiest day on average.
    rainy_days = dict()
    for day in data_points:
        rainy_days[(day.date.month, day.date.day)] = \
            rainy_days[(day.date.month, day.date.day)] + [day] \
            if rainy_days.get((day.date.month, day.date.day)) else [day]

    for day, data in rainy_days.items():
        rainy_days[day] = sum(d.total for d in data) / len(data)

    rainiest_day_on_average = max(rainy_days.items(), key=lambda d: d[1])
    rainiest_day_on_average = list(rainiest_day_on_average)
    rainiest_day_on_average[0] = datetime.datetime.strftime(
        datetime.datetime.strptime('-'.join([str(x) for x in rainiest_day_on_average[0]]), '%m-%d'),
        "%d-%b"
        )

    print(f'The rainiest day on average was: {rainiest_day_on_average[0]} with {rainiest_day_on_average[1] * 0.01} inches of rain.')
