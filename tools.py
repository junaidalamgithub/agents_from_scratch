import requests
import os
from dotenv import load_dotenv

load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


import requests
from typing import Literal

# Note: WEATHER_API_KEY should be defined in your environment or config
# WEATHER_API_KEY = "your_actual_api_key_here"


def get_weather(city: str) -> str:
    """
    Retrieve the current weather condition and temperature for a given city using the WeatherAPI service.

    This function queries the free tier of WeatherAPI[](https://www.weatherapi.com/) to fetch real-time
    weather data. It returns a human-readable string with the weather description and temperature
    in Celsius.

    Parameters
    ----------
    city : str
        The name of the city (or city,country code) for which to retrieve the weather.
        Examples: "London", "New York", "Paris,FR", "Tokyo".

    Returns
    -------
    str
        A formatted string describing the current weather and temperature, e.g.
        "The weather in London is currently Clear with a temperature of 15°C."
        If the request fails or the city is not found, a friendly error message is returned:
        "Sorry, I couldn't retrieve the weather information right now."

    Raises
    ------
    requests.RequestException
        Propagates network-related errors (timeouts, connection errors, etc.) from the
        underlying `requests.get` call if they are not explicitly handled.

    Notes
    -----
    - Requires a valid `WEATHER_API_KEY` constant or environment variable containing a WeatherAPI key.
    - The function uses the free endpoint `/v1/current.json` which has rate limits on the free plan.
    - Temperature is returned in Celsius (`temp_c`) as provided by the API.

    Example
    -------
    >>> get_weather("Berlin")
    'The weather in Berlin is currently Partly cloudy with a temperature of 18°C.'
    """
    print("TOOL: get_weather called")
    url = f"https://api.weatherapi.com/v1/current.json?q={city}&key={WEATHER_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_desc = data['current']['condition']['text']
        temp = data['current']['temp_c']
        return f"The weather in {city} is currently {weather_desc} with a temperature of {temp}°C."
    else:
        return "Sorry, I couldn't retrieve the weather information right now."

def calculate_sum(expression: str) -> float:
    """Evaluate a string containing a simple arithmetic expression and return the result as a float.

    This function uses Python's built-in `eval()` to compute the value of the provided expression.
    It is intended **only** for basic summation-style expressions (e.g., addition, subtraction,
    multiplication, division, parentheses, and numeric literals). It is **not safe** for untrusted
    input because `eval()` can execute arbitrary code.

    Parameters
    ----------
    expression : str
        A string representing a valid Python arithmetic expression, such as:
        - "1 + 2 + 3"
        - "10.5 * 2 - 4 / 2"
        - "(100 + 200) * 0.15"

    Returns
    -------
    float
        The numeric result of evaluating the expression.

    Raises
    ------
    SyntaxError
        If the expression contains invalid Python syntax.
    NameError
        If the expression references undefined names.
    Exception
        For any other evaluation errors (ZeroDivisionError, OverflowError, etc.).

    Examples
    --------
    >>> calculate_sum("5 + 10")
    15.0
    >>> calculate_sum("3.14 * 10")
    31.4
    >>> calculate_sum("(50 + 50) * 0.2")
    20.0

    Security note
    -------------
    Do **not** use this function with input from untrusted sources, as it can lead to arbitrary
    code execution. In production code, prefer a safe parser (e.g., `ast.literal_eval` with a custom
    visitor or libraries like `sympy`/`pyparsing`).
    """
    print("TOOL: calculate_sum called")
    return eval(expression)
