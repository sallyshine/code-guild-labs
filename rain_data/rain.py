import datetime

if __name__ == '__main__':
    with open('sample.rain') as f:
        raw_rain_data = f.readlines()
        raw_rain_data = [line.strip() for line in raw_rain_data]

    for index, line in enumerate(raw_rain_data):
        if set(line) == set('-'):
            raw_rain_data = raw_rain_data[index +1::]
            break

    data_points = list()

    for data_point in raw_rain_data:
        data = data_point.split(' ')
        data = [item for item in data if item is not '']

        if '-' in data:
            continue

        date = datetime.datetime.strptime(data[0], '%d-%b-%Y')
        data_points.append((date, int(data[1])))

    rainiest_date = max(data_points, key=lambda d: d[1])
    print(f"The most rainy day was: {datetime.datetime.strftime(rainiest_date[0], '%b-%d-%Y')} with {rainiest_date[1] * 0.01} inches.")

    year_totals = dict()

    for data_point in data_points:

        if year_totals.get(data_point[0].year):
            year_totals[data_point[0].year].append(data_point)
        else:
            year_totals[data_point[0].year] = [data_point]

    for year, data_points in year_totals.items():
        rain_total = sum(date[1] for date in data_points)
        year_totals[year] = rain_total

    rainiest_year = max(year_totals.items(), key=lambda x: x[1])
    print(f'The most rainy year was: {rainiest_year[0]} with {rainiest_year[1] * 0.01} inches.')
