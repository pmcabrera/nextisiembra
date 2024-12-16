import re
from bs4 import BeautifulSoup
import requests

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

        # Si hay datos en la sección 'compra', 'venta', o 'merval', procesamos
        for section, section_data in zip(['compra', 'venta', 'merval'], [compra, venta, merval]):
            if section_data:
                # Eliminamos las etiquetas <label class="detail-mob">(COMPRA)</label> completamente
                for label in section_data.find_all('label', class_='detail-mob'):
                    label.decompose()

                # Extraemos el nombre sin las etiquetas indeseadas
                name = section_data.find('label', class_='name')

                if name:
                    name_text = name.get_text(strip=True)

                    # Eliminamos los textos "(COMPRA)" y "(VENTA)" usando expresiones regulares
                    name_text = re.sub(r'\(COMPRA\)', '', name_text)
                    name_text = re.sub(r'\(VENTA\)', '', name_text)

                    # Limpiamos cualquier texto residual con paréntesis y espacios
                    name_text = re.sub(r'\s*\(.*\)\s*', '', name_text)

                    # Limpiamos las repeticiones de "(COMPRA)" y "(VENTA)"
                    name_text = re.sub(r'(\(COMPRA\)|\(VENTA\))\1+', '', name_text)

                    # Eliminamos cualquier espacio adicional o texto residual
                    name_text = name_text.strip()

                    # Agregamos el nombre limpio y otros valores
                    price = section_data.find('label', class_='price')
                    percent = section_data.find('label', class_='percent')

                    if price and percent:
                        data[section].append({
                            'name': name_text,
                            'price': price.get_text(strip=True),
                            'percent': percent.get_text(strip=True)
                        })

    return data
