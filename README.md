# ForecastHub

ForecastHub is a simple weather dashboard application that enables users to search for weather forecasts of different locations. It fetches real-time weather data from an external API and presents weather information such as temperature, humidity, and wind speed in a visually appealing manner.

## Features

- **Search:** Users can search for weather forecasts of different locations by entering the city name.
- **Real-time Data:** Weather data is fetched from the OpenWeather API, providing accurate and up-to-date information.
- **Visually Appealing:** Weather information is displayed in a clear and visually appealing format, making it easy for users to understand.

## Technologies Used

- **Python:** Backend development using the Flask framework.
- **HTML/CSS:** Frontend styling and layout.
- **OpenWeather API:** External API used to fetch real-time weather data.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/forecasthub.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Obtain an API key from [OpenWeather](https://openweathermap.org/api) and replace `"YOUR_API_KEY_HERE"` in `app.py` with your actual API key.

## Usage

1. Run the application:

   ```bash
   python app.py
   ```

2. Open a web browser and go to `http://127.0.0.1:5000`.
3. Enter the name of the city for which you want to check the weather forecast and click the "Search" button.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
