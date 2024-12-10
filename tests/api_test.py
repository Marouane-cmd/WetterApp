import requests

# OpenWeatherMap API Details
API_KEY = "3eb9532610b9a0398975097ac251da69"  # Ersetzen Sie dies mit Ihrem korrekten API-Schlüssel
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Parameter für die Anfrage
params = {
    "q": "Berlin",  # Stadtname
    "appid": API_KEY,  # API-Schlüssel
    "units": "metric"  # Optional: Einheit (Celsius)
}

# Anfrage an die API senden
response = requests.get(BASE_URL, params=params)

# Antwort verarbeiten
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Fehler: {response.status_code}, {response.text}")

