
import requests
from juego.models import Jugador

def importar_jugadores():
    url = "http://localhost:8000/players"
    response = requests.get(url)
    if response.status_code == 200:
        datos = response.json()
        for item in datos:
            Jugador.objects.update_or_create(
                nombre=item['nombre'],
                defaults={
                    'valor_mercado': item['valor_mercado'],
                    'imagen_url': item['imagen_url']
                }
            )
    else:
        print(f"Error al acceder a la API: {response.status_code}")
