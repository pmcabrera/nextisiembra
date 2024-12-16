from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def scrape_daily_items():
    url = "https://news.agrofy.com.ar/"  # Reemplaza con la URL real
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "No se pudo acceder a la página"}), 500

    soup = BeautifulSoup(response.content, 'html.parser')
    data = []

    # Buscar todos los bloques con clase 'daily-item'
    daily_items = soup.find_all('div', class_='daily-item')

    if not daily_items:
        return jsonify({"error": "No se encontraron bloques 'daily-item'"}), 404

    # Iterar sobre cada bloque para extraer los datos
    for item in daily_items:
        # Extraer las diferentes secciones (compra, venta, merval)
        for section in item.find_all('div', class_=['compra', 'venta', 'merval']):
            name = section.find('label', class_='name')
            detail = section.find('label', class_='detail')
            price = section.find('label', class_='price')
            percent = section.find('label', class_='percent')
            indicator = section.find('label', class_='indicator')
            icon = section.find('label', class_='icon')

            # Agregar los datos al resultado
            data.append({
                'name': name.get_text(strip=True) if name else None,
                'detail': detail.get_text(strip=True) if detail else None,
                'price': price.get_text(strip=True) if price else None,
                'percent': percent.get_text(strip=True) if percent else None,
                'indicator': indicator.get_text(strip=True) if indicator else None,
                'icon': icon.get_text(strip=True) if icon else None
            })

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
