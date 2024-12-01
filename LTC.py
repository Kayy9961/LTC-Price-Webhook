import requests
import time
import datetime

WEBHOOK_URL = 'TU ENLACE DE WEEBHOOK'

def obtener_precio_ltc():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    parametros = {
        'ids': 'litecoin',
        'vs_currencies': 'usd'
    }
    try:
        respuesta = requests.get(url, params=parametros)
        respuesta.raise_for_status() 
        datos = respuesta.json()
        precio = datos['litecoin']['usd']
        return precio
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener el precio de LTC: {e}")
        return None
def enviar_a_discord(mensaje):
    data = {
        "content": mensaje
    }
    try:
        respuesta = requests.post(WEBHOOK_URL, json=data)
        respuesta.raise_for_status()
        print(f"Mensaje enviado correctamente a Discord a las {datetime.datetime.now()}")
    except requests.exceptions.RequestException as e:
        print(f"Error al enviar el mensaje a Discord: {e}")

def main():
    while True:
        precio = obtener_precio_ltc()
        if precio is not None:
            mensaje = f"📈 El precio actual de Litecoin (LTC) es: **${precio} USD** (Actualizado a las {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})"
            enviar_a_discord(mensaje)
        time.sleep(300)

if __name__ == "__main__":
    main()
