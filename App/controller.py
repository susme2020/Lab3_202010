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
import model
import csv
from ADT import list as lt
from ADT import map as map

from DataStructures import listiterator as it
from Sorting import mergesort as sort
from time import process_time 


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# Funcionaes utilitarias

def printList (lst):
    iterator = it.newIterator(lst)
    while  it.hasNext(iterator):
        element = it.next(iterator)
        result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
        print (result)



def compareratings (movie1, movie2):
    return ( float(movie1['vote_average']) > float(movie2['vote_average']))


# Funciones para la carga de datos 

def loadBooks (catalog, sep=','):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por 
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    t1_start = process_time() #tiempo inicial
    booksfile = cf.data_dir + 'GoodReads/books.csv'
    dialect = csv.excel()
    dialect.delimiter=sep
    with open(booksfile, encoding="utf-8-sig") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader: 
            # Se adiciona el libro a la lista de libros
            model.addBookList(catalog, row)
            # Se adiciona el libro al mapa de libros (key=title)
            model.addBookMap(catalog, row)
            # Se obtienen los autores del libro
            authors = row['authors'].split(",")
            # Cada autor, se crea en la lista de autores del catalogo, y se 
            # adiciona un libro en la lista de dicho autor (apuntador al libro)
            for author in authors:
                model.addAuthor (catalog, author.strip(), row)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución carga libros:",t1_stop-t1_start," segundos")

def loadMovies (catalog, sep=','):
    """
    Carga las películas del archivo.  Por cada película se toman sus directores y por 
    cada uno de ellos se crea una referencia a la película que se esta procesando.
    """
    t1_start = process_time() #tiempo inicial
    moviesfile = cf.data_dir + 'Movies/MoviesCastingRaw-small.csv'
    dialect = csv.excel()
    dialect.delimiter=sep
    with open(moviesfile, encoding="utf-8-sig") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        # row es de casting
        # row 2 es de votos
        for row in spamreader:
            # Se adiciona la película a la lista de películas

            """ AQUI SE AGREGA ÚNICAMENTE LA INFORMACIÓN DE CASTING """
            movie = model.addMovieList(catalog, row)
            # Se adiciona la película al mapa de películas (key=title)
            #model.addMovieMap(catalog, row)
            # Se obtienen los actores de la película
            actors = ["actor1_name", "actor2_name", "actor3_name", "actor4_name", "actor5_name"]
            # Se crea en la lista de actores del catalogo, y se 
            # adiciona una película en la lista de dicho actor (apuntador a la película)
            for actor in actors:
                if row[actor] != None:
                    """ FALTA TERMINAR """
                    model.addActor(catalog, row[actor], row)
                    lt.addLast(movie["actors"], row[actor])
            # Se obtiene el director de la película
            """ TAMBIÉN FALTA TERMINAR """
            #model.addDirector(catalog, row["director_name"], row, row2)
    
    moviesfile = cf.data_dir + 'Movies/SmallMoviesDetailsCleaned.csv'
    with open(moviesfile, encoding="utf-8-sig") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        """ AQUI SE DEBERÍA AGREGAR UNICAMENTE LA INFORMACIÓN DE VOTOS """
        for row in spamreader:
            model.addMovieListVoteData(catalog, row)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución carga películas:",t1_stop-t1_start," segundos")   

def initCatalog ():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

def loadData (catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadBooks(catalog)
    loadMovies(catalog)
    

# Funciones llamadas desde la vista y enviadas al modelo


def getBookInfo(catalog, bookTitle):
    t1_start = process_time() #tiempo inicial
    book=model.getBookInList(catalog, bookTitle)
    #book=model.getBookInMap(catalog, bookTitle)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución buscar libro:",t1_stop-t1_start," segundos")   
    if book:
        return book
    else:
        return None

def getMovieInfo (catalog, movieTitle):
    t1_start = process_time() #tiempo inicial
    movie=model.getMovieInList(catalog, movieTitle)
    #movie=model.getMovieInMap(catalog, movieTitle)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución buscar película:",t1_stop-t1_start," segundos")   
    if movie:
        return movie
    else:
        return None

def getAuthorInfo(catalog, authorName):
    author=model.getAuthorInfo(catalog, authorName)
    if author:
        return author
    else:
        return None    

def getDirectorInfo (catalog, director_name):
    director=model.getDirectorInfo(catalog, director_name)
    if director:
        return director
    else:
        return None 