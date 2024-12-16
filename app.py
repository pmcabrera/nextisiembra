from flask import Flask, render_template, jsonify, request
from data_service import scrape_agrofy, scrape_bolsaycot  # Importamos ambas funciones
from clima import get_weather  # Importa la función que obtendrá el clima

app = Flask(__name__)

@app.before_request
def before_request():
    # Asegúrate de que las respuestas utilicen UTF-8
    request.charset = 'utf-8'

@app.route('/')
def home():
    try:
        # Obtener datos de Agrofy
        agrofy_data = scrape_agrofy()
        if agrofy_data.get("error"):
            return jsonify({"error": "No se pudo obtener datos de Agrofy"}), 500

        # Obtener datos del clima para Rosario
        weather_data = get_weather()
        if weather_data.get("error"):
            return jsonify({"error": "No se pudo obtener los datos del clima"}), 500
        
         # Obtener cotizaciones (compra, venta, merval)
        bolsaycot_data = scrape_bolsaycot()
        if bolsaycot_data.get("error"):
            return jsonify({"error": "No se pudo obtener datos de Bolsaycot"}), 500

        # Crear un diccionario combinado con los datos de Agrofy y el clima
        data = {
            'soja': agrofy_data.get('soja', []),
            'maiz': agrofy_data.get('maiz', []),
            'trigo': agrofy_data.get('trigo', []),
            'weather': weather_data,
            'bolsaycot': bolsaycot_data
        }

        # Renderizar la plantilla con los datos
        return render_template('index.html', data=data)
    
    except Exception as e:
        # Manejar excepciones generales
        return jsonify({"error": f"Se produjo un error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
