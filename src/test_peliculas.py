from peliculas import *


def test_lee_peliculas(datos):
    print("Test de lee_peliculas:")
    print("Total de registros leidos:", len(datos))
    print("Mostrando los tres primeros registros:", datos[:3])
    print("Mostrando los tres últimos registros:", datos[-4:])
    
def test_peliculas_mas_ganancias(datos):
    print("Test de peliculas_mas_ganancias (genero = None): ", peliculas_mas_ganancias(datos, None))
    print("Test de peliculas_mas_ganancias (genero = Drama): ", peliculas_mas_ganancias(datos, "Drama"))

def test_media_presupuesto_por_genero(datos):
    print("Test de media_presupuesto_por_genero: ", media_presupuesto_por_genero(datos))


def test_peliculas_por_actor(datos):
    print("Test de peliculas_por_actor (año_inicial =None, año_final =None", peliculas_por_actor(datos, None, None))
    print("Test de peliculas_por_actor (año_inicial =2010, año_final =2020", peliculas_por_actor(datos, 2010, 2020))
    print("Test de peliculas_por_actor (año_inicial =2005, año_final =2015", peliculas_por_actor(datos, 2005, 2015))
    #falta ver que solo salgan 3 actores, y no todos 
    
    
if __name__ == '__main__':
    datos = lee_peliculas("data/peliculas.csv")
    test_lee_peliculas(datos)
    test_peliculas_mas_ganancias(datos)
    test_media_presupuesto_por_genero(datos)
    test_peliculas_por_actor(datos)