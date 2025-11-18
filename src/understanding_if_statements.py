# condicional ! = para determinar desigualdad

requested_toppin = 'mushrooms'
if requested_toppin != 'anchovies':
    print('hold the anchovies')
print("\n")
# comparaciones numericas
age = 18
print(age==18) #True
answer = 17
if answer !=42: #True
    print("Esa no es la respuesta correcta .intenta otra edad")

age = 19
print(age<21) #true 
print(age<=21)#true
print(age>21)#false
print(age>=21)#faslse
print("\n")
#condicionales multiples
age_0 = 22
age_1 = 18

print(age_0>=21 and age_1>21 ) #false

print(age_0>=21 and age_1>=18) #true
print("\n")
# operacion logica or


age_0 = 22
age_1 = 18


print(age_0>=21 or age_1>21 ) #True

print(age_0>=23 or age_1>=21) #false
print("\n")

# preguntarme si un valor esta en una lista 

cars = ["micro", "vocho", "tsuru", "Subaru"]
print("subaru" in cars)# True
print("chevy" in cars)# False


# Preguntarnos si un valor no esta en una lista
hechiceros = ["itadori", "nobara", "todo aoi", "geto"]
maldicion = ["mahito"]

print (maldicion not in hechiceros) #true
print ('nobara' not in hechiceros) #false


 

"""
type() - nos dice el tipo de dato
list() - crea una lista
input() - obtiene entrada del usuario
str() - convierte a cadena de texto
int() - convierte a entero
print() - muestra informacion en pantalla
tuple() - crea una tupla
len() - obtiene la longitud de un objeto
sorted() - ordena los elementos de una lista

"""