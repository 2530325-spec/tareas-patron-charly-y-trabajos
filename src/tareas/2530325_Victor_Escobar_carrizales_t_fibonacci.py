# Portada
# Nombre: Victor Escobar Carrizales
# Matrícula: 2530325
# Grupo: 103

# ----------------------------------------------------------------------
# 4. RESUMEN EJECUTIVO (COMENTARIOS EN EL .py)
# ----------------------------------------------------------------------

# Resumen Ejecutivo:
# La serie de Fibonacci es una secuencia matemática donde cada número es la suma
# de los dos anteriores. Comienza típicamente con 0 y 1 (o 1 y 1).
# Calcular la serie hasta un número de términos 'n' significa generar los
# primeros 'n' elementos de dicha secuencia.
# Este programa pide al usuario el valor de 'n', realiza las validaciones
# necesarias para asegurar que 'n' sea un entero positivo y dentro de un límite
# razonable, y finalmente genera e imprime la serie utilizando un bucle 'for'
# para la iteración.

# ----------------------------------------------------------------------
# 5. PLANTILLA PARA DOCUMENTAR EL PROBLEMA (COMENTARIOS)
# ----------------------------------------------------------------------

# Problem: Fibonacci series generator
# Description: Program that reads an integer 'n' and prints the first 'n' terms
# of the Fibonacci series starting at 0 and 1. The implementation uses basic
# variables and a loop for calculation, and includes robust input validation.
#
# Inputs:
# - n (string/int; number of terms to generate)
#
# Outputs:
# - "Number of terms: <n>"
# - "Fibonacci series: <term_1>, <term_2>, ..., <term_n>"
#
# Validations:
# - The input must be convertible to an integer.
# - The integer 'n' must be >= 1.
# - 'n' must be <= 50 (a defined maximum reasonable limit).
#
# Test cases:
# 1) Normal: n = 7
#    → expected series: 0, 1, 1, 2, 3, 5, 8
# 2) Border: n = 1
#    → expected series: 0
# 3) Error: n = "hello" or n = 0
#    → expected message: "Error: invalid input"

# ----------------------------------------------------------------------
# 6. PROBLEMA ÚNICO: Fibonacci series up to n terms (CÓDIGO)
# ----------------------------------------------------------------------

# Constants (UPPER_SNAKE_CASE)
MAX_TERMS = 50
MIN_TERMS = 1
ERROR_MESSAGE = "Error: invalid input"

def main():
    """
    Main function to read input, validate it, and generate the Fibonacci series.
    """
    print("\n--- Fibonacci Series Generator ---")

    # 1. Read input from user
    input_str = input(f"Enter the number of terms ({MIN_TERMS}-{MAX_TERMS}): ")

    # 2. Validation
    try:
        terms_count = int(input_str.strip())
    except ValueError:
        print(ERROR_MESSAGE)
        return

    if terms_count < MIN_TERMS or terms_count > MAX_TERMS:
        print(ERROR_MESSAGE)
        print(f"Number of terms must be between {MIN_TERMS} and {MAX_TERMS}.")
        return

    # Input is valid, proceed with calculation
    print(f"Number of terms: {terms_count}")
    print("Fibonacci series: ", end="")

    # Initialization of the first two terms
    first_term = 0
    second_term = 1
    
    # 3. Generate the series using a loop
    series_terms = []

    if terms_count >= 1:
        series_terms.append(first_term)
        
    if terms_count >= 2:
        series_terms.append(second_term)

    # Calculate remaining terms using a 'for' loop for a fixed number of iterations
    # Loop starts from the 3rd term (index 2) up to terms_count
    for i in range(2, terms_count):
        next_term = first_term + second_term
        series_terms.append(next_term)
        
        # Update variables for the next iteration
        first_term = second_term
        second_term = next_term

    # 4. Print the result
    # Joining the list elements with a comma and a space for clean output
    print(", ".join(map(str, series_terms)))


if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------
# 7. CONCLUSIONES (COMENTARIOS AL FINAL)
# ----------------------------------------------------------------------

# Conclusiones:
# El uso del bucle 'for' fue fundamental, ya que nos permitió repetir la lógica
# de suma y actualización de variables ("next = a + b", "a = b", "b = next") un
# número exacto de veces ('n'), asegurando que la serie se detenga en el término deseado.
# Es crucial manejar bien los casos especiales n=1 y n=2 fuera del bucle principal
# para inicializar la serie correctamente (0 y 1), ya que la lógica iterativa de
# suma solo aplica a partir del tercer término.
# Esta lógica de generación secuencial se podría reutilizar en otros programas,
# por ejemplo, para simular el crecimiento de poblaciones, en algoritmos de búsqueda
# (Fibonacci Search), o como un simple generador de números aleatorios con propiedades específicas.

# ----------------------------------------------------------------------
# 8. REFERENCIAS (MÍNIMO 3) – EN COMENTARIOS
# ----------------------------------------------------------------------

# References:
# 1) Python documentation – while and for loops:
#    https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
# 2) GeeksforGeeks – Fibonacci Series in Python (Iterative Approach):
#    https://www.geeksforgeeks.org/python-program-for-program-for-fibonacci-numbers/
# 3) Official Python documentation – Built-in Functions (e.g., input() and print()):
#    https://docs.python.org/3/library/functions.html