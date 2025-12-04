# 2530325_CortexUpv.py
# Portada
# Student: Cortex Upv
# Matricula: 2530325
# Group: A

# Executive Summary:
# This file contains six programming problems focused on loops in Python (for and while).
# A for loop is used when the number of iterations is known or when iterating over a sequence.
# A while loop runs while a condition holds and is ideal for sentinels and repeated input until
# a termination condition. Counters (e.g., count += 1) and accumulators (e.g., total += value)
# are used to aggregate results across iterations. The document explains inputs/outputs,
# validations, and includes three test cases (normal, border, error) for each problem.

# Principles and Best Practices (short):
# - Use for when you know the number of iterations (range or sequence).
# - Use while when the end depends on a condition or sentinel.
# - Initialize counters and accumulators before the loop.
# - Update loop-control variables inside while to avoid infinite loops.
# - Keep loop bodies simple and extract complex logic to functions.

# -----------------------------------------------------------------------------
# Problem 1: Sum of range with for
# Description: Sum integers from 1 to n inclusive and sum only even numbers in that range.
# Inputs:
# - n (int)
# Outputs:
# - "Sum 1..n:" <total_sum>
# - "Even sum 1..n:" <even_sum>
# Validations:
# - n convertible to int and n >= 1
# Test cases:
# 1) Normal: n=10 -> Sum 55, Even sum 30
# 2) Border: n=1 -> Sum 1, Even sum 0
# 3) Error: n=0 -> Error: invalid input

def problem1_sum_range(n):
    try:
        n_int = int(n)
    except Exception:
        print("Error: invalid input")
        return
    if n_int < 1:
        print("Error: invalid input")
        return
    total_sum = 0
    even_sum = 0
    for i in range(1, n_int + 1):
        total_sum += i
        if i % 2 == 0:
            even_sum += i
    print("Sum 1..n:", total_sum)
    print("Even sum 1..n:", even_sum)

# -----------------------------------------------------------------------------
# Problem 2: Multiplication table with for
# Description: Print multiplication table for base from 1 to m.
# Inputs: base (int), m (int)
# Outputs: lines like "5 x 1 = 5"
# Validations: base and m convertible to int, m >= 1
# Test cases:
# 1) Normal: base=5, m=4
# 2) Border: m=1
# 3) Error: m=0 -> Error: invalid input

def problem2_multiplication_table(base, m):
    try:
        base_int = int(base)
        m_int = int(m)
    except Exception:
        print("Error: invalid input")
        return
    if m_int < 1:
        print("Error: invalid input")
        return
    for i in range(1, m_int + 1):
        product = base_int * i
        print(f"{base_int} x {i} = {product}")

# -----------------------------------------------------------------------------
# Problem 3: Average of numbers with while and sentinel
# Description: Read numbers until sentinel (-1). Compute count and average.
# Inputs: sequence of numbers (list provided to function), sentinel fixed -1
# Outputs: "Count:" <count> "Average:" <average> or "Error: no data"
# Validations: convertible to float, ignore sentinel
# Test cases:
# 1) Normal: [1,2,3,-1] -> Count 3 Average 2.0
# 2) Border: [-1] -> Error: no data
# 3) Error: ['a', -1] -> Error: invalid input

def problem3_average_sentinel(inputs):
    # inputs: iterable of values to simulate repeated reads
    SENTINEL_VALUE = -1
    total = 0.0
    count = 0
    idx = 0
    while True:
        if idx >= len(inputs):
            # no more inputs provided
            break
        val = inputs[idx]
        idx += 1
        try:
            fval = float(val)
        except Exception:
            print("Error: invalid input")
            return
        if fval == SENTINEL_VALUE:
            break
        total += fval
        count += 1
    if count == 0:
        print("Error: no data")
    else:
        average = total / count
        print("Count:", count)
        print("Average:", round(average, 6))

# -----------------------------------------------------------------------------
# Problem 4: Password attempts with while
# Description: Allow up to MAX_ATTEMPTS attempts to enter the correct password.
# Inputs: attempts_list (list of candidate passwords to simulate user input)
# Outputs: "Login success" or "Account locked"
# Validations: MAX_ATTEMPTS > 0
# Test cases:
# 1) Normal: attempts include correct within limit
# 2) Border: correct on last attempt
# 3) Error: no attempts or invalid types -> Account locked or Error

def problem4_password_attempts(attempts_list):
    CORRECT_PASSWORD = "admin123"
    MAX_ATTEMPTS = 3
    if MAX_ATTEMPTS <= 0:
        print("Error: invalid input")
        return
    attempts = 0
    idx = 0
    while attempts < MAX_ATTEMPTS:
        if idx >= len(attempts_list):
            # no more simulated inputs
            break
        user_password = attempts_list[idx]
        idx += 1
        attempts += 1
        if not isinstance(user_password, str):
            print("Error: invalid input")
            return
        if user_password == CORRECT_PASSWORD:
            print("Login success")
            return
    # if loop finishes without return
    print("Account locked")

# -----------------------------------------------------------------------------
# Problem 5: Simple menu with while
# Description: Text menu that repeats until user selects 0. Simulates inputs via list.
# Inputs: options_list (list of option values as strings or ints)
# Outputs: messages per option; "Bye!" when exiting
# Validations: option convertible to int and in {0,1,2,3}
# Test cases:
# 1) Normal: ["1","3","2","0"] -> shows greeting, increments, shows counter, exits
# 2) Border: ["0"] -> exits immediately
# 3) Error: ["9","0"] -> invalid option message then exit

def problem5_simple_menu(options_list):
    counter = 0
    idx = 0
    while True:
        # get next option from list; if none, exit loop
        if idx >= len(options_list):
            print("Bye!")
            break
        opt_raw = options_list[idx]
        idx += 1
        try:
            option = int(opt_raw)
        except Exception:
            print("Error: invalid option")
            continue
        if option == 0:
            print("Bye!")
            break
        elif option == 1:
            print("Hello!")
        elif option == 2:
            print("Counter:", counter)
        elif option == 3:
            counter += 1
            print("Counter incremented")
        else:
            print("Error: invalid option")

# -----------------------------------------------------------------------------
# Problem 6: Pattern printing with nested loops
# Description: Print a right triangle of asterisks with n rows. Optionally print inverted.
# Inputs: n (int)
# Outputs: lines with increasing asterisks
# Validations: n convertible to int and n >= 1
# Test cases:
# 1) Normal: n=4 -> prints 1..4 stars
# 2) Border: n=1 -> prints one star
# 3) Error: n=0 -> Error: invalid input

def problem6_pattern_printing(n, print_inverted=False):
    try:
        n_int = int(n)
    except Exception:
        print("Error: invalid input")
        return
    if n_int < 1:
        print("Error: invalid input")
        return
    for i in range(1, n_int + 1):
        print("*" * i)
    if print_inverted:
        for i in range(n_int, 0, -1):
            print("*" * i)

# -----------------------------------------------------------------------------
# Conclusions (comments):
# - For loops are ideal when the number of iterations is known or when iterating over sequences.
# - While loops are useful for input-driven repetition (sentinels, menus, retries) but require
#   careful loop-control to avoid infinite loops.
# - Counters and accumulators helped compute counts and aggregates in all examples.
# - Nested loops are a natural pattern for 2D output like patterns or tables.
# - Validations and clear messages prevent unexpected behavior and improve user experience.

# References (minimum 5):
# 1) Python documentation - for and while statements
# 2) "Automate the Boring Stuff with Python" - loops chapter
# 3) Real Python tutorials on loops and iterators
# 4) "Think Python" - control flow and loops
# 5) Official Python tutorial: control flow tools

# -----------------------------------------------------------------------------
"""

https://youtu.be/CCUNuqqn7PQ?si=HltURE4xKIDyQjm9
https://youtu.be/9k91jETchkI?si=3jr1oLLRh44mghYe
https://youtu.be/Pr-9wkSJDJk?si=ekXXTMe1kblZUbZ_
https://youtu.be/OvafT2HL0uU?si=tbUWDtTrdG60q3xk
https://youtu.be/WSQvaPHsm64?si=EJurIIuAx-bDLgl5
https://youtu.be/tb6EYiHtcXU?si=pJIBO9-hqXKYw0_l

"""