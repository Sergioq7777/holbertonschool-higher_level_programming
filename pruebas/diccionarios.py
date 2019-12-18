#!/usr/bin/python3

#Estructura de datos que nos permite almacenar valores de diferente 
#Tipos enteros cadenas de texto, decimales, incluso listas
#Sus datos almacenan asociados a una clave q crea una asociacion de tipo clave:valor para cada valor
#Datos almacenados no ordenados.
#CLAVE : VALOR



midiccionario={"Alemania":"Berlin", "Francia":"Paris", "España":"Madrid"}

#imprimir informacion de la clave
print(midiccionario["Francia"])
#imprimir todo el diccionario
print(midiccionario)
#Agregar nuevo elemnto a ddicionario
midiccionario={"Alemania":"Berlin", "Francia":"Paris", "España":"Madrid"}
midiccionario["Italia"]="Lisboa"
print(midiccionario)
#Modificar dato erroneo - sobre escribir
midiccionario["Italia"]="Roma"
#Eliminar un elemnto con la clave
del midiccionario ["España"]
#Crear diccionario variado
midiccionario2={"Alemania":"Berlin", 23:"jordan", "España":27}
#Utilizar una tupla para  asignar claves
mitupla=["España", "Reino Unido", "Alemania", "Francia"]
midiccionario={mitupla[0]:"Madrid", mitupla[1]:"Paris", mitupla[2]:"Berlin", mitupla[3]:"Londres", }
print(midiccionario)
#Diccionario almacene junto con otros valores una tupla-- diccionario adicional
midiccionario2={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":[1991,1992,1993]}}
print(midiccionario)
#Imprime todas las claves
print(midiccionario.keys())
#Imprimi los valores
print(midiccionario.values())
#Imprime longitud de diccionario
print(len(midiccionario))
