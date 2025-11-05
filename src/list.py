# LISTAS 

"""
    las listas nos permite almacenar informacion en un lugar
    'la cantidad que tengas' : ya sean pocos elementos o 
    millones de elemento

    se recomineda nimbrar una varuabke de tipo lista en 
    PLURAL

    en python los corchetes [] indican o definen una lista 
    los elementos en una lista se separan por comas.

    EJEMPLO:

"""

my_favorite_songs = ['alright', 'are we still friend', 'she', 'almohada']

print (my_favorite_songs, type(my_favorite_songs))

print(my_favorite_songs[-1].title(), type(my_favorite_songs[-1])) 

message = "my first favorite song is: "
print(message)

cars = ["honda", "toyota", "nissan", "vmercedez benz"]

print("lista original: ", cars)

cars.append("bmw")

print("lista append: ", cars)

"""
    el metodo append() agrega elementos 
    al final de la lista

"""


camiones_1 = []

print ("lsita de camiones   : ", camiones_1)

camiones_1.append ("volvo")


print ("lsita de camiones   : ", camiones_1)

camiones_1.append ("caterpillar")

print ("lsita de camiones   : ", camiones_1)

camiones_1.append ("cummins")

print ("lsita de camiones   : ", camiones_1)

camiones_1.append ("volswagen")



# agrefar elemento en una posicion especifica


motorcycles = ["honda", "yamaga", "suzuki"]

print ("lista de motocicletas: ", motorcycles)

motorcycles.insert (0, "ducatti")

motorcycles.insert (2, "mortalika")



# ELIMINAR ELEMENTOS DE UNA LISTA USANDO  (del)

print ("lista original de motocicletas: ", motorcycles)

del motorcycles[0]

print ("lista de motocicletas despues de eliminar el primer elemento", motorcycles)


# eliminar un elemento usando el metodo (pop)

print ("lista original de motocicletas: ", motorcycles)

popped_motorcycles = motorcycles.pop()

print ("lista de motocicletas despues de usar pop()", motorcycles)


print("elemento eliminado de la lista: ", popped_motorcycles)