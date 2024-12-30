from peliculas import *


def test_lee_peliculas(datos):
    print("Test de lee_peliculas:")
    print("Total de registros leidos:", len(datos))
    print("Mostrando los tres primeros registros:", datos[:3])
    print("Mostrando los tres últimos registros:", datos[-4:])
    print("##########"*10)
    
def test_peliculas_mas_ganancias(datos):
    print("Test de peliculas_mas_ganancias (genero = None): ", peliculas_mas_ganancias(datos, None))
    print("Test de peliculas_mas_ganancias (genero = Drama): ", peliculas_mas_ganancias(datos, "Drama"))
    print("##########"*10)

def test_media_presupuesto_por_genero(datos):
    print("Test de media_presupuesto_por_genero: ", media_presupuesto_por_genero(datos))
    print("##########"*10)

def imprimir_solo_tres(diccionario):
    for actor, pelicula in  diccionario.items():
        if actor == 'Robert Downey Jr.' or actor == 'Christian Bale' or actor == 'Adam Driver': 
            print(f'{actor}: {pelicula}')
        

def test_peliculas_por_actor(datos):
    print("Test de peliculas_por_actor (año_inicial =None, año_final =None)")
    imprimir_solo_tres(peliculas_por_actor(datos, None, None))
    print("Test de peliculas_por_actor (año_inicial =2010, año_final =2020)")
    imprimir_solo_tres(peliculas_por_actor(datos, 2010, 2020))
    print("##########"*10)

def test_actores_mas_frecuentes(datos):
    print("Test de actores_mas_frecuentes (n=3, año_inicial=2005, año_final=2015):", actores_mas_frecuentes(datos, 3, 2005, 2015))
    print("##########"*10)

def test_recaudacion_total_por_año(datos):
    print("Test de recaudacion_total_por_año (generos=None): ")
    print(recaudacion_total_por_año(datos, None))
    print("Test de recaudacion_total_por_año (generos={'Drama', 'Acción'}): ")
    print(recaudacion_total_por_año(datos, {'Drama', 'Acción'}))
    print("##########"*10)

def test_incrementos_recaudacion_por_año(datos):
    print("Test de incrementos_recaudacion_por_año (generos=None):", incrementos_recaudacion_por_año(datos, None))
    print("Test de incrementos_recaudacion_por_año (generos={'Drama', 'Acción'}):", incrementos_recaudacion_por_año(datos, {'Drama', 'Acción'}))

if __name__ == '__main__':
    datos = lee_peliculas("data/peliculas.csv")
    test_lee_peliculas(datos)
    test_peliculas_mas_ganancias(datos)
    test_media_presupuesto_por_genero(datos)
    test_peliculas_por_actor(datos)
    test_actores_mas_frecuentes(datos)
    test_recaudacion_total_por_año(datos)
    test_incrementos_recaudacion_por_año(datos)