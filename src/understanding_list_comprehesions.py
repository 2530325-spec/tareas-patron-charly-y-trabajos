"""
    un list comprehesions combina el for loop
    y la creacuon de nuevos elementos en una sola linea de codigo.
    y automaticamente agrega los nuevos elementos a una lista.
    sin tener que utilizar el metodo .append()

"""
 # Generear una lista de cuadrados de numeros del 0 al 10
squares = [value**2 for value in range(1,11)]

print(squares)

print("\n")
# generar una lista con los numeros pares

evens = [value for value in range(101) if value % 2 == 0]
print(evens)
