# Portada
# name:Victor Escobar Carrizales
# Matricula: 2530325
# Group: A

# Executive Summary:
# This file contains six Python problems that exercise list, tuple and dictionary
# data structures. A list is an ordered, mutable collection; a tuple is an ordered,
# immutable collection; a dictionary stores key-value pairs for fast lookup by key.
# Mutability means that a list's contents can be changed (append, remove), while a
# tuple cannot be modified after creation. Dictionaries associate keys (e.g., names)
# with values (e.g., prices) and support methods like get(), keys(), items().
# The document includes problem descriptions, input/output design, validations,
# and three test cases (normal, border, error) per problem. It demonstrates
# practical uses: shopping lists, geometric points, product catalogs, grade
# management, word frequency, and a simple contact book.

# Principles and Best Practices (short):
# - Use lists when you need to add/remove items frequently.
# - Use tuples for fixed records (coordinates, dates).
# - Use dicts for fast lookup by key (id, name).
# - Avoid modifying a list while iterating over it unless intentional.
# - Use descriptive keys like "name", "price" in dicts.
# - Write readable code and clear messages.

# -----------------------------------------------------------------------------
# Problem 1: Shopping list basics
# Description: Manage a shopping list using list operations.
# Inputs:
# - initial_items_text (string, comma-separated, e.g. "apple,banana,orange")
# - new_item (string)
# - search_item (string)
# Outputs:
# - "Items list:" <items_list>
# - "Total items:" <len_list>
# - "Found item:" true|false
# Validations:
# - initial_items_text must not be empty after strip()
# - new_item and search_item must not be empty
# Test cases:
# 1) Normal: "apple, banana, orange" + add "pear" + search "banana"
# 2) Border: "   " (empty initial) + add "apple" + search "apple"
# 3) Error: initial="apple,banana" + add "" (empty new_item) -> error

def problem1_shopping_list(initial_items_text, new_item, search_item):
    # Validations
    if not isinstance(initial_items_text, str):
        print("Error: invalid input")
        return
    initial_strip = initial_items_text.strip()
    if initial_strip == "":
        # Decide: treat as empty initial list
        items_list = []
    else:
        # split and strip elements
        items_list = [item.strip() for item in initial_strip.split(',') if item.strip() != ""]

    if not isinstance(new_item, str) or new_item.strip() == "":
        print("Error: invalid input")
        return
    if not isinstance(search_item, str) or search_item.strip() == "":
        print("Error: invalid input")
        return

    # Add new item
    items_list.append(new_item.strip())

    # Outputs
    print("Items list:", items_list)
    print("Total items:", len(items_list))
    found = search_item.strip() in items_list
    print("Found item:", str(found).lower())

# -----------------------------------------------------------------------------
# Problem 2: Points and distances with tuples
# Description: Represent two 2D points as tuples, compute Euclidean distance and midpoint.
# Inputs: x1, y1, x2, y2 (floats)
# Outputs:
# - "Point A:" (x1, y1)
# - "Point B:" (x2, y2)
# - "Distance:" <distance>
# - "Midpoint:" (mx, my)
# Validations:
# - All inputs convertible to float
# Test cases:
# 1) Normal: (0,0) and (3,4) -> distance 5.0 midpoint (1.5,2.0)
# 2) Border: same point (1,1) and (1,1) -> distance 0 midpoint (1,1)
# 3) Error: non-numeric input

def problem2_points_distance(x1, y1, x2, y2):
    try:
        fx1 = float(x1)
        fy1 = float(y1)
        fx2 = float(x2)
        fy2 = float(y2)
    except Exception:
        print("Error: invalid input")
        return

    point_a = (fx1, fy1)
    point_b = (fx2, fy2)
    distance = ((fx2 - fx1) ** 2 + (fy2 - fy1) ** 2) ** 0.5
    midpoint = ((fx1 + fx2) / 2.0, (fy1 + fy2) / 2.0)

    print("Point A:", point_a)
    print("Point B:", point_b)
    # round distance to 6 decimals for display
    print("Distance:", round(distance, 6))
    print("Midpoint:", (round(midpoint[0], 6), round(midpoint[1], 6)))

# -----------------------------------------------------------------------------
# Problem 3: Product catalog with dictionary
# Description: Manage a product-price dictionary and compute totals.
# Inputs: product_name (string), quantity (int)
# Outputs:
# - If exists: "Unit price:" <unit_price> \n "Quantity:" <quantity> \n "Total:" <total_price>
# - If not: "Error: product not found"
# Validations:
# - quantity > 0
# - product_name not empty
# Test cases:
# 1) Normal: product exists, e.g., "apple", quantity 3
# 2) Border: quantity 1
# 3) Error: product does not exist

def problem3_product_catalog(product_name, quantity):
    # sample initial catalog
    product_prices = {
        "apple": 10.0,
        "banana": 5.5,
        "orange": 8.25
    }

    if not isinstance(product_name, str) or product_name.strip() == "":
        print("Error: invalid input")
        return
    try:
        q = int(quantity)
    except Exception:
        print("Error: invalid input")
        return
    if q <= 0:
        print("Error: invalid input")
        return

    key = product_name.strip()
    if key in product_prices:
        unit_price = product_prices[key]
        total_price = round(unit_price * q, 2)
        print("Unit price:", unit_price)
        print("Quantity:", q)
        print("Total:", total_price)
    else:
        print("Error: product not found")

# -----------------------------------------------------------------------------
# Problem 4: Student grades with dict and list
# Description: Store students and their grades, compute average and pass status.
# Inputs: student_name (string)
# Outputs:
# - If exists: "Grades:" <grades_list> \n "Average:" <average> \n "Passed:" true|false
# - If not: "Error: student not found"
# Validations:
# - student_name not empty
# - grades list not empty
# Test cases:
# 1) Normal: student exists with grades [90,80,70]
# 2) Border: student with one grade 70
# 3) Error: student not found

def problem4_student_grades(student_name):
    grades_dict = {
        "Alice": [90.0, 85.0, 78.5],
        "Bob": [60.0, 70.0, 65.0],
        "Charlie": [100.0]
    }

    if not isinstance(student_name, str) or student_name.strip() == "":
        print("Error: invalid input")
        return
    key = student_name.strip()
    if key not in grades_dict:
        print("Error: student not found")
        return
    grades_list = grades_dict[key]
    if not grades_list:
        print("Error: invalid input")
        return
    average = sum(grades_list) / len(grades_list)
    passed = average >= 70.0
    # Format outputs
    print("Grades:", grades_list)
    print("Average:", round(average, 2))
    print("Passed:", str(passed).lower())

# -----------------------------------------------------------------------------
# Problem 5: Word frequency counter (list + dict)
# Description: Count word frequencies in a sentence.
# Inputs: sentence (string)
# Outputs:
# - "Words list:" <words_list>
# - "Frequencies:" <freq_dict>
# - "Most common word:" <word>
# Validations:
# - sentence not empty after strip()
# - handle punctuation optionally (here we remove common punctuation)
# Test cases:
# 1) Normal: "Apple apple banana"
# 2) Border: single word
# 3) Error: empty string

def problem5_word_frequency(sentence):
    if not isinstance(sentence, str):
        print("Error: invalid input")
        return
    s = sentence.strip()
    if s == "":
        print("Error: invalid input")
        return

    # simple punctuation removal (documented decision)
    for ch in ['.', ',', '!', '?', ';', ':', '"', "'", "(", ")"]:
        s = s.replace(ch, '')

    s = s.lower()
    words_list = [w for w in s.split() if w != ""]
    if not words_list:
        print("Error: invalid input")
        return

    freq_dict = {}
    for w in words_list:
        if w in freq_dict:
            freq_dict[w] += 1
        else:
            freq_dict[w] = 1

    # Find most common word (any in tie)
    most_common_word = None
    max_count = -1
    for k, v in freq_dict.items():
        if v > max_count:
            max_count = v
            most_common_word = k

    print("Words list:", words_list)
    print("Frequencies:", freq_dict)
    print("Most common word:", most_common_word)

# -----------------------------------------------------------------------------
# Problem 6: Simple contact book (dictionary CRUD)
# Description: Simple contact book supporting ADD, SEARCH, DELETE actions.
# Inputs:
# - action_text (string: "ADD", "SEARCH", "DELETE")
# - name (string)
# - phone (string for ADD)
# Outputs per action as specified in problem description
# Validations:
# - action_text normalized to upper and validated
# - name not empty
# - for ADD: phone not empty
# Test cases:
# 1) Normal: ADD new contact, SEARCH it, DELETE it
# 2) Border: ADD with existing name (updates)
# 3) Error: SEARCH non-existing

def problem6_contact_book(action_text, name, phone=None):
    # initial contacts
    contacts = {
        "Alice": "1234567890",
        "Bob": "0987654321"
    }

    if not isinstance(action_text, str):
        print("Error: invalid input")
        return
    action = action_text.strip().upper()
    if action not in ("ADD", "SEARCH", "DELETE"):
        print("Error: invalid input")
        return
    if not isinstance(name, str) or name.strip() == "":
        print("Error: invalid input")
        return
    key = name.strip()

    if action == "ADD":
        if not isinstance(phone, str) or phone.strip() == "":
            print("Error: invalid input")
            return
        contacts[key] = phone.strip()
        print("Contact saved:", key + ",", contacts[key])
        return

    if action == "SEARCH":
        if key in contacts:
            print("Phone:", contacts[key])
        else:
            print("Error: contact not found")
        return

    if action == "DELETE":
        if key in contacts:
            contacts.pop(key)
            print("Contact deleted:", key)
        else:
            print("Error: contact not found")
        return

# -----------------------------------------------------------------------------
# Conclusions (comments):
# - Use lists when you need mutability and ordered sequences (e.g., shopping items).
# - Use tuples for fixed records (coordinates) because they protect data from accidental changes.
# - Use dictionaries for fast lookups and to map keys to values (catalogs, contact books).
# - Combining structures is common: dicts of lists to store students and their grades.
# - When designing programs, validate inputs, handle empty collections, and present clear messages.

# References (minimum 5):
# 1) Python documentation - Built-in Types: list, tuple, dict
# 2) "Automate the Boring Stuff with Python" - Al Sweigart (chapters on data structures)
# 3) "Think Python" - Allen B. Downey (data structures)
# 4) Real Python articles on lists, tuples and dictionaries
# 5) Official Python tutorial: Data Structures

# -----------------------------------------------------------------------------
# Quick test runner with the specified test cases (prints separators)
"""

https://youtu.be/CCUNuqqn7PQ?si=HltURE4xKIDyQjm9
https://youtu.be/9k91jETchkI?si=3jr1oLLRh44mghYe
https://youtu.be/Pr-9wkSJDJk?si=ekXXTMe1kblZUbZ_
https://youtu.be/OvafT2HL0uU?si=tbUWDtTrdG60q3xk
https://youtu.be/WSQvaPHsm64?si=EJurIIuAx-bDLgl5
https://youtu.be/tb6EYiHtcXU?si=pJIBO9-hqXKYw0_l
"""