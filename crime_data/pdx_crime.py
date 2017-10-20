import glob
import csv
from datetime import datetime

if __name__ == '__main__':
    raw_crime_data = glob.glob('*.csv')

    incidents = list()

    for csv_file in raw_crime_data:
        with open(csv_file) as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                incidents.append(row)

    new_incidents = list()

    for data_point in incidents:
        date = datetime.strptime(data_point[1], '%m/%d/%Y')
        new_incidents.append((date, data_point[3]))

    frequency = dict()

    for crime in new_incidents:
        if frequency.get(crime[1]):
            frequency[crime[1]] += 1
        else:
            frequency[crime[1]] = 1

    most_common = max(frequency.items(), key=lambda x: x[1])
    print(f'The most common crime between 2011-2014 was {most_common[0]} with {most_common[1]} instances.')

    least_common = min(frequency.items(), key=lambda x: x[1])
    print(f'The least common crime between 2011-2014 was {least_common[0]} with {least_common[1]} instances.')

    # year_totals = dict()
    #
    # for crime in new_incidents:
    #
    #     if year_totals.get(crime[0].year):
    #         year_totals[crime[0].year].append(crime)
    #     else:
    #         year_totals[crime[0].year] = [crime]
    #
    # for year, crime in year_totals.items():
    #     crime_total = sum(date[1] for date in new_incidents)
    #     year_totals[year] = crime_total
    #
    # most_crime_year = max(year_totals.items(), key=lambda x: x[1])
    # print(f'The year with the most crime between 2011-2014 was {year_totals[0]} with {year_totals[1]} instances.')
