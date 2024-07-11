# Google Maps Enhanced Insights 📍➡️📍

This Streamlit application calculates the distance between two locations and provides additional insights such as traffic, weather, hotels, and restaurants using the Google Maps API and OpenWeatherMap API.

## Features

- Calculate the distance and duration between two locations.
- Display the current weather at both the origin and destination.
- List nearby hotels and restaurants at both the origin and destination.
- Display a map preview of the specified locations.

## Prerequisites

- Python 3.7 or higher
- Google Cloud Platform account
- OpenWeatherMap account

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/google-maps-enhanced-insights.git
    cd google-maps-enhanced-insights
    ```

2. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up API keys:**

    - Create a `.env` file in the root directory of the project and add your API keys:

        ```plaintext
        GOOGLE_MAPS_API_KEY=your_google_maps_api_key
        WEATHER_API_KEY=your_weather_api_key
        ```

## Usage

1. **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

2. **Open your web browser and go to:**

    ```
    http://localhost:8501
    ```

3. **Enter the origin and destination locations in the provided input fields and click "Get Insights 🚗".**

## Project Structure

- `app.py`: The main application file containing the Streamlit app code.
- `requirements.txt`: The file listing all required Python packages.
- `.env`: File to store your API keys (not included in the repository).

## API Configuration

### Google Maps API

1. **Create a Google Cloud Project:**

    - Go to the [Google Cloud Console](https://console.cloud.google.com/).
    - Create a new project.

2. **Enable APIs:**

    - Enable the following APIs:
        - Maps JavaScript API
        - Places API
        - Distance Matrix API
        - Directions API

3. **Create API Key:**

    - Go to the **Credentials** page.
    - Create a new API key and copy it.
    - Add the API key to your `.env` file.

### OpenWeatherMap API

1. **Create an OpenWeatherMap Account:**

    - Go to the [OpenWeatherMap website](https://openweathermap.org/).
    - Sign up for a free account.

2. **Generate API Key:**

    - Go to the **API keys** section.
    - Generate a new API key and copy it.
    - Add the API key to your `.env` file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [Streamlit](https://www.streamlit.io/)
- [Google Maps API](https://developers.google.com/maps/documentation)
- [OpenWeatherMap API](https://openweathermap.org/api)

## Contact

For any questions or suggestions, please contact [your-email@example.com].

