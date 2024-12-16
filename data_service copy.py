import requests
from bs4 import BeautifulSoup
from datetime import datetime
from bolsaycot import scrape_bolsaycot



def scrape_agrofy():
    url = "https://news.agrofy.com.ar/"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "No se pudo acceder a la página"}

    soup = BeautifulSoup(response.content, 'html.parser')
    data = {'soja': [], 'maiz': [], 'trigo': []}

    # Buscar contenedor principal
    main_container = soup.find('div', class_='cotization-tabs gray-tabs show-sponsored')
    if not main_container:
        return {"error": "Estructura de página no encontrada"}

    # Iterar por las pestañas (nav-tabs)
    tabs = main_container.find_all('div', class_='tab-pane')
    tab_names = ['soja', 'maiz', 'trigo']

    for index, tab in enumerate(tabs):
        tab_items = tab.find_all('div', class_='tab-item')

        for item in tab_items:
            # Extraer los datos de cada item
            name = item.find('label', class_='name').get_text(strip=True) if item.find('label', class_='name') else None
            price = item.find('label', class_='price').get_text(strip=True) if item.find('label', class_='price') else None
            percent = item.find('label', class_='percent').get_text(strip=True) if item.find('label', class_='percent') else None
            indicator = item.find('label', class_='indicator').get_text(strip=True) if item.find('label', class_='indicator') else None
            icon = item.find('label', class_='icon').get_text(strip=True) if item.find('label', class_='icon') else None

            data[tab_names[index]].append({
                'name': name, 'price': price, 'percent': percent, 'indicator': indicator, 'icon': icon
            })

    return data


def get_weather():
    latitude = -32.9468
    longitude = -60.6393
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&daily=temperature_2m_max,temperature_2m_min,weathercode&timezone=America/Argentina/Buenos_Aires"

    response = requests.get(url)
    if response.status_code != 200:
        return {"error": "No se pudo acceder a los datos del clima"}

    data = response.json()
    current_weather = data['current_weather']
    daily_forecast = data['daily']

    # Map weather codes to descriptions
    weather_icons = {
        0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Cloudy",
        45: "Fog", 48: "Depositing rime fog", 51: "Drizzle", 53: "Moderate drizzle",
        55: "Heavy drizzle", 61: "Showers of rain", 63: "Moderate showers of rain",
        65: "Heavy showers of rain", 71: "Snow fall", 73: "Moderate snow fall",
        75: "Heavy snow fall", 77: "Snow grains", 80: "Showers of snow",
        81: "Moderate showers of snow", 82: "Heavy showers of snow", 95: "Thunderstorms",
        96: "Thunderstorms with light hail", 99: "Thunderstorms with heavy hail"
    }

    current_data = {
        'temperature': current_weather.get('temperature', "N/A"),
        'description': weather_icons.get(current_weather.get('weathercode', "N/A"), "Unknown")
    }

    forecast_data = []
    for i in range(len(daily_forecast['time'])):
        forecast_data.append({
            'date': daily_forecast['time'][i],
            'max_temp': daily_forecast['temperature_2m_max'][i],
            'min_temp': daily_forecast['temperature_2m_min'][i],
            'description': weather_icons.get(daily_forecast['weathercode'][i], "Unknown")
        })

    return {'current': current_data, 'forecast': forecast_data}


def scrape_bolsaycot():
    url = "https://news.agrofy.com.ar/"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "No se pudo acceder a la página"}

    soup = BeautifulSoup(response.text, 'html.parser')
    daily_items = soup.find_all('div', class_='daily-item')

    data = {
        'compra': [],
        'venta': [],
        'merval': []
    }

    # Iteramos sobre cada bloque de daily-item
    for item in daily_items:
        # Extraemos los bloques para cada sección (compra, venta, merval)
        compra = item.find('div', class_='compra')
        venta = item.find('div', class_='venta')
        merval = item.find('div', class_='merval')

        for section, section_data in zip(['compra', 'venta', 'merval'], [compra, venta, merval]):
            if section_data:
                # Extraemos los datos relevantes
                name = section_data.find('label', class_='name')
                price = section_data.find('label', class_='price')
                percent = section_data.find('label', class_='percent')
                indicator_icon = section_data.find('label', class_='icon')

                if name and price and percent:
                    data[section].append({
                        'name': name.get_text(strip=True),
                        'price': price.get_text(strip=True),
                        'percent': percent.get_text(strip=True),
                        'indicator': "Presente" if indicator_icon else "No presente"
                    })

    return data