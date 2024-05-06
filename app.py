from flask import Flask, render_template, request

app = Flask(__name__)

def get_mock_weather(city):
    
    mock_data = {
        "New York": {"temperature": 25, "humidity": 50, "wind_speed": 10, "description": "Sunny"},
        "London": {"temperature": 18, "humidity": 70, "wind_speed": 5, "description": "Cloudy"},
        "Tokyo": {"temperature": 30, "humidity": 60, "wind_speed": 15, "description": "Rainy"}
    }
    return mock_data.get(city, {"error": "City not found"})

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def weather():
    city = request.form["city"]
    weather_data = get_mock_weather(city)
    return render_template("weather.html", weather_data=weather_data)

API_KEY = "YOUR_API_KEY_HERE"

if API_KEY == "YOUR_API_KEY_HERE":
    raise ValueError("Please replace 'YOUR_API_KEY_HERE' with your actual OpenWeather API key")

if __name__ == "__main__":
    app.run(debug=True)
