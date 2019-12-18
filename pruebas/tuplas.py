#!/usr/bin/python3

#No se pueden modificar despues de su creacion
#No permite añadir, elminar, mover elemntos (appen,extend, remove)
#si permite extraer porciones, pero el resultado de la extraccion es una tupla nueva
#si permiten comprobar si un elemnto se encuentra en una tupla

#Que utilidad - mas rapidas- menos espacio - formatean strings - claves en diccionario

#syntaxis: nombretupla=(elem1, elem2, elem3 ..)

mitupla=("Juan", 13, 1, 1995)

#para acceder a un dato espesifico
print(mitupla[1])
#Convertir tupla en una lista
mitupla=("Juan", 13, 1, 1995)
milista = list(mitupla)
print(milista)
#Convertir una lista en una tupla
milista=["Juan", 13, 1, 1995]
mitupla=tuple(milista)
print(mitupla)
#Imprimi si se encuentra en la tupla
print("juan" in mitupla)
#"count"instruccion averiguar cuantos elemntos se encuentra dentro de una tupla
print(mitupla.count(13))
#Permite averiguar longitud de una tupla
print(len(mitupla))
#Crear tupla con unico elemnto
mitupla1=("Juan",)
#empaquetado de tupla Los parentesis son opcionales
mitupla2="Sergio", 14, 15.4
print(mitupla)
#desempaquetado de una tupla - asigna los valores en orden
mitupla=("Juan", 13, 1, 1995)
name, day, month, year = mi tupla
print(mitupla)
