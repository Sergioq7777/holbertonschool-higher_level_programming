#!/usr/bin/python3

milista=["Maria", "Juan", "Pepe", "Antonio"]

print(milista[:])

#el primero excluye y y muestra el resto
print(milista[0:3])
#sobre entiende q es 0
print(milista[:2])
#acceda al desde eñ primero al 2
print(milista[1:2])
#accede a los dos ultimos elementos
print(milista[2:])
#agregar elemnto a lista al final
milista.append("Vanessa")
#Pide dos elemntos- indice y elemnto
milista.insert(2,"Vanessa")
#Agregar varios elemntos a una lista
milista.extend(["Vanessa", "Ana", "laura"])
#Para saber en q indice esta el nombre
print(milista.index("Juan"))
#Comprobar si un elemnto se encuentra o no en una lista. True or false
print("pepe" in milista)
#para elminar elementos
milista.remove("Ana")
#para elminar el ultimo elemnto de una lista
milista.pop()
#operador para unir se crea otras 2 listas
milista2 = [5, "lucia"]

milista3 = milista + milista2

print(milista3[:])
#operador multiplicasion

milista=["Maria", "Juan", "Pepe", "Antonio"] * 3
