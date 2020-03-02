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
from ADT import list as lt
from ADT import map as map
from DataStructures import listiterator as it


"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores 
y otra para géneros
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de peliculas. Retorna el catalogo inicializado.
    """
    catalog = {'booksList':None, 'authors':None, 'booksMap': None, "moviesList": None, "moviesMap": None, "directors": None, "actors": None}
    catalog['booksList'] = lt.newList("ARRAY_LIST")
    catalog['booksMap'] = map.newMap (5003, maptype='CHAINING')#10000 books
    catalog['authors'] = map.newMap (12007, maptype='PROBING') #5841 authors

    catalog['moviesList'] = lt.newList("ARRAY_LIST")
    catalog['moviesMap'] = map.newMap (164531, maptype='CHAINING') #329044 movies
    catalog['actors'] = map.newMap (130439, maptype='CHAINING') #260861 actors
    catalog['directors'] = map.newMap (171863, maptype='PROBING') #85929 directors
    catalog['genres'] = map.newMap (43, maptype='PROBING') # 21 genres
    return catalog


def newBook (row):
    """
    Crea un nuevo diccionario para un libro
    """
    book = {"book_id": row['book_id'], "title":row['title'], "average_rating":row['average_rating'], "ratings_count":row['ratings_count']}
    return book

def newMovie(row, actors_movie):
    """
    Crea un nuevo diccionario para una película
    """
    movie = {"id": row['id'], "title":None, "vote_average":0, "vote_count":0, "director": row["director_name"], "actors": actors_movie}
    return movie

def addBookList (catalog, row):
    """
    Adiciona libro a la lista
    """
    books = catalog['booksList']
    book = newBook(row)
    lt.addLast(books, book)

def addMovieList(catalog, row, actors_movie):
    """
    Adiciona película a la lista
    """
    movies = catalog['moviesList']
    movie = newMovie(row, actors_movie)
    lt.addLast(movies, movie)
    return movie

def addMovieListVoteData(movie, row):
    """
    Adiciona información a una película
    """
    movie["title"] = row["title"]
    movie["vote_average"] += float(row["vote_average"])
    movie["vote_count"] += float(row["vote_count"])

def addBookMap (catalog, row):
    """
    Adiciona libro al map con key=title
    """
    books = catalog['booksMap']
    book = newBook(row)
    map.put(books, book['title'], book, compareByKey)

def addMovieMap(catalog, row, actors_movie):
    """
    Adiciona película al map con key=title
    """
    movies = catalog['moviesMap']
    movie = newMovie(row, actors_movie)
    map.put(movies, movie['id'], movie, compareByKey)

def addMovieMapVoteData(movie, row):
    """
    Adiciona información a una película en el map
    """
    movie["title"]= row["title"]
    movie["vote_average"] = float(row["vote_average"])
    movie["vote_count"] = float(row["vote_count"])


def newAuthor (name, row):
    """
    Crea una nueva estructura para modelar un autor y sus libros
    """
    author = {'name':"", "authorBooks":None,  "sum_average_rating":0}
    author ['name'] = name
    author['sum_average_rating'] = float(row['average_rating'])
    author ['authorBooks'] = lt.newList('SINGLE_LINKED')
    lt.addLast(author['authorBooks'],row['book_id'])
    return author

def newActor(name, row):
    """
    Crea una nueva estructura para modelar un actor y sus películas
    """
    actor = {'name':name, "movie_titles": lt.newList("ARRAY_LIST"),  "sum_average_rating":0, "movies_id": lt.newList("ARRAY_LIST")}
    lt.addLast(actor['movies_id'], row['id'])
    return actor

def addAuthor (catalog, name, row,):
    """
    Adiciona un autor al map y sus libros
    """
    if name:
        authors = catalog['authors']
        author=map.get(authors,name,compareByKey)
        if author:
            lt.addLast(author['authorBooks'],row['book_id'])
            author['sum_average_rating'] += float(row['average_rating'])
        else:
            author = newAuthor(name, row)
            map.put(authors, author['name'], author, compareByKey)

def addActor(catalog, name, row):
    """
    Adiciona un actor al map y sus películas
    """
    if name:
        actors = catalog['actors']
        actor=map.get(actors,name,compareByKey)
        if actor:
            lt.addLast(actor['movies_id'],row['id'])
        else:
            actor = newActor(name, row)
            map.put(actors, actor['name'], actor, compareByKey)

def addActorVoteData(catalog, name, row):
    actors = catalog['actors']
    actor=map.get(actors,name,compareByKey)
    if actor:
        if row["id"] in actor["movies_id"]:
            lt.addLast(actor['movie_titles'],row['title'])
            lt.addLast(actor['movies_id'],row['id'])
            actor['sum_average_rating'] += float(row['vote_average'])

def newDirector(name, row):
    """
    Crea una nueva estructura para modelar un director y sus películas
    """
    director = {'name':name, "movie_titles": lt.newList("ARRAY_LIST"),  "sum_average_rating":0, "movies_id": lt.newList("ARRAY_LIST")}
    lt.addLast(director['movies_id'], row['id'])
    return director

def addDirector(catalog, name, row):
    """
    Adiciona un director al map y sus películas
    """
    if name:
        directors = catalog['directors']
        director=map.get(directors,name,compareByKey)
        if director:
            lt.addLast(director['movies_id'], row['id'])
        else:
            director = newDirector(name, row)
            map.put(directors, name, director, compareByKey)

def addDirectorVoteData(catalog, name, row):
    directors = catalog['directors']
    director=map.get(directors,name,compareByKey)
    if director:
        if row["id"] in director["movies_id"]:
            lt.addLast(director['movie_titles'],row['title'])
            lt.addLast(director['movies_id'],row['id'])
            director['sum_average_rating'] += float(row['vote_average'])

def addGenre(catalog, name, row):
    """
    Adiciona un director al map y sus películas
    """
    genres = catalog['genres']
    genre =map.get(genres,name,compareByKey)
    if genre:
        lt.addLast(genre['titles'], row['title'])
        lt.addLast(genre['ids'], row['id'])
        genre['sum_average_rating'] += float(row['vote_average'])
    else:
        genre = newGenre(name, row)
        map.put(genres, name, genre, compareByKey)

def newGenre(name, row):
    """
    Crea un nuevo diccionario para una género
    """
    genre = {"name": name, "titles":lt.newList("ARRAY_LIST"), "ids": lt.newList("ARRAY_LIST"), "sum_average_rating":0}
    lt.addLast(genre["titles"], row["title"])
    lt.addLast(genre["ids"], row["id"])
    genre["sum_average_rating"] = float(row["vote_average"])
    return genre

# Funciones de consulta

def getBookInList (catalog, bookTitle):
    """
    Retorna el libro desde la lista a partir del titulo
    """
    pos = lt.isPresent(catalog['booksList'], bookTitle, compareByTitle)
    if pos:
        return lt.getElement(catalog['booksList'],pos)
    return None

def getMovieInList(catalog, movieTitle):
    """
    Retorna la película desde la lista a partir del titulo
    """
    pos = lt.isPresent(catalog['moviesList'], movieTitle, compareByTitle)
    if pos:
        return lt.getElement(catalog['moviesList'],pos)
    return None

def getBookInMap (catalog, bookTitle):
    """
    Retorna el libro desde el mapa a partir del titulo (key)
    """
    return map.get(catalog['booksMap'], bookTitle, compareByKey)

def getMovieInMap(catalog, movieTitle):
    """
    Retorna la película desde el mapa a partir del titulo (key)
    """
    return map.get(catalog['moviesMap'], movieTitle, compareByTitle)

def getAuthorInfo (catalog, authorName):
    """
    Retorna el autor a partir del nombre
    """
    return map.get(catalog['authors'], authorName, compareByKey)

def getDirectorInfo(catalog, director_name):
    """
    Retorna el director a partir del nombre
    """
    return map.get(catalog['directors'], director_name, compareByName)

# Funciones de comparacion

def compareByKey (key, element):
    return  (key == element['key'] )  

def compareByTitle(bookTitle, element):
    return  (bookTitle == element['title'] )

def compareByName(name, element):
    return (name == element["name"])