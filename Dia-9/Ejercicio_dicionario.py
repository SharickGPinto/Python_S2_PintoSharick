import json
import re
from collections import Counter

def cargar_datos(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

def artistas_reino_unido_1960_1970(artistas):
    print("\nArtistas del Reino Unido entre 1960 y 1970:")
    for artista in artistas:
        if artista["Country"] == "United Kingdom":
            años = artista["Active years"]
            if "1960" in años or "1970" in años:
                print("- " + artista["Artist name"])

def artistas_genero_rock_pop(artistas):
    print("\nArtistas del género Rock/pop:")
    for artista in artistas:
        genero = artista.get("Genre", "").lower()
        if "rock" in genero and "pop" in genero:
            print("- " + artista["Artist name"])

def artistas_activos_ultimos_10_anios(artistas):
    print("\nArtistas activos en los últimos 10 años:")
    año_actual = 2025
    año_limite = año_actual - 10  # 2015
    
    for artista in artistas:
        años = artista.get("Active years", "")
        
        if "present" in años:
            print("- " + artista["Artist name"])
        else:
            try:
                rango = años.split("–")  # guion largo
                if len(rango) == 2:
                    año_fin = int(rango[1])
                    if año_fin >= año_limite:
                        print("- " + artista["Artist name"])
            except:
                pass

def numero_artistas_por_anio(artistas):
    print("\nNúmero de artistas por año de primer lanzamiento:")
    años = []
    for artista in artistas:
        año = artista.get("Release year of first charted record")
        if isinstance(año, int):
            años.append(año)
    
    conteo = Counter(años)
    for año, cantidad in sorted(conteo.items()):
        print(f"Año {año}: {cantidad} artista(s)")

def unidades_certificadas_por_pais(artistas):
    print("\nUnidades certificadas por país en 2023:")
    paises_totales = {}
    
    for artista in artistas:
        unidades_str = artista.get("Total certified units", "")
        try:
            match = re.search(r"([\d\.]+) million", unidades_str)
            if match:
                valor = float(match.group(1))
                pais = artista.get("Country", "Desconocido")
                paises_totales[pais] = paises_totales.get(pais, 0) + valor
        except:
            pass
    
    for pais, total in paises_totales.items():
        print(f"{pais}: {total:.2f} millones")

def menu():
    print("\n=== LimeWire - Gestión de Artistas ===")
    print("1. Ver artistas del Reino Unido entre 1960 y 1970")
    print("2. Ver artistas de género Rock/pop")
    print("3. Ver artistas activos en los últimos 10 años")
    print("4. Ver número de artistas por año")
    print("5. Ver unidades certificadas por país en 2023")
    print("6. Salir")

def main():
    artistas = cargar_datos("Artistas.json")
    paises = cargar_datos("paises.json")
    generos = cargar_datos("generos.json")

    while True:
        menu()
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            artistas_reino_unido_1960_1970(artistas)
        elif opcion == "2":
            artistas_genero_rock_pop(artistas)
        elif opcion == "3":
            artistas_activos_ultimos_10_anios(artistas)
        elif opcion == "4":
            numero_artistas_por_anio(artistas)
        elif opcion == "5":
            unidades_certificadas_por_pais(artistas)
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción incorrecta. Intenta de nuevo.")
