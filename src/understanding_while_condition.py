"""
Docstring for understanding_while_condition
This module demonstrates the use of a while loop with a condition
     vamos a hacer un programa
     que describa un pin correcto
     que describa un pin correcto
     definamos un maximo de intentos
     y el usuario ingrese el pin correcto

     si el pin es correcto ,mostramos un mensaje

     """


VALID_PIN = "1234"
MAX_ATTEMPTS = 3
attempts = 0
while attempts < MAX_ATTEMPTS:
    user_pin = input("Please enter your PIN: ")
    if user_pin == VALID_PIN:
        print("PIN accepted. Access granted.")
        break
    else:
        attempts += 1
        print(f"Incorrect PIN. You have {MAX_ATTEMPTS - attempts} attempts left.")
else:
     print("Maximum attempts reached. Access denied.")


