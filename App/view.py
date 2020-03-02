"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
import csv
from ADT import list as lt
from ADT import map as map

from DataStructures import listiterator as it

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("\nBienvenido al RETO 2")
    print("1- Cargar información")
    print("2- Buscar película por título")
    print("3- Buscar información de un director por nombre ...")

    """ Requerimiento 1: Buenas películas """

    print("4- Buenas películas, cuantas películas con votación positiva (vote_average ≥ 6) tiene dado un nombre exacto de director ")
    
    """ Requerimiento 2: Votos """

    print("5- Votos, los datos de una película por título exacto: voto promedio, votos totales y su director")

    """ Requerimiento 3: Directores """
    
    print("6- Directores, todas las películas de un director dado su nombre exacto. Indicando el número de películas dirigidas, y el promedio de votos obtenidos en sus películas.")

    """ Requerimiento 4: Actores """

    print("7- Actores, todas las películas en las que ha participado un actor dado su nombre exacto. Indicando el total de películas en las que ha participado, el promedio de votos de sus películas y el director que más veces lo ha dirigido.")

    """ Requerimiento 5: Géneros """

    print("8- Géneros, cuántas películas tiene asociadas un género (genres) a partir del nombre exacto del género. Adicionalmente se debe indicar para dicho género, el promedio de votos de todas las películas de dicho género")
    
    print("0- Salir")


def initCatalog ():
    """
    Inicializa el catalogo de peliculas
    """
    return controller.initCatalog()


def loadData (catalog):
    """
    Carga las peliculas en la estructura de datos
    """
    controller.loadData(catalog)


"""
Menu principal
"""
datos_cargados = False
while True:
    printMenu()
    inputs =input('Seleccione una opción para continuar\n')
    if int(inputs[0])==1: # 1- Cargar información
        print("Cargando información de los archivos ....")
        catalog = initCatalog ()
        loadData (catalog)
        """
        print ('Mapa Libros cargados: ' + str(map.size(catalog['booksMap'])))
        print ('Lista Libros cargados: ' + str(lt.size(catalog['booksList'])))
        print ('Autores cargados: ' + str(map.size(catalog['authors'])))
        """
        print ('Lista: Películas cargadas: ' + str(lt.size(catalog['moviesList'])))
        print ('Mapa: Películas cargadas: ' + str(map.size(catalog['moviesMap'])))
        print ('Mapa: Actores cargados: ' + str(map.size(catalog['actors'])))
        print ('Mapa: Directores cargados: ' + str(map.size(catalog['directors'])))
        print ('Mapa: Géneros cargados: ' + str(map.size(catalog['genres'])))

        datos_cargados = True
        
    elif int(inputs[0])==2: # 2- Buscar película por título
        if not datos_cargados:
            """
            bookTitle = input("Nombre del libro a buscar: ")
            book = controller.getBookInfo (catalog, bookTitle)
            if book:
                print("Libro encontrado:",book['title'],",Rating:",book['average_rating'])
            else:
                print("Libro No encontrado")
            """
            movieTitle = input("Nombre de la película a buscar: ")
            movie = controller.getMovieInfo (catalog, movieTitle)
            if movie:
                print("Película encontrada:", movie['title'], ", ID:", movie['id'], "\nVoto Promedio: ",  movie['vote_average'], "\nDirector: ", movie['director'], "\nActores: ", movie["actors"])
            else:
                print("Película No encontrada")
        else:
            print("No ha cargado los datos aún")

    elif int(inputs[0])==3: # 3- Buscar información de director por nombre ...
        if not datos_cargados:
            """
            authorName = input("Nombre del autor a buscar: ")
            author = controller.getAuthorInfo (catalog, authorName)
            if author:
                print("Libros del autor",authorName,":",lt.size(author['authorBooks']))
                print("Promedio de Votación: ",authorName,(author['sum_average_rating']/lt.size(author['authorBooks'])))
            else:
                print("Autor No encontrado")
            """
            director_name = input("Nombre del director a buscar: ")
            director = controller.getDirectorInfo (catalog, director_name)
            if director:
                print("Películas dirigidas por ", director_name,": ", lt.size(director['movie_titles']))
                print("Promedio de Votación: ", (director['sum_average_rating']/lt.size(director['movie_titles'])))
            else:
                print("Director No encontrado")
        else:
            print("No ha cargado los datos aún")

    elif int(inputs[0])==4: # 4- Buenas películas, cuantas películas con votación positiva (vote_average ≥ 6) tiene dado un nombre exacto de director
        if not datos_cargados:
            label = input (" ")
        else:
            print("No ha cargado los datos aún")

    elif int(inputs[0])==5: # 5- Votos, los datos de una película por título exacto: voto promedio, votos totales y su director
        if not datos_cargados:
        else:
            print("No ha cargado los datos aún")

    elif int(inputs[0])==6: # 6- Directores, todas las películas de un director dado su nombre exacto. Indicando el número de películas dirigidas, y el promedio de votos obtenidos en sus películas.
        if not datos_cargados:
        else:
            print("No ha cargado los datos aún")

    elif int(inputs[0])==7: # 7- Actores, todas las películas en las que ha participado un actor dado su nombre exacto. Indicando el total de películas en las que ha participado, el promedio de votos de sus películas y el director que más veces lo ha dirigido.
        if not datos_cargados:
        else:
            print("No ha cargado los datos aún")

    elif int(inputs[0])==8: # 8- Géneros, cuántas películas tiene asociadas un género (genres) a partir del nombre exacto del género. Adicionalmente se debe indicar para dicho género, el promedio de votos de todas las películas de dicho género
        if not datos_cargados:
        else:
            print("No ha cargado los datos aún")

    else:
        sys.exit(0)
sys.exit(0)