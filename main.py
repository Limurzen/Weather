import requests

# Введите ваш API ключ от OpenWeatherMap
API_KEY = "your_api_key"

# Введите город и страну для которых нужна погода
city = "Moscow"
country = "Russia"

# Запрос на получение текущей погоды
url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

# Извлечение нужных данных из ответа API
temperature = data["main"]["temp"]
description = data["weather"][0]["description"]
humidity = data["main"]["humidity"]
wind_speed = data["wind"]["speed"]

# Вывод полученной информации о погоде
print(f"Temperature: {temperature}°C")
print(f"Description: {description}")
print(f"Humidity: {humidity}%")
print(f"Wind Speed: {wind_speed} m/s")