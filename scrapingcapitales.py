import requests
from bs4 import BeautifulSoup

def extraer_capitales(pais):
    # URL de la página que contiene la lista de capitales
    url = "https://es.wikipedia.org/wiki/Anexo:Capitales_de_Estado"

    # Realizar la solicitud HTTP
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Parsear el contenido HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Encontrar la tabla que contiene las capitales
        tabla = soup.find("table", {"class": "wikitable"})

        # Inicializar una lista para almacenar las capitales del país especificado
        capitales_pais = []

        # Buscar en todas las filas de la tabla
        filas = tabla.find_all("tr")
        for fila in filas:
            # Encontrar las celdas de cada fila
            celdas = fila.find_all("td")
            if len(celdas) > 1:  # Verificar si la fila tiene al menos dos celdas
                nombre_pais = celdas[0].text.strip()
                capital = celdas[1].text.strip()
                if nombre_pais.lower() == pais.lower():
                    capitales_pais.append(capital)

        return capitales_pais
    else:
        # Si la solicitud no fue exitosa, imprimir el mensaje de error
        print("Error al obtener la página:", response.status_code)
        return None

# Pedir al usuario que ingrese el nombre del país
nombre_pais = input("Ingresa el nombre del país para obtener su capital: ")

# Obtener las capitales del país ingresado por el usuario
capitales = extraer_capitales(nombre_pais)

if capitales:
    if len(capitales) == 0:
        print("No se encontró información sobre la capital de", nombre_pais)
    elif len(capitales) == 1:
        print("La capital de", nombre_pais, "es:", capitales[0])
    else:
        print("Las capitales de", nombre_pais, "son:")
        for capital in capitales:
            print("-", capital)
