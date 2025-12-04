"""
    estructura basica del bucle while

    conditional = boolean

    while conditional"
        actions


"""

#while infinito
while True: #while infinito
    try:
        number = int(input("ingresa un numero del 25 al 50: "))
        if number >=25 and number <=50:
            print("Hola estas dentro del rango")
            break
        else:
            print("lastima tonoto")
    except:
        print("ingresa un numero")
