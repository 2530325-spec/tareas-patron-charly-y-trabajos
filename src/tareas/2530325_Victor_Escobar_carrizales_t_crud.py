# Portada
# Nombre: Victor Escobar Carrizales
# Matrícula: 2530325
# Grupo: 103
# ----------------------------------------------------------------------
# 4. RESUMEN EJECUTIVO (COMENTARIOS EN EL .py)
# ----------------------------------------------------------------------

# Resumen Ejecutivo:
# Un CRUD (Create, Read, Update, Delete) es el conjunto de operaciones básicas
# para gestionar datos persistentes. 'Create' añade nuevos datos, 'Read' los
# recupera, 'Update' modifica los datos existentes y 'Delete' los elimina.
# Elegí la estructura de datos de una **lista de diccionarios** (Opción B)
# porque simula mejor una tabla de base de datos o una colección de registros,
# donde cada diccionario es un ítem con campos definidos (id, name, price, quantity).
# El uso de funciones (una por cada operación CRUD) ayuda a organizar la lógica,
# promoviendo la **separación de responsabilidades** y haciendo el código más
# modular y fácil de mantener.
# El programa cubre un menú principal que permite al usuario interactuar para
# crear, leer, actualizar, eliminar y listar todos los ítems de inventario,
# incluyendo validaciones robustas para la entrada de datos.

# ----------------------------------------------------------------------
# 5. PLANTILLA PARA DOCUMENTAR EL PROBLEMA (COMENTARIOS)
# ----------------------------------------------------------------------

# Problem: In-memory CRUD manager with functions
#
# Descripción: Programa que implementa un CRUD (Crear, Leer, Actualizar, Eliminar)
# simple para elementos de inventario almacenados en una lista de diccionarios,
# usando funciones en Python para cada operación y un menú de texto para
# interactuar con el usuario. Las entradas son validadas rigurosamente.
#
# Inputs:
# - User menu options (string or int, e.g., '1' for Create, '0' for Exit).
# - For CREATE/UPDATE: item_id (string), name (string), price (string/float), quantity (string/int).
# - For READ/DELETE: item_id (string).
#
# Outputs:
# - Messages indicating the result of each operation:
#   - "Item created", "Item updated", "Item deleted", "Item not found", "Items list:", etc.
# - Error messages like "Error: invalid input" or "Error: ID already exists".
#
# Validations:
# - Menu option must be valid (0 to 5).
# - item_id must not be empty after strip().
# - Numeric fields (price, quantity) must be valid numbers:
#   - price >= 0.0
#   - quantity >= 0
# - In CREATE: item_id must be unique (ID already exists error if duplicated).
# - In READ/UPDATE/DELETE: If the id does not exist, show "Item not found".
# - If any validation fails, show "Error: invalid input" and abort the operation.
#
# Test cases:
# 1) Normal:
#    - Action: Create (ID: 'A1', Name: 'Laptop', Price: '1200.50', Quantity: '10'). Read 'A1'. Update 'A1' (New Qty: '5'). Delete 'A1'. List all.
#    - Expected: "Item created", item details shown, "Item updated", "Item deleted", "Items list:" (empty).
# 2) Border:
#    - Action: Create (ID: 'B2', Name: 'Cable', Price: '0.0', Quantity: '0'). Read 'B2'.
#    - Expected: "Item created", item details shown (zero values allowed as valid minimal data).
# 3) Error:
#    - Action: Invalid menu option ('7'). Create (ID: '', Name: 'Test', Price: '10', Quantity: '1'). Create (ID: 'A1', Name: 'Laptop', Price: '-1', Quantity: '10').
#    - Expected: "Error: invalid input" (for menu option '7'), "Error: invalid input" (for empty ID), "Error: invalid input" (for negative price).

# ----------------------------------------------------------------------
# 6. PROBLEMA ÚNICO: CRUD CON FUNCIONES (CÓDIGO)
# ----------------------------------------------------------------------

# 6.1 Estructura de datos elegida:
# Chosen data structure: Option B (list of dictionaries).
# Rationale: It's flexible, easy to iterate, and each dictionary clearly represents an item/record.

# Constants (UPPER_SNAKE_CASE)
EXIT_OPTION = '0'

# Global data structure (The "in-memory database")
# inventory_data = [{"id": "...", "name": "...", "price": ..., "quantity": ...}]
inventory_data = []

# --- Helper Functions for Validation ---

def is_valid_numeric_field(value_str, field_name):
    """
    Validates if a string can be converted to a non-negative float/int.
    """
    try:
        if field_name == "quantity":
            value = int(value_str)
        else: # price
            value = float(value_str)
        
        if value < 0:
            return False, f"{field_name} must be non-negative."
        return True, value
    except ValueError:
        return False, f"{field_name} must be a valid number."

def get_item_index(data_structure, item_id):
    """
    Finds the index of an item in the list by its ID.
    Returns the index (int) or -1 if not found.
    """
    for index, item in enumerate(data_structure):
        if item['id'] == item_id:
            return index
    return -1

# --- CRUD Operations Functions (lower_snake_case) ---

def create_item(data_structure, item_id, name, price_str, quantity_str):
    """
    Adds a new item to the inventory after validating all inputs.
    Returns True on success, False otherwise.
    """
    item_id = item_id.strip()
    name = name.strip()

    # 1. Validate ID
    if not item_id:
        print("Error: invalid input (ID cannot be empty)")
        return False
    
    # 2. Check for ID duplication
    if get_item_index(data_structure, item_id) != -1:
        print("Error: ID already exists")
        return False

    # 3. Validate Price
    is_price_valid, price_value = is_valid_numeric_field(price_str, "price")
    if not is_price_valid:
        print(f"Error: invalid input ({price_value})")
        return False

    # 4. Validate Quantity
    is_quantity_valid, quantity_value = is_valid_numeric_field(quantity_str, "quantity")
    if not is_quantity_valid:
        print(f"Error: invalid input ({quantity_value})")
        return False

    # 5. Create the item
    new_item = {
        "id": item_id,
        "name": name,
        "price": price_value,
        "quantity": quantity_value
    }
    data_structure.append(new_item)
    print("Item created")
    return True

def read_item(data_structure, item_id):
    """
    Retrieves a single item by its ID and prints its details.
    """
    item_id = item_id.strip()
    if not item_id:
        print("Error: invalid input (ID cannot be empty)")
        return None

    index = get_item_index(data_structure, item_id)
    if index != -1:
        item = data_structure[index]
        print("\n--- Item Found ---")
        print(f"ID: {item['id']}")
        print(f"Name: {item['name']}")
        print(f"Price: ${item['price']:.2f}")
        print(f"Quantity: {item['quantity']}")
        print("------------------\n")
        return item
    else:
        print("Item not found")
        return None

def update_item(data_structure, item_id, new_name, new_price_str, new_quantity_str):
    """
    Updates an existing item's details after validating inputs.
    Returns True on success, False otherwise.
    """
    item_id = item_id.strip()
    new_name = new_name.strip()
    
    # 1. Validate ID existence
    if not item_id:
        print("Error: invalid input (ID cannot be empty)")
        return False
        
    index = get_item_index(data_structure, item_id)
    if index == -1:
        print("Item not found")
        return False

    # 2. Validate Price
    is_price_valid, price_value = is_valid_numeric_field(new_price_str, "price")
    if not is_price_valid:
        print(f"Error: invalid input ({price_value})")
        return False

    # 3. Validate Quantity
    is_quantity_valid, quantity_value = is_valid_numeric_field(new_quantity_str, "quantity")
    if not is_quantity_valid:
        print(f"Error: invalid input ({quantity_value})")
        return False

    # 4. Update the item
    data_structure[index]['name'] = new_name
    data_structure[index]['price'] = price_value
    data_structure[index]['quantity'] = quantity_value
    print("Item updated")
    return True

def delete_item(data_structure, item_id):
    """
    Removes an item from the inventory by its ID.
    Returns True on success, False otherwise.
    """
    item_id = item_id.strip()
    
    # 1. Validate ID
    if not item_id:
        print("Error: invalid input (ID cannot be empty)")
        return False

    # 2. Check for ID existence and delete
    index = get_item_index(data_structure, item_id)
    if index != -1:
        del data_structure[index]
        print("Item deleted")
        return True
    else:
        print("Item not found")
        return False

def list_items(data_structure):
    """
    Prints all items in the inventory in a readable format.
    """
    print("\n--- Items list: ---")
    if not data_structure:
        print("The inventory is empty.")
    else:
        # Print header
        print(f"{'ID':<10}{'Name':<20}{'Price':>10}{'Quantity':>10}")
        print("-" * 50)
        for item in data_structure:
            print(f"{item['id']:<10}{item['name']:<20}{item['price']:>10.2f}{item['quantity']:>10}")
    print("-------------------\n")

# --- Main Program Loop ---

def display_menu():
    """
    Prints the main menu options to the console.
    """
    print("\n--- Inventory CRUD Manager ---")
    print("1) Create item")
    print("2) Read item by id")
    print("3) Update item by id")
    print("4) Delete item by id")
    print("5) List all items")
    print(f"{EXIT_OPTION}) Exit")
    print("------------------------------")

def main_loop():
    """
    Main function to handle user interaction and delegate to CRUD functions.
    """
    while True:
        display_menu()
        
        option = input("Select an option: ").strip()

        if option == '1': # CREATE
            print("\n--- Create Item ---")
            item_id = input("Enter Item ID: ")
            name = input("Enter Item Name: ")
            price = input("Enter Item Price (e.g., 10.99): ")
            quantity = input("Enter Item Quantity (e.g., 50): ")
            create_item(inventory_data, item_id, name, price, quantity)
        
        elif option == '2': # READ
            print("\n--- Read Item ---")
            item_id = input("Enter Item ID to Read: ")
            read_item(inventory_data, item_id)
            
        elif option == '3': # UPDATE
            print("\n--- Update Item ---")
            item_id = input("Enter Item ID to Update: ")
            new_name = input("Enter NEW Item Name: ")
            new_price = input("Enter NEW Item Price (e.g., 10.99): ")
            new_quantity = input("Enter NEW Item Quantity (e.g., 50): ")
            update_item(inventory_data, item_id, new_name, new_price, new_quantity)

        elif option == '4': # DELETE
            print("\n--- Delete Item ---")
            item_id = input("Enter Item ID to Delete: ")
            delete_item(inventory_data, item_id)

        elif option == '5': # LIST ALL
            list_items(inventory_data)
            
        elif option == EXIT_OPTION: # EXIT
            print("Exiting program. Goodbye!")
            break
            
        else:
            print("Error: invalid input (Select an option from the menu: 0-5)")

if __name__ == "__main__":
    # Initialize with some test data (optional, for quick testing)
    # create_item(inventory_data, "P101", "Keyboard", "50.00", "20")
    # create_item(inventory_data, "P102", "Mouse", "25.50", "15")
    main_loop()

# ----------------------------------------------------------------------
# 7. CONCLUSIONES (COMENTARIOS AL FINAL)
# ----------------------------------------------------------------------

# Conclusiones:
# El uso de funciones (create_item, read_item, etc.) simplificó enormemente la implementación
# del CRUD al forzar la **modularidad**. Cada función se encarga de una única responsabilidad,
# lo que hace que el bucle principal sea limpio y legible, actuando solo como un **delegador**
# de tareas. La lista de diccionarios (Opción B) fue una opción excelente, ya que modela
# intuitivamente la estructura de registros de una tabla de inventario.
# El principal desafío fue la **validación de entradas**, especialmente el manejo de errores
# de conversión de tipos (string a float/int) y el asegurar los rangos válidos (> 0).
# Solucioné esto usando bloques `try-except` y una función auxiliar `is_valid_numeric_field`
# para centralizar la lógica de validación, asegurando que todos los datos fueran correctos
# antes de modificar la estructura principal.
# Para extender este CRUD a un sistema más grande, la primera mejora sería guardar los datos
# en un archivo (como JSON o CSV) al salir y cargarlos al iniciar, o migrar a una base de
# datos relacional como SQLite, manteniendo la lógica CRUD en las funciones, pero modificando
# la forma en que interactúan con la capa de persistencia (archivo/DB).

# ----------------------------------------------------------------------
# 8. REFERENCIAS (MÍNIMO 3) – EN COMENTARIOS
# ----------------------------------------------------------------------

# References:
# 1) Python documentation – Data structures (list and dict):
#    https://docs.python.org/3/tutorial/datastructures.html
# 2) Python documentation – Defining functions:
#    https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# 3) GeeksforGeeks – Python CRUD Operations in List of Dictionaries:
#    https://www.geeksforgeeks.org/python-crud-operations-in-list-of-dictionaries/