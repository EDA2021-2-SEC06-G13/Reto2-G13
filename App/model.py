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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

from DISClib.DataStructures.arraylist import addLast
from os import replace
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    """
    Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
    los mismos.
    """


    catalog = {'artistas': None,
               'obras': None}

    catalog['artistas'] = mp.newMap(152,maptype='PROBING',loadfactor=0.5,comparefunction=cmpartistas)
    catalog["obras"] = mp.newMap(656,maptype='PROBING',loadfactor=0.5,comparefunction=cmpobras)
    catalog["medios"] = mp.newMap(40, maptype='CHAINING', loadfactor=4.00, comparefunction=cmpmedios)
    catalog["nationality"] = mp.newMap(152, maptype='PROBING', loadfactor=0.80, comparefunction=cmpnacionalidad)
    catalog["artist_medio"]=mp.newMap(152,maptype="PROBING",loadfactor=0.5,comparefunction=compareartist_medios)

                            
    return catalog



# Funciones para agregar informacion al catalogo
def addArtist(catalog, artista):
    presente = mp.contains(catalog["artistas"], artista["ConstituentID"])
    if not presente:
        mp.put(catalog["artistas"],artista["ConstituentID"],artista)
        mapa=mp.newMap(152,maptype="PROBING",loadfactor=0.5,comparefunction=compareartist_medios)

        mp.put(catalog["artist_medio"],artista["ConstituentID"],mapa)


def addObras(catalog, obras):
    presente = mp.contains(catalog["obras"], obras["ObjectID"])
    if not presente:
        mp.put(catalog["obras"],obras["ObjectID"],obras)
        ids= obras["ConstituentID"]
        ids = ids.replace("[", "").replace("]","").replace(" ", "").split(",")
        for id in ids:
            esta = mp.contains(catalog["artistas"], id)
            if esta:
                artista = mp.get(catalog["artistas"], id)
                artista= artista["value"]
                nacionalidad = artista["Nationality"]
                nacionalidad_esta = mp.contains(catalog["nationality"], nacionalidad)
                if not nacionalidad_esta:
                    nacionalidad_1=nueva_nacionalidad(nacionalidad)
                    lt.addLast(nacionalidad_1["obras"], obras)
                    nacionalidad_1["numero_obras"]=lt.size(nacionalidad_1["obras"])
                    mp.put(catalog["nationality"], nacionalidad, nacionalidad_1)
                else:
                    nacionalidad_1=mp.get(catalog["nationality"], nacionalidad)["value"]
                    lt.addLast(nacionalidad_1["obras"], obras)
                    nacionalidad_1["numero_obras"]=lt.size(nacionalidad_1["obras"])
                medio=obras["Medium"]
                mapa_artista=mp.get(catalog["artist_medio"],id)["value"]
                medio_esta=mp.contains(mapa_artista,medio)
                if not medio_esta:
                    lista_obras=lt.newList()
                    lt.addLast(lista_obras,obras)
                    mp.put(mapa_artista,medio,lista_obras)
                else:
                    lista_obras=mp.get(mapa_artista,medio)["value"]
                    lt.addLast(lista_obras,obras)
                    mp.put(mapa_artista,medio,lista_obras)
                mp.put(catalog["artist_medio"],id,mapa_artista)   
                

                    

def nueva_nacionalidad(nacionalidad):
    nacionalidad = {"nacionalidad":nacionalidad,"numero_obras":0,"obras":lt.newList() }
    return nacionalidad



def tres(medio,cantidad,catalog):
    encontrar=mp.get(catalog["medios"],medio)
    lista=me.getValue(encontrar)
    ordenada=sa.sort(lista,cmpArtWorkByDateAcquired)
    if lt.size(ordenada)>=cantidad:
        sublista=lt.subList(ordenada,1,cantidad)
        return sublista
    else:
        return ordenada


def nacionalidad(nacionalidad, catalog):
    presente = mp.contains(catalog["nationality"],nacionalidad)
    if presente:
        lista= mp.get(catalog["nationality"],nacionalidad)["value"]
        tamano = lt.size(lista)
        return tamano

 
# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista




def cmpmedios(country, count_entry):     
    ctentry = me.getKey(count_entry)    
    if (country) == (ctentry):         
        return 0     
    elif (country) > (ctentry):         
        return 1     
    else:         
        return -1


def cmpartistas(nombre_art, artist_entry):
    ctentry = me.getKey(artist_entry)    
    if int(nombre_art) == int(ctentry):         
        return 0     
    elif int(nombre_art) > int(ctentry):         
        return 1     
    else:         
        return -1


def cmpobras(id_obras, artist_entry):
    ctentry = me.getKey(artist_entry)    
    if int(id_obras) == int(ctentry):         
        return 0     
    elif int(id_obras) > int(ctentry):         
        return 1     
    else:         
        return -1
def cmpnacionalidad(nacionalidad, count_entry):
    ctentry = me.getKey(count_entry)    
    if (nacionalidad) == (ctentry):         
        return 0     
    elif (nacionalidad) > (ctentry):         
        return 1     
    else:         
        return -1

def cmpfunction(uno,dos):

    if int(uno["BeginDate"])> int(dos["BeginDate"]):
        r=True
    else:
        r=False
    return r
def cmpArtWorkByDateAcquired(uno,dos):
    x=str(uno["DateAcquired"])
    y=str(dos["DateAcquired"])
    if x> y:
        r=True
    else:
        r=False
    return r
def compareobras(obra1,obra2):
    if (lt.getElement(obra2, 1) ==obra1):
        return 0
    return -1
def comparepais(pais1, pais2):
    return (lt.getElement(pais1,2) >lt.getElement(pais2,2))
def comparepaises(pais1, pais2):
    if (lt.getElement(pais2, 1) ==pais1):
        return 0
    return -1
def less(element1, element2):
    if int(element1["numero_obras"]) > int(element2["numero_obras"]):
        return True

def compareartist_medios(medio,medio_entry):
    ctentry = me.getKey(medio_entry)    
    if (medio) == (ctentry):         
        return 0     
    elif (medio) > (ctentry):         
        return 1     
    else:         
        return -1

# Funciones de ordenamiento



#Como curador del museo quiero listar cronológicamente los artistas que nacieron en un rango de años.


def artistasCronologicamente(anho_inicio, anho_final,catalog):
    lista=mp.valueSet(catalog["artistas"])
    ordenar=sa.sort(lista,cmpfunction)
    lista_1234=lt.newList("ARRAY_LIST")
    for i in range(1,lt.size(ordenar)+1):
        anho=lt.getElement(ordenar,i)
        if int(anho["BeginDate"])>= int(anho_inicio) and int(anho["BeginDate"])<=int(anho_final):
            lt.addLast(lista_1234,anho)
    return lista_1234



def adquisicionCronologicamente(fecha_inicial,fecha_final,catalog):
    lista = mp.valueSet(catalog["obras"])
    ordenar=sa.sort(lista,cmpArtWorkByDateAcquired)
    lista=lt.newList("ARRAY_LIST")
    for i in range(1,lt.size(ordenar)+1):
        anho=lt.getElement(ordenar,i)
        x=str((anho["DateAcquired"]))
        if x>=(fecha_inicial) and x<=(fecha_final):
            lt.addLast(lista,anho)
    return lista

        

def clasificarobras(nombreArtista,catalog):
    
    lista=lt.newList('ARRAY_LIST',
                                    cmpfunction=compareobras)
    
    i =1
    while i <= lt.size(catalog["artistas"]):
        artista = lt.getElement(catalog["artistas"], i)
        if nombreArtista==artista["DisplayName"]:
            #print ("funciona1")
            iden = artista["ConstituentID"]
            
            j = 1   
            while j <= lt.size(catalog["obras"]):
                obra = lt.getElement(catalog["obras"], j)
                ids = obra["ConstituentID"]
                ids = ids.replace("[", "").replace("]","").replace(" ", "").split(",")
                for id in ids:
                    
                    if id == iden:
                        #print ("funciona2")
                        tecnica = obra["Medium"]
                        if lt.isPresent(lista, tecnica)==0:
                            #print ("funciona3")

                            lista_2 = lt.newList()
                            lt.addLast(lista_2, tecnica)
                            lt.addLast(lista_2, 1)
                            lt.addLast(lista, lista_2)
                    
                        else:
                            tecnicas= lt.getElement(lista,lt.isPresent(lista,tecnica))
                            cantidad=lt.getElement(tecnicas,2)
                            lt.changeInfo(tecnicas,2,cantidad+1)               
                j+=1
        i+=1
    sorted_list = sa.sort(lista, comparepais)
    return sorted_list
    
"""""
def clasificar_obras2(nombreArtista, catalog):
"""


def clasificarObrasNacionalidad(catalog):
    lista_nacionalidad = mp.valueSet(catalog["nationality"])  
    lista_ordenada = sa.sort(lista_nacionalidad, less)
    return lista_ordenada

    """
    lista=lt.newList('ARRAY_LIST',
                                    cmpfunction=comparepaises)
    
    i =1
    while i <= lt.size(catalog["obras"]):
        obra = lt.getElement(catalog["obras"], i)
        ids = obra["ConstituentID"]
        ids = ids.replace("[", "").replace("]","").replace(" ", "").split(",")
        
        for id in ids:
            j = 1
            encontre_artista=False
            
            while j<= lt.size(catalog["artistas"]) and not encontre_artista:
                artista = lt.getElement(catalog["artistas"], j)
                iden= artista["ConstituentID"]
                
                if id == iden:
                    encontre_artista=True
                    nacionalidad = artista["Nationality"]
                    if nacionalidad == "":
                        nacionalidad = "Unknown"
                    if lt.isPresent(lista, nacionalidad)==0:

                        lista_2 = lt.newList()
                        lt.addLast(lista_2, nacionalidad)
                        lt.addLast(lista_2, 1)
                        lt.addLast(lista, lista_2)
                    
                    else:
                        pais= lt.getElement(lista,lt.isPresent(lista,nacionalidad))
                        cantidad=lt.getElement(pais,2)
                        lt.changeInfo(pais,2,cantidad+1)               
                j+=1
        i+=1
    sorted_list = sa.sort(lista, comparepais)
    return sorted_list"""


def transportar_obras(catalog,departamento):
    ordenar=sa.sort(catalog["obras"],compareobras)
    lista=lt.newList("ARRAY_LIST")
    obra=lt.getElement(catalog["obras"])
    for i in range(1,lt.size(ordenar)+1):
        lugar=obra["Department"]
        if lugar==departamento:
            lt.addLast(lista, obra)
    lista2=lt.newList()
    for i in range(1,lt.size(lista)):
        r=calcular_costo(i)
        lt.addLast(lista2,r)
    return lista2

def calcular_costo(obra):
    valor={"kg":0,
    "M2caj":0,
    "M22caj":0,
    "M23caj":0,
    "M3":0,
    "M2C":0,
    "M3C":0}

    if obra["Weight (kg)"]:
        valor["kg"]=72*obra["Weight (kg)"]
    if obra["Width (cm)"] and obra["Height (cm)"]:
        valor["M22caj"]=72*(obra["Width (cm)"]/100*(obra["Height (cm)"]/100))
    if obra["Width (cm)"] and obra["Lenght (cm)"]:
        valor["M22caj"]=72*(obra["Width (cm)"]/100*(obra["Lenght (cm)"]/100))
    if obra["Lenght (cm)"] and obra["Height (cm)"] and obra["Width (cm)"]:
        valor["M3caj"]=72*(obra["Lenght (cm)"]/100*(obra["Height (cm)"]/100)*(obra["Width (cm)"]/100))
    if obra["Lenght (cm)"] and obra["Height (cm)"]:
        valor["M2caj"]=72*(obra["Lenght (cm)"]/100*(obra["Height (cm)"]/100))
    if obra["Diameter (cm)"]:
        valor["M2C"]=72*(((obra["Diameter (cm)"]/200)**2)*3.14)
    if obra["Diameter (cm)"] and obra["Height (cm)"]:
        valor["M3C"]=72*(((obra["Diameter (cm)"]/200)**2)*3.14*(obra["Height (cm)"]/100))
    if obra["Diameter (cm)"] and obra["Depth (cm)"]:
        valor["M3C"]=72*(((obra["Diameter (cm)"]/200)**2)*3.14*(obra["Depth (cm)"]/100))
    
    menor=0
    for costo in valor.values():
        if costo>menor:
            menor=costo
    if menor==0:
        r=48
    else:
        r=menor
    return r

    
    
   
   
   
    
    
   




