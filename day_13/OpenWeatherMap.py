import requests

city = input("Enter city name: ")
api_key = "4949c59529d5488d5bb899d1dac14483"  # put your real key here

# Base URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Send GET request
response = requests.get(url)

# Convert to JSON
data = response.json()

if data['cod'] == 200:
    print("✅ Weather Details for", city)
    print("Latitude:", data['coord']['lat'])
    print("Longitude:", data['coord']['lon'])
    print("Temperature:", data['main']['temp'], "°C")
    print("Condition:", data['weather'][0]['description'])
    print("Humidity:", data['main']['humidity'], "%")
else:
    print("❌ Error:", data['message'])