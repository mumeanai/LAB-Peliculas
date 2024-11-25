from collections import Counter, defaultdict
from typing import NamedTuple
from datetime import *
import csv

Pelicula = NamedTuple(
    "Pelicula",
    [("fecha_estreno", date), 
    ("titulo", str), 
    ("director", str), 
    ("generos",list[str]),
    ("duracion", int),
    ("presupuesto", int), 
    ("recaudacion", int), 
    ("reparto", list[str])
    ]
)



def parsea_lista(cadena:str)-> list[str]:
    res = []
    for trozo in cadena.split(","):     #.split()   separa la cadena, como una lista de cadenas
        res.append(trozo.strip())       #.strip()   
    return res


def lee_peliculas(ruta:str)-> list[Pelicula]:
    '''
    recibe una cadena de texto con la ruta de un fichero csv, 
    y devuelve una lista de tuplas Pelicula con la información 
    contenida en el fichero. Utilice 
    datetime.strptime(cadena, "%d/%m/%Y").date() para parsear 
    las fechas. (1 punto)
    '''
    res = []
    
    with open(ruta, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ';')
        next(lector)
        for fecha_estreno, titulo, director,generos, duracion, presupuesto, recaudacion, reparto in lector:
            fecha_estreno = datetime.strptime(fecha_estreno, "%d/%m/%Y").date()
            generos = parsea_lista(generos)
            duracion = int(duracion)
            presupuesto = int(presupuesto)
            recaudacion = int(recaudacion)
            reparto = parsea_lista(reparto)
            tupla = Pelicula(fecha_estreno, titulo, director,generos, duracion, presupuesto, recaudacion, reparto)
            res.append(tupla)
        return res    

def peliculas_mas_ganancias(peliculas: list[Pelicula], genero:str = None)-> tuple[str,str]:
    '''
    recibe una lista de tuplas de tipo Pelicula y una cadena de 
    texto genero, con valor por defecto None, y devuelve el título 
    y las ganancias de la película con mayores ganancias, de entre
    aquellas películas que tienen entre sus géneros el genero 
    indicado. Si el parámetro genero es None, se busca la película
    con mayores ganancias, sin importar sus géneros. Las ganancias 
    de una película se calculan como la diferencia entre la 
    recaudación y el presupuesto. (1 puntos)
    '''
    res =[]
    for p in peliculas:
        if genero == None or genero in p.generos:
            ganancias = p.recaudacion - p.presupuesto
            tupla = (p.titulo, ganancias)
            res.append(tupla)
    maximo = max(res, key = lambda t:t[1])
    return maximo
    

def media_presupuesto_por_genero(peliculas:list[Pelicula]) -> dict[str, float]:
    '''
    recibe una lista de tuplas de tipo Pelicula y devuelve un 
    diccionario en el que las claves son los distintos géneros 
    y los valores son la media de presupuesto de las películas 
    de cada género. (1,5 puntos)
    '''
    presupuestos = defaultdict(list)
    for p in peliculas:
        for g in p.generos:
            presupuestos[g].append(p.presupuesto)
    
    res = {}
    for  genero, presupuesto in presupuestos.items():
        res[genero] = sum(presupuesto)/len(presupuesto)
    return res

def peliculas_por_actor(peliculas:list[Pelicula], año_inicial:date.year = None, año_final:date.year = None) -> dict[str,int]:
    '''
    recibe una lista de tuplas de tipo Pelicula y dos enteros año_inicial 
    y año_final, con valor por defecto None, y devuelve un diccionario en el 
    que las claves son los nombres de los actores y actrices, y los valores 
    son el número de películas, estrenadas entre año_inicial y año_final 
    (ambos incluidos), en que ha participado cada actor o actriz. Si año_
    inicial o año_final son None, se contarán las películas sin filtrar por 
    año inicial o final, respectivamente. (1,5 puntos)
    '''

    res = defaultdict(int)
    for p in peliculas:
        if (año_inicial == None or año_inicial <= p.fecha_estreno.year) and (año_final == None or p.fecha_estreno.year<=año_final):
            for actor in p.reparto:
                res[actor]+=1
    
    return res

def actores_mas_frecuentes():
    '''
    recibe una lista de tuplas de tipo Pelicula, un entero n y dos enteros 
    año_inicial y año_final, con valor por defecto None, y devuelve una lista 
    con los n actores o actrices que han participado en más películas estrenadas 
    entre año_inicial y año_final (ambos incluidos). La lista de actores o actrices
    debe estar ordenada alfabéticamente. Si año_inicial o año_final son None, se 
    contarán las películas sin filtrar por año inicial o final, respectivamente. 
    Haga uso de la función peliculas_por_actor para implementar esta función. 
    (1 punto)
    '''
    
    pass

def recaudacion_total_por_año():
    '''
    recibe una lista de tuplas de tipo Pelicula y un conjunto de cadenas de texto 
    generos, con valor por defecto None, y devuelve un diccionario en el que las 
    claves son los años en los que se han estrenado películas, y los valores son 
    la recaudación total de las películas estrenadas en cada año que son de alguno
    de los géneros contenidos en el parámetro generos. Si generos es None, se 
    calcularán las recaudaciones totales de todas las películas de cada año, 
    independientemente de su género. NOTA: Puede usar operaciones entre conjuntos 
    para ver si existe alguna coincidencia entre los géneros de cada película y 
    los géneros especificados por el parámetro. (1,5 puntos)
    '''
    pass

def incrementos_recaudacion_por_año():
    '''
    recibe una lista de tuplas de tipo Pelicula y un conjunto de cadenas de 
    texto generos, con valor por defecto None, y devuelve una lista de enteros 
    con las diferencias de recaudación total de cada año con respecto al anterior 
    registrado, de películas de alguno de los géneros indicados por el parámetro 
    generos. Si generos es None, se usarán para el cálculo las recaudaciones 
    totales de todas las películas de cada año, independientemente de su género. 
    Haga uso de la función recaudacion_total_por_año para implementar esta función.
    (1,5 punto)
    '''
    pass

#Pruebe las funciones implementadas en un módulo peliculas_test.py. 
# Se recomienda que lo vaya haciendo a medida que vaya resolviendo 
# los distintos apartados. (1 punto)