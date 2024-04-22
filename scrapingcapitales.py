import pandas as pd
'''
esta funcion extrae la capital de un pais dada por el usuario
args:
    pais (str): nombre del pais
returns:
    capital (str): capital del pais
    None (None): si no se encuentra la capital
'''


def extraer_capitales(pais):
    # URL de la página que contiene la lista de capitales
    url = "https://es.wikipedia.org/wiki/Anexo:Capitales_de_Estado"

    # Leer las tablas de la página
    tablas = pd.read_html(url)

    # Buscar el país en la primera columna de la primera tabla
    for fila in tablas[0].itertuples(index=False):
        for elemento in fila:
            if str(pais).lower() in str(elemento).lower():
                return fila[-3].strip()

    # Si no se encontró el país o la capital, devolver None
    return None



# Pedir al usuario que ingrese el nombre del país
nombre_pais = input("Ingresa el nombre del país para obtener su capital: ")

# Obtener la capital del país ingresado por el usuario
capital = extraer_capitales(nombre_pais)

if capital:
    print("La capital de", nombre_pais, "es:", capital)
else:
    print("No se encontró información sobre la capital de", nombre_pais)
