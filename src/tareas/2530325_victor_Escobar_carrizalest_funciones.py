# ==============================================================================
# PORTADA
# ==============================================================================
# Nombre del Estudiante:Escobar Carrizales Victor
# Matrícula: 2530325
# Grupo: 103
# Tarea: Dominio de Funciones en Python
# ==============================================================================

# ==============================================================================
# RESUMEN EJECUTIVO
# ==============================================================================
# ¿Qué es una función en Python y para qué sirve?
# Una función en Python es un bloque de código reusable que realiza una tarea específica.
# Permite organizar el código, hacerlo modular y mejorar la legibilidad, evitando la repetición.

# ¿Qué diferencia hay entre parámetros (definition) y argumentos (call)?
# Los parámetros son los nombres de las variables listadas en la definición de la función (def).
# Los argumentos son los valores reales que se pasan a la función cuando se llama (call).

# ¿Por qué es útil separar la lógica en funciones reutilizables?
# Facilita el principio DRY (Don't Repeat Yourself), hace que el código sea más fácil de probar,
# mantener y entender, ya que cada función se enfoca en una única responsabilidad.

# ¿Qué es un valor de retorno y por qué es mejor devolver resultados en lugar de solo imprimirlos?
# Un valor de retorno es el resultado que una función le pasa de vuelta al código que la llamó, usando 'return'.
# Es mejor devolver valores para permitir que el código llamador decida qué hacer con ellos
# (imprimir, usar en otro cálculo, guardar en una base de datos), manteniendo la función pura y reutilizable.

# ¿Qué cubrirá tu documento?
# Este documento cubre la implementación de seis problemas de programación, aplicando funciones con parámetros,
# valores de retorno y argumentos nombrados/por defecto. Cada problema incluye una descripción, entradas, salidas,
# validaciones y tres casos de prueba específicos.
# ==============================================================================

# ==============================================================================
# PRINCIPIOS Y BUENAS PRÁCTICAS
# ==============================================================================
# 1. Single Responsibility Principle: Preferir funciones pequeñas que hagan una sola cosa (e.g., one function for area, one for perimeter).
# 2. DRY (Don't Repeat Yourself): Evitar la repetición de código; si la lógica se copia, se extrae en una función.
# 3. Purity: Intentar que las funciones sean "puras" (mismo input -> mismo output, sin efectos secundarios externos), como en el problema de descuento.
# 4. Documentation: Usar comentarios simples para documentar el propósito de cada función y sus parámetros.
# 5. Clear Naming: Dar nombres claros y descriptivos a las funciones (lower_snake_case).
# ==============================================================================


# ==============================================================================
# 7.1 Problem 1: Rectangle area and perimeter (basic functions)
# ==============================================================================

# Problem 1: Rectangle Calculations
# Description: Defines two functions to calculate the area and perimeter of a rectangle
#              given its width and height.
#
# Inputs:
# - width (float): The width of the rectangle.
# - height (float): The height of the rectangle.
#
# Outputs:
# - "Area:" <area_value>
# - "Perimeter:" <perimeter_value>
# - If invalid, "Error: invalid input"
#
# Validations:
# - width must be > 0.
# - height must be > 0.
#
# Test cases:
# 1) Normal: width=5.0, height=10.0 -> Area: 50.0, Perimeter: 30.0
# 2) Border: width=0.1, height=0.1 -> Area: 0.01, Perimeter: 0.4
# 3) Error: width=-5.0, height=10.0 -> Error: invalid input

def calculate_area(width: float, height: float) -> float:
    """Calculates the area of a rectangle."""
    return width * height

def calculate_perimeter(width: float, height: float) -> float:
    """Calculates the perimeter of a rectangle."""
    return 2 * (width + height)

def run_problem_1(width: float, height: float):
    """Runs tests for Problem 1 with validation."""
    print("\n--- Problem 1: Rectangle Calculations ---")
    if width <= 0 or height <= 0:
        print("Error: invalid input")
        return

    area = calculate_area(width, height)
    perimeter = calculate_perimeter(width, height)
    
    # Output
    print(f"Width: {width}, Height: {height}")
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")

# Test Cases for Problem 1
run_problem_1(5.0, 10.0)    # 1) Normal
run_problem_1(0.1, 0.1)    # 2) Border
run_problem_1(-5.0, 10.0)  # 3) Error (invalid input)


# ==============================================================================
# 7.2 Problem 2: Grade classifier (function with return string)
# ==============================================================================

# Problem 2: Grade Classifier
# Description: Defines a function to classify a numeric score (0-100) into a letter category (A, B, C, D, F).
#
# Inputs:
# - score (float or int): The numeric grade to classify.
#
# Outputs:
# - "Score:" <score>
# - "Category:" <grade_letter>
# - If invalid, "Error: invalid input"
#
# Validations:
# - score must be within the range [0, 100].
#
# Test cases:
# 1) Normal: score=85 -> Score: 85, Category: B
# 2) Border: score=90 -> Score: 90, Category: A
# 3) Error: score=105 -> Error: invalid input

def classify_grade(score: float) -> str:
    """
    Classifies a score (0-100) into a letter grade.
    Returns "A", "B", "C", "D", or "F".
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def run_problem_2(score: float):
    """Runs tests for Problem 2 with validation."""
    print("\n--- Problem 2: Grade Classifier ---")
    
    # Validation
    MIN_SCORE = 0
    MAX_SCORE = 100
    if not (MIN_SCORE <= score <= MAX_SCORE):
        print(f"Score: {score}")
        print("Error: invalid input")
        return

    grade_letter = classify_grade(score)
    
    # Output
    print(f"Score: {score}")
    print(f"Category: {grade_letter}")

# Test Cases for Problem 2
run_problem_2(85)   # 1) Normal (B)
run_problem_2(90)   # 2) Border (A)
run_problem_2(105)  # 3) Error (invalid input)


# ==============================================================================
# 7.3 Problem 3: List statistics function (min, max, average)
# ==============================================================================

# Problem 3: List Statistics
# Description: Defines a function that takes a list of numbers and returns a dictionary
#              containing the minimum, maximum, and average of the list.
#
# Inputs:
# - numbers_text (string): A comma-separated string of numbers (e.g., "10,20,30").
# - Internally: numbers_list (list of float or int).
#
# Outputs:
# - "Min:" <min_value>
# - "Max:" <max_value>
# - "Average:" <average_value>
# - If invalid, "Error: invalid input"
#
# Validations:
# - numbers_text must not be empty after strip().
# - The resulting list must not be empty.
# - All elements must be convertible to numbers.
#
# Test cases:
# 1) Normal: "10,20,30,40" -> Min: 10.0, Max: 40.0, Average: 25.0
# 2) Border: "100" -> Min: 100.0, Max: 100.0, Average: 100.0
# 3) Error: "10,20,abc" -> Error: invalid input

from typing import Dict, List, Union

def summarize_numbers(numbers_list: List[Union[int, float]]) -> Dict[str, float]:
    """
    Calculates the minimum, maximum, and average of a list of numbers.
    Assumes the input list is not empty.
    """
    min_val = min(numbers_list)
    max_val = max(numbers_list)
    average = sum(numbers_list) / len(numbers_list)
    
    return {
        "min": min_val,
        "max": max_val,
        "average": average
    }

def run_problem_3(numbers_text: str):
    """Runs tests for Problem 3 with validation and number parsing."""
    print("\n--- Problem 3: List Statistics ---")
    print(f"Input text: '{numbers_text}'")
    
    if not numbers_text.strip():
        print("Error: invalid input (empty text)")
        return
        
    # Split and attempt conversion
    numbers_list = []
    try:
        # Split by comma and strip whitespace from each part
        str_numbers = [s.strip() for s in numbers_text.split(',')]
        
        # Validation: Check for empty strings resulting from multiple commas
        str_numbers = [s for s in str_numbers if s]
        
        for s in str_numbers:
            numbers_list.append(float(s))
            
    except ValueError:
        print("Error: invalid input (non-numeric elements)")
        return

    # Validation: Check if the final list is empty
    if not numbers_list:
        print("Error: invalid input (list is empty)")
        return

    # Call the core function
    stats = summarize_numbers(numbers_list)
    
    # Output
    print(f"Min: {stats['min']}")
    print(f"Max: {stats['max']}")
    print(f"Average: {round(stats['average'], 2)}")

# Test Cases for Problem 3
run_problem_3("10,20,30,40")    # 1) Normal
run_problem_3("100")            # 2) Border (single element)
run_problem_3("10,20,abc")      # 3) Error (non-numeric element)


# ==============================================================================
# 7.4 Problem 4: Apply discount list (pure function)
# ==============================================================================

# Problem 4: Apply Discount
# Description: Defines a pure function that calculates discounted prices for a list
#              of prices based on a given discount rate, returning a new list.
#
# Inputs:
# - prices_text (string): A comma-separated string of prices (e.g., "100,200,300").
# - discount_rate (float): The rate of discount (e.g., 0.10 for 10%).
#
# Outputs:
# - "Original prices:" <original_list>
# - "Discounted prices:" <discounted_list>
# - If invalid, "Error: invalid input"
#
# Validations:
# - Resulting price list must not be empty.
# - All prices must be > 0.
# - 0 <= discount_rate <= 1.
#
# Test cases:
# 1) Normal: "100,200", rate=0.10 -> Original: [100.0, 200.0], Discounted: [90.0, 180.0]
# 2) Border: "10, 1000", rate=0.00 -> Original: [10.0, 1000.0], Discounted: [10.0, 1000.0]
# 3) Error: "100,200", rate=1.5 -> Error: invalid input (rate out of range)

def apply_discount(prices_list: List[float], discount_rate: float) -> List[float]:
    """
    Calculates discounted prices based on the rate.
    Returns a new list (pure function).
    """
    # Calculate multiplier (e.g., 0.10 discount means multiplier is 0.90)
    multiplier = 1.0 - discount_rate
    
    # Use a list comprehension for conciseness and to ensure a new list is created
    discounted_prices = [round(price * multiplier, 2) for price in prices_list]
    
    return discounted_prices

def run_problem_4(prices_text: str, discount_rate: float):
    """Runs tests for Problem 4 with validation and number parsing."""
    print("\n--- Problem 4: Apply Discount ---")
    print(f"Input prices: '{prices_text}', Discount Rate: {discount_rate}")

    # 1. Validate Discount Rate
    if not (0.0 <= discount_rate <= 1.0):
        print("Error: invalid input (discount rate must be between 0 and 1)")
        return
        
    # 2. Parse Prices
    original_prices = []
    try:
        str_prices = [s.strip() for s in prices_text.split(',')]
        str_prices = [s for s in str_prices if s] # Remove empty strings
        
        for s in str_prices:
            price = float(s)
            # 3. Validate Price Range
            if price <= 0:
                print("Error: invalid input (price must be greater than 0)")
                return
            original_prices.append(price)
            
    except ValueError:
        print("Error: invalid input (non-numeric price elements)")
        return

    # 4. Validate List Content
    if not original_prices:
        print("Error: invalid input (price list is empty)")
        return
        
    # Call the core function
    discounted_prices = apply_discount(original_prices, discount_rate)
    
    # Output
    print(f"Original prices: {original_prices}")
    print(f"Discounted prices: {discounted_prices}")

# Test Cases for Problem 4
run_problem_4("100,200,300", 0.10)   # 1) Normal (10% discount)
run_problem_4("10, 1000", 0.00)      # 2) Border (0% discount)
run_problem_4("100,200", 1.5)        # 3) Error (rate out of range)


# ==============================================================================
# 7.5 Problem 5: Greeting function with default parameters
# ==============================================================================

# Problem 5: Greeting Function
# Description: Defines a function 'greet' that constructs a greeting message.
#              It uses an optional 'title' parameter with a default value.
#
# Inputs:
# - name (string): The person's name.
# - title (string, optional): A title (e.g., "Dr.", "Eng."). Default is "".
#
# Outputs:
# - "Greeting:" <greeting_message>
# - If invalid, "Error: invalid input"
#
# Validations:
# - name must not be empty after strip().
# - title can be empty.
#
# Test cases:
# 1) Normal: name="Alice", title="Dr." -> Greeting: Hello, Dr. Alice!
# 2) Border: name="Bob", title="" (using default) -> Greeting: Hello, Bob!
# 3) Error: name=" ", title="Eng." -> Error: invalid input

def greet(name: str, title: str = "") -> str:
    """
    Generates a greeting message, optionally including a title.
    Title parameter has a default value of "".
    """
    # Clean up inputs before combining
    clean_name = name.strip()
    clean_title = title.strip()
    
    full_name = clean_name
    
    if clean_title:
        # Concatenate title and name if title is provided
        full_name = f"{clean_title}. {clean_name}"
    
    return f"Hello, {full_name}!"

def run_problem_5(name: str, title: str = ""):
    """Runs tests for Problem 5 with validation."""
    print("\n--- Problem 5: Greeting Function ---")
    print(f"Input: name='{name}', title='{title}'")
    
    # Validation
    if not name.strip():
        print("Error: invalid input (name cannot be empty)")
        return

    # Test case 1: Positional arguments
    if title == "Dr.": # Special case to test positional call
        greeting = greet(name, title)
        print("Call (Positional):")
        print(f"Greeting: {greeting}")

    # Test case 2: Named arguments (using default for empty title)
    elif not title:
        greeting = greet(name=name)
        print("Call (Named, Default):")
        print(f"Greeting: {greeting}")
        
    # Test case 3: Named arguments (full)
    else:
        greeting = greet(name=name, title=title)
        print("Call (Named, Full):")
        print(f"Greeting: {greeting}")

# Test Cases for Problem 5
run_problem_5("Alice", "Dr.")     # 1) Normal (Positional)
run_problem_5("Bob")              # 2) Border (Named, Default)
run_problem_5(" ", "Eng.")        # 3) Error (invalid input - empty name)


# ==============================================================================
# 7.6 Problem 6: Factorial function (iterative or recursive)
# ==============================================================================

# Problem 6: Factorial Function
# Description: Defines a function to calculate the factorial of a non-negative integer n (n!).
#              Implementation choice: Iterative (using a for loop).
#
# Inputs:
# - n (int): The non-negative integer for factorial calculation.
#
# Outputs:
# - "n:" <n>
# - "Factorial:" <factorial_value>
# - If invalid, "Error: invalid input"
#
# Validations:
# - n must be an integer.
# - n must be >= 0.
# - n is optionally limited to N_LIMIT to prevent overflow/long calculation.
#
# Test cases:
# 1) Normal: n=5 -> n: 5, Factorial: 120
# 2) Border: n=0 -> n: 0, Factorial: 1
# 3) Error: n=-2 -> Error: invalid input

N_LIMIT = 20  # Constant: Maximum reasonable input for factorial

def factorial(n: int) -> int:
    """
    Calculates the factorial of n (n!).
    Implementation: Iterative method.
    """
    if n == 0:
        return 1
        
    result = 1
    # Iterate from 1 up to and including n
    for i in range(1, n + 1):
        result *= i
    
    return result

def run_problem_6(n: int):
    """Runs tests for Problem 6 with validation."""
    print("\n--- Problem 6: Factorial Function ---")
    
    # Validation
    if not isinstance(n, int) or n < 0 or n > N_LIMIT:
        print(f"n: {n}")
        print("Error: invalid input (n must be a non-negative integer <= 20)")
        return

    # Call the core function
    factorial_value = factorial(n)
    
    # Output
    print(f"n: {n}")
    print(f"Factorial: {factorial_value}")

# Test Cases for Problem 6
run_problem_6(5)    # 1) Normal
run_problem_6(0)    # 2) Border (0!)
run_problem_6(-2)   # 3) Error (invalid input - negative)
run_problem_6(21)   # Additional Error Test (out of N_LIMIT)

# ==============================================================================
# 8. CONCLUSIONES
# ==============================================================================
# El desarrollo de esta tarea confirmó la importancia de las funciones como herramientas de organización.
# Permiten desglosar problemas complejos en piezas manejables, lo cual se vio claramente al separar el cálculo
# de área y perímetro en el Problema 1. Devolver valores con 'return' (Problemas 1-6) en lugar de solo imprimir
# asegura que las funciones son unidades de cálculo puras, cuyos resultados pueden ser usados flexiblemente por
# el código principal, en lugar de forzar un efecto secundario. La implementación de parámetros con valor
# por defecto (Problema 5) demostró cómo el código se vuelve más flexible, permitiendo llamadas con menos argumentos.
# Finalmente, la clara distinción entre la lógica principal (que solo llama y muestra resultados) y las funciones
# de apoyo (que contienen toda la lógica de validación y cálculo) simplificó la depuración y lectura del código.
# ==============================================================================

# ==============================================================================
# 9. REFERENCIAS
# ==============================================================================
# References:
# 1) Python documentation - Defining Functions (def, return, parameters): https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# 2) PEP 8 - Style Guide for Python Code (Naming Conventions - lower_snake_case, UPPER_SNAKE_CASE): https://peps.python.org/pep-0008/
# 3) GeeksforGeeks - Python Functions (Parameters vs. Arguments, Default Arguments): https://www.geeksforgeeks.org/python-functions/
# 4) Fluent Python - Chapter 7: Functions as First-Class Objects (Concept of Pure Functions and Side Effects).
# 5) Official Python Tutorial on Data Structures (Lists and Dictionaries usage for Problem 3 & 4): https://docs.python.org/3/tutorial/datastructures.html
# ==============================================================================