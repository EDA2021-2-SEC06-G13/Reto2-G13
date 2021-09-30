"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import time


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar artistas cronologicamente en un rango de años")
    print("3- Listar cronologicamente las adquisiciones del museo en un rango de años")
    print("4- Clasificar las obras de un artista de acuerdo a la tecnica")
    print("5- Clasificar las obras por la nacionalidad de su creador")
    print("6- Calcular el costo para transportar todas las obras de un departamento")
    print("7- Proponer una nueva exposicion en el museo")


def initCatalog():
    """
    Inicializa el catalogo 
    """
    return controller.initCatalog()
"""
Menu principal
"""
def loadData():
     return controller.loadData(catalog)

catalog = None
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        #tipo_lista=input("Ingrese el tipo de lista que quiere utilizar: ")
        print("Cargando información de los archivos ....")
        catalog=initCatalog()
        loadData()
        print('Artistas cargados: ' + str(lt.size(catalog['artistas'])))
        print('Obras cargadas: ' + str(lt.size(catalog['obras'])))

    elif int(inputs[0]) == 2:
        anho_inicial=input("Ingrese el año inicial: ")
        anho_final=input("Ingrese el año final: ")
        r=controller.requerimiento_1(anho_inicial,anho_final,catalog)        
        print("Se encontraron "+ str(lt.size(r))+" artistas que nacieron entre los años "+str(anho_inicial)+ " y "+str(anho_final))
        print("Los primeros tres artistas en el rango son...")
        for i in range(1,4):
            valor=lt.getElement(r,i)
            print(valor)
        print("Los ultimos tres artistas en el rango son...")
        for j in range(lt.size(r)-2,lt.size(r)+1):
            ultimas=lt.getElement(r,j)
            print(ultimas)

 
    elif int(inputs[0]) == 3:
        fecha_inicial=input("Ingrese la fecha inicial: ")
        fecha_final=input("Ingrese la fecha final: ")
        r=controller.requerimiento_2(fecha_inicial,fecha_final,catalog)
        print("Se encontraron "+str(lt.size(r))+" obras, desde la fecha "+str(fecha_inicial)+" hasta "+str(fecha_final))
        con=0
        for i in range(1,lt.size(r)):
            comprar=lt.getElement(r,i)
            if  str(comprar["CreditLine"])==str("Purchase"):
                con+=1
        print("Se encontraron "+str(con)+" obras adquiridas por compra.")
        print("Las primeras tres obras en el rango son...")
        for i in range(1,4):
            valor=lt.getElement(r,i)
            print(valor)
        print("Las ultimas tres obras en el rango son...")
        for j in range(lt.size(r)-2,lt.size(r)+1):
            ultimas=lt.getElement(r,j)
            print(ultimas)

    elif int(inputs[0]) == 4:
        nombreArtista=input("Ingrese el nombre del artista al que quiere analizar: ")
        r=controller.requerimiento_3(nombreArtista, catalog)
        print("El total de obras del artista son: "+str(lt.size(r)))
        for i in range(1,lt.size(r)):
            valor=lt.getElement(r,i)
            print("La tecnica que mas utilizo..")
            print(valor)
            tecnica=lt.getElement(valor,1)
            cantidad=lt.getElement(valor,2)
            print(str(tecnica))
            print("CANTIDAD: "+str(cantidad))

        pass
    elif int(inputs[0]) == 5:
        inicio=time.process_time()
        r=controller.requerimiento_4(catalog)
        for i in range(1,10):
            valor=lt.getElement(r,i)
            nacionalidad=lt.getElement(valor, 1)
            cantidad=lt.getElement(valor,2)
            print(nacionalidad,cantidad)
        for mayor in range(1,4):
            val=lt.getElement(r,mayor)
            print(val)
        pass
    elif int(inputs[0]) == 6:
        departamento=input("Ingrese el departamento que quiere analizar: ")
        r=controller.requerimiento_5(departamento,catalog)
        print("Se transportaran "+str(lt.size(r))+" desde "+str(departamento))
        i=0
        for i in range(1,lt.size(r)):
            valor=lt.getElement(r,i)
            i+=valor
        print("El precio estimado es: "+str(i))

    elif int(inputs[0]) == 7:
        input("Que exposicion desea proponer:  ")
        

    elif int(inputs[0]) == 8:
        cantidad=input("Ingrese el numero de obras antiguas a las que quiere tener una visualización: ")
        medio=input("Ingrese el medio por el cual quiere analizar la informacion: ")
        r=controller.laboratorio(medio,cantidad,catalog)
        print (r)
    else:
        sys.exit(0)
sys.exit(0)