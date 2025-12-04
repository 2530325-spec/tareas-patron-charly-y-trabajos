"""

    docstring for understanding_while_centimel
    centienl is useful when you want to ensure
    that a loop runs at least once before
    cheking a condition

    ejercicio
        vamos a realizar un ekemplo que realice la 
        suma de n numeros ingresado por el usuario,
        no sabemos cuantos numeros se ingresaran,
        quiere contabilizar cuantos numeros se han ingresado,
        mostrar la suma, el minimo y el maximo de los numeros
        ingresados
"""

counter = 0
sum_values = 0.0
minimum = None
maximum = None

while True:
    user_input = input("ingresa una cantidad (mxn): ")
    if user_input == 'exit':
        break

    try:
        quantity = float(user_input)
    except:
        print("ingresa un valor valido")
        continue

    counter += 1  # counter = counter + 1
    sum_values += quantity  # sum_values = sum_values + quantity

    if minimum is None or quantity < minimum:
        minimum = quantity
    if maximum is None or quantity > maximum:
        maximum = quantity
print(f"cantidad de numeros ingresados: {counter}")
print(f"suma de los numeros ingresados: {sum_values}")
print(f"minimo de los numeros ingresados: {minimum}")
print(f"maximo de los numeros ingresados: {maximum}")

