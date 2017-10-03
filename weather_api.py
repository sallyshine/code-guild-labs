import requests
import pytemperature

city = input('What city?: \n')
temp = input("Which temp format? C or F?: \n").lower()

package = {
    'APPID': "8b447aaba14ad1e178b186031642d0de",
    'q': city
}

r = requests.post('http://api.openweathermap.org/data/2.5/weather', params=package)
data = r.json()
print('Condition: ' + data['weather'][0]['main'])

if temp == 'c':
    print('Temp: ' + str(pytemperature.k2c(int(data['main']['temp']))))
elif temp == 'f':
    print('Temp: ' + str(pytemperature.k2f(int(data['main']['temp']))))

if data['wind']['deg'] >= 0 and data['wind']['deg'] <= 25:
    print('Wind Direction: North')
elif data['wind']['deg'] > 25 and data['wind']['deg'] <= 68:
    print('Wind Direction: Northeast')
elif data['wind']['deg'] > 68 and data['wind']['deg'] <= 110:
    print('Wind Direction: East')
elif data['wind']['deg'] > 110 and data['wind']['deg'] <= 150:
    print('Wind Direction: Southeast')
elif data['wind']['deg'] > 150 and data['wind']['deg'] <= 205:
    print('Wind Direction: South')
elif data['wind']['deg'] > 205 and data['wind']['deg'] <= 245:
    print('Wind Direction: Southwest')
elif data['wind']['deg'] > 245 and data['wind']['deg'] <= 295:
    print('Wind Direction: West')
elif data['wind']['deg'] > 295 and data['wind']['deg'] <= 335:
    print('Wind Direction: Northwest')
elif data['wind']['deg'] > 335 and data['wind']['deg'] <= 360:
    print('Wind Direction: North')
# print(data['main']['temp'])
# print(data['wind']['deg'])
#condition
#temp
#wind direction
