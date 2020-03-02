import os
import sys
import csv

#file_path = os.path.join(os.path.dirname(__file__), '../..')
file_dir = os.path.dirname(os.path.realpath('__file__'))
#sys.path.insert(0, os.path.abspath(file_path))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
data_dir = file_dir

def loadBooks (sep=';'):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por 
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    booksfile = data_dir + '/Data/Movies/SmallMoviesDetailsCleaned.csv'
    dialect = csv.excel()
    dialect.delimiter=sep
    with open(booksfile, encoding="utf-8-sig") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        total_generos = 0
        diccionario_generos = {}
        for row in spamreader:
            generos = row["genres"].split("|")
            for i in generos:
                genero = diccionario_generos.get(i)
                if genero == None:
                   total_generos += 1
                   diccionario_generos[i] = i
        print(diccionario_generos)
        print("En total hay ", total_generos, " géneros en el archivo")
        
loadBooks()