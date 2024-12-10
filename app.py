from flask import Flask, render_template, request, jsonify

import requests


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wetter', methods=['GET'])
def wetter():
    stadt = request.args.get('stadt', 'Berlin')  # Standardstadt ist Berlin
    api_key = "3eb9532610b9a0398975097ac251da69"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": stadt,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Daten konnten nicht abgerufen werden"}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

