import requests
from bs4 import BeautifulSoup

def scrape_bolsaycot():
    # URL de la página a scrapear
    url = "https://news.agrofy.com.ar/"

    # Realizamos la solicitud HTTP
    response = requests.get(url)

    # Verificamos si la solicitud fue exitosa
    if response.status_code == 200:
        # Parseamos el contenido HTML con BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Buscamos los bloques que contienen la información deseada
        daily_items = soup.find_all('div', class_='daily-item')

        # Lista para almacenar los datos extraídos
        data = []

        # Iteramos sobre cada bloque de daily-item
        for item in daily_items:
            # Extraemos los datos relevantes para cada sección (COMPRA, VENTA, Merval)
            compra = item.find('div', class_='compra')
            venta = item.find('div', class_='venta')
            merval = item.find('div', class_='merval')

            # Procesamos cada bloque (compra, venta, merval) de forma independiente
            for section in [compra, venta, merval]:
                if section:
                    # Extraemos el nombre (U$ Nación, U$ Blue, Merval)
                    name = section.find('label', class_='name')
                    # Extraemos el precio
                    price = section.find('label', class_='price')
                    # Extraemos el porcentaje
                    percent = section.find('label', class_='percent')
                    # Extraemos el indicador
                    indicator_icon = section.find('label', class_='icon')

                    # Verificamos que los datos existan y los almacenamos
                    if name and price and percent:
                        data.append({
                            'name': name.get_text(strip=True),
                            'price': price.get_text(strip=True),
                            'percent': percent.get_text(strip=True),
                            'indicator': "Presente" if indicator_icon else "No presente"
                        })

        # Devolvemos los datos extraídos
        return data

    else:
        print(f"Error al acceder a la página: {response.status_code}")
        return None
