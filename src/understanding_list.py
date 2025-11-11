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
print(message + my_favorite_songs[0].title())
print("")

cars = ["honda", "toyota", "nissan", "mercedez benz", "volvo"]

print("lista original: ", cars)

cars.append("bmw")
print("")

print("lista append: ", cars)
print("")

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
print("")



# agrefar elemento en una posicion especifica


motorcycles = ["honda", "yamaga", "suzuki"]

print ("lista de motocicletas: ", motorcycles)

motorcycles.insert (0, "ducatti")

motorcycles.insert (2, "mortalika")
print("")




# ELIMINAR ELEMENTOS DE UNA LISTA USANDO  (del)

print ("lista original de motocicletas: ", motorcycles)

del motorcycles[0]

print ("lista de motocicletas despues de eliminar el primer elemento", motorcycles)
print("")


# eliminar un elemento usando el metodo (pop)

print ("lista original de motocicletas: ", motorcycles)

popped_motorcycles = motorcycles.pop()

print ("lista de motocicletas despues de usar pop()", motorcycles)


print("elemento eliminado de la lista: ", popped_motorcycles)
print("")

# eliminar elemtnos de una lista por valor

motorcycles.remove ("yamaga")

print(motorcycles) 

print("")

# Ordenara listas 

#permanentemente metodo .sort() 

print (cars)

cars.sort()

print (cars)


cars.sort(reverse=True)

print (cars)

print(len(cars))


"""
    lista de metodos de list
    .insert()
    .append()
    .pop()
    .remove()
    .sort()
    ____________________________________________________________________
    Built in
    str()
    type()
    print()
    len()----cantidad de elementos
"""

best_tech = ["ipod", "mp3", "3ds", "digital camera", "pspvita", "ereader"]


print (best_tech)

best_tech.reverse()

print (best_tech)

sorted_best_tech = sorted(best_tech)
print (sorted_best_tech)

print (best_tech)



"""


    las listas tambien pueden contener numeros 
    y de hecho son ideales para eso. python ofrece muchas herramientas
    que ayudan a trabajar de manera eficiente con listas de numeros

"""

print("/n")

# METODO Range
# nos ayuda a generar facilmente series de numeros
# EJEMPLO:

print("numeros del 0 al 9")
for number in range(10):

    print(number)
first_10_numbers = list(range(10))
print(first_10_numbers)
print("numeros del 1 al 4")

for number in range(1,5):
    print(number)
numebrs_1_to_4 = list(range(1,5))
print(numebrs_1_to_4)

print("imprime los numeros impares entre el 0 y el 10")
for number in range (1,11,2):
    print(number)
numbers_impares = list(range(1,11,2))
print(numbers_impares)
print("imprime la tabla del 8")

for number in range (0,81,8):
    print(number)
tabla_del_8 = list(range(0,81,8))
print(tabla_del_8)
print("--------------------------------------------------------------------------------")

print("generar una lista con los caudrados de los primeros 10 numeros")
squares = []
for number in range(1,11):
    square = number ** 2
    squares.append(square)
    print(squares)



    ##### otro metodo built-in

    digits = [1,2,3,4,5,6,7,8,9,0]
    print("el maximo valor en la lista digits es: ", max(digits)) ### salida 9
    print("el minimo valor en la lista digits es: ", min(digits))### salida 0
    print("la suma de todos los valores en la lista digits es: ", sum(digits))###salida 45


    