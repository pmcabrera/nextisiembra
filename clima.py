from datetime import datetime
import locale
import requests

def get_weather_icon(code):
    icons = {
        0: "/static/images/despejado.png",
        1: "/static/images/mayormente despejado.png",
        2: "/static/images/parcualmente nueblado.png",
        3: "/static/images/nublado.png",
        45: "/static/images/niebla.png",
        48: "/static/images/niebla.png",
        51: "/static/images/llovizna.png",
        53: "/static/images/llovizna.png",
        55: "/static/images/llovizna.png",
        61: "/static/images/lluvia.png",
        63: "/static/images/lluvia.png",
        65: "/static/images/lluvia.png",
        95: "/static/images/tomenta electrica.png",
        96: "/static/images/tormenta con granizo.png",
        99: "/static/images/tormenta con granizo.png"
    }
    return icons.get(code, "/static/images/despejado.png")

def get_weather():
    # Configura la localización (intenta con 'es_ES.UTF-8' si 'es_AR.UTF-8' no funciona)
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    
    latitude = -32.9468
    longitude = -60.6393
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}&current_weather=true"
        f"&daily=temperature_2m_max,temperature_2m_min,weathercode"
        f"&timezone=America/Argentina/Buenos_Aires"
    )
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        current_weather = data.get('current_weather', {})
        temperature = current_weather.get('temperature', "N/A")
        weather_icon_code = current_weather.get('weathercode', None)
        icon_class = get_weather_icon(weather_icon_code)
        
        daily_forecast = data.get('daily', {})
        forecast = []
        today = datetime.today().strftime('%Y-%m-%d')
        
        # Diccionario para traducir días manualmente
        days_translation = {
            'Monday': 'lunes',
            'Tuesday': 'martes',
            'Wednesday': 'miércoles',  # Asegúrate de que "miércoles" tenga el acento
            'Thursday': 'jueves',
            'Friday': 'viernes',
            'Saturday': 'sábado',
            'Sunday': 'domingo'
        }

        for i in range(3):
            try:
                date = daily_forecast['time'][i]
                max_temp = daily_forecast['temperature_2m_max'][i]
                min_temp = daily_forecast['temperature_2m_min'][i]
                weather_code = daily_forecast['weathercode'][i]
                weather_icon = get_weather_icon(weather_code)
                
                # Obtener el nombre del día en español
                day_name = datetime.strptime(date, '%Y-%m-%d').strftime('%A')
                day_name = days_translation.get(day_name, day_name)  # Traducción manual
                
                if date == today:
                    day_name = "Hoy"
                
                forecast.append({
                    "date": date,
                    "day_name": day_name,
                    "max_temp": max_temp,
                    "min_temp": min_temp,
                    "weather_icon": weather_icon
                })
            except (IndexError, KeyError):
                continue
        
        return {
            'current_weather': {
                'temperature': temperature,
                'icon_class': icon_class
            },
            'forecast': forecast
        }
    else:
        return {"error": f"Failed to retrieve weather data: HTTP {response.status_code}"}
