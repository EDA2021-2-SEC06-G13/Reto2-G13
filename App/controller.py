"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog



# Funciones para la carga de datos
def loadData(catalog):
    loadArtistas(catalog)
    loadObras(catalog)
    


def loadArtistas(catalog):
    artistasfile = cf.data_dir + 'Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistasfile, encoding='utf-8'))
    for artista in input_file:
        model.addArtist(catalog, artista)

def loadObras(catalog):

    artistasfile = cf.data_dir + 'Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artistasfile, encoding='utf-8'))
    for obras in input_file:
        model.addObras(catalog, obras)

def requerimiento_1(anho_inicial,anho_final,catalog):
    return model.artistasCronologicamente(anho_inicial,anho_final,catalog)

def requerimiento_2(fecha_inicial,fecha_final,catalog):
    return model.adquisicionCronologicamente(fecha_inicial,fecha_final,catalog)

def requerimiento_3(nombreArtista,catalog):
    return model.clasificarobras(nombreArtista,catalog)


def requerimiento_4(catalog):
    return model.clasificarObrasNacionalidad(catalog)


def requerimiento_5(catalog,departamento):
    return model.transportar_obras(catalog,departamento)

def laboratorio(medio,cantidad,catalog):
    return model.tres(medio,cantidad,catalog)


# Funciones de ordenamiento

    
# Funciones de consulta sobre el catálogo

