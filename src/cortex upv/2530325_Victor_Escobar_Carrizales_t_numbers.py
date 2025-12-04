# PORTADA
# ================================================================
# Name: Escobar Carrizales Victor
# Matriculation: 2530325
# Group: 103
#
# Numerical Types and Booleans – Practice Exercises
# ================================================================


# ================================================================
# EXECUTIVE SUMMARY
# ================================================================
# In Python, integers (int) represent whole numbers and floats 
# represent decimal values, both essential for mathematical 
# operations. Boolean values (True/False) are often produced from 
# comparisons and logical expressions, allowing decision-making 
# through conditional statements. Validating input ranges and 
# preventing division by zero ensures safe and reliable programs. 
# This document covers six problems involving integers, floats, 
# booleans, comparisons, casting, and logical operators. Each 
# section includes descriptions, inputs, outputs, validations, 
# and test cases.
# ================================================================


# ================================================================
# PRINCIPLES AND BEST PRACTICES
# ================================================================
# - Use int for counters and float for decimal quantities.
# - Store repeated expressions in variables to avoid redundancy.
# - Validate user inputs before performing operations.
# - Use descriptive variable names in lower_snake_case.
# - Clearly document what True and False represent in each context.
# ================================================================



# ================================================================
# 7.1 PROBLEM 1: Temperature converter and range flag
# ================================================================
# Description:
# Convert Celsius temperature to Fahrenheit and Kelvin. Determine
# if the temperature is considered high (>= 30°C).
#
# Inputs:
# - temp_c (float)
#
# Outputs:
# - Fahrenheit
# - Kelvin
# - High temperature flag
#
# Validations:
# - Must be convertible to float
# - Kelvin temperature must not be negative
#
# Test cases:
# 1) Normal: temp_c = 25   → High temperature: false
# 2) Border: temp_c = 30   → High temperature: true
# 3) Error: temp_c = -300  → Kelvin < 0 → invalid
# ================================================================
"""
temp_c_text = input("Enter temperature in Celsius: ").strip()

try:
    temp_c = float(temp_c_text)
    temp_k = temp_c + 273.15

    if temp_k < 0:
        print("Error: invalid temperature (Kelvin < 0)")
    else:
        temp_f = temp_c * 9 / 5 + 32
        is_high_temperature = (temp_c >= 30.0)

        print("Fahrenheit:", temp_f)
        print("Kelvin:", temp_k)
        print("High temperature:", str(is_high_temperature).lower())

except:
    print("Error: invalid input")

"""

# ================================================================
# 7.2 PROBLEM 2: Work hours and overtime payment
# ================================================================
# Description:
# Compute weekly payment with overtime at 150% of hourly rate.
#
# Inputs:
# - hours_worked (float)
# - hourly_rate (float)
#
# Outputs:
# - Regular pay
# - Overtime pay
# - Total pay
# - Has overtime flag
#
# Validations:
# - hours_worked >= 0
# - hourly_rate > 0
#
# Test cases:
# 1) Normal: hours=38, rate=100 → no overtime
# 2) Border: hours=40 → no overtime
# 3) Error: hours=-1 or rate=0 → invalid
# ================================================================
"""
hours_text = input("Enter hours worked: ").strip()
rate_text = input("Enter hourly rate: ").strip()

try:
    hours_worked = float(hours_text)
    hourly_rate = float(rate_text)

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
    else:
        regular_hours = min(40, hours_worked)
        overtime_hours = max(0, hours_worked - 40)

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay

        has_overtime = (hours_worked > 40)

        print("Regular pay:", regular_pay)
        print("Overtime pay:", overtime_pay)
        print("Total pay:", total_pay)
        print("Has overtime:", str(has_overtime).lower())

except:
    print("Error: invalid input")

"""

# ================================================================
# 7.3 PROBLEM 3: Discount eligibility with booleans
# ================================================================
# Description:
# Determine if a client is eligible for a discount based on:
# - student
# - senior
# - purchase >= 1000
#
# Inputs:
# - purchase_total (float)
# - is_student_text (YES/NO)
# - is_senior_text (YES/NO)
#
# Outputs:
# - Discount eligible
# - Final total
#
# Validations:
# - purchase_total >= 0
# - Student/senior must be YES or NO
#
# Test cases:
# 1) Normal: total=1200, NO, NO → true
# 2) Border: total=1000 → true
# 3) Error: invalid text → invalid input
# ================================================================
"""
purchase_text = input("Enter purchase total: ").strip()
student_text = input("Is student? (YES/NO): ").strip().upper()
senior_text = input("Is senior? (YES/NO): ").strip().upper()

try:
    purchase_total = float(purchase_text)

    if purchase_total < 0:
        print("Error: invalid input")
    elif student_text not in ("YES", "NO") or senior_text not in ("YES", "NO"):
        print("Error: invalid input")
    else:
        is_student = (student_text == "YES")
        is_senior = (senior_text == "YES")

        discount_eligible = (
            is_student or is_senior or purchase_total >= 1000.0
        )

        if discount_eligible:
            final_total = purchase_total * 0.9
        else:
            final_total = purchase_total

        print("Discount eligible:", str(discount_eligible).lower())
        print("Final total:", final_total)

except:
    print("Error: invalid input")

"""

# ================================================================
# 7.4 PROBLEM 4: Basic statistics of three integers
# ================================================================
# Description:
# Read three integers and compute: sum, average, max, min, and
# a boolean indicating if all numbers are even.
#
# Inputs:
# - n1, n2, n3 (int)
#
# Outputs:
# - Sum
# - Average
# - Max
# - Min
# - All even flag
#
# Validations:
# - Must be convertible to int
#
# Test cases:
# 1) Normal: 3,6,9 → all_even: false
# 2) Border: 2,4,6 → all_even: true
# 3) Error: text input
# ================================================================
"""
try:
    n1 = int(input("Enter integer 1: "))
    n2 = int(input("Enter integer 2: "))
    n3 = int(input("Enter integer 3: "))

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print("Sum:", sum_value)
    print("Average:", average_value)
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", str(all_even).lower())

except:
    print("Error: invalid input")

"""

# ================================================================
# 7.5 PROBLEM 5: Loan eligibility
# ================================================================
# Description:
# Determine loan eligibility based on income, debt ratio and 
# credit score.
#
# Inputs:
# - monthly_income (float)
# - monthly_debt (float)
# - credit_score (int)
#
# Outputs:
# - Debt ratio
# - Eligible flag
#
# Validations:
# - monthly_income > 0
# - monthly_debt >= 0
# - credit_score >= 0
#
# Test cases:
# 1) Normal: 10000, 2000, 700 → eligible
# 2) Border: 8000, 3200, 650 → eligible
# 3) Error: income = 0 → invalid input
# ================================================================
"""
income_text = input("Enter monthly income: ").strip()
debt_text = input("Enter monthly debt: ").strip()
score_text = input("Enter credit score: ").strip()

try:
    monthly_income = float(income_text)
    monthly_debt = float(debt_text)
    credit_score = int(score_text)

    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income
        eligible = (
            monthly_income >= 8000.0 and
            debt_ratio <= 0.4 and
            credit_score >= 650
        )

        print("Debt ratio:", debt_ratio)
        print("Eligible:", str(eligible).lower())

except:
    print("Error: invalid input")

"""

# ================================================================
# 7.6 PROBLEM 6: BMI and category flag
# ================================================================
# Description:
# Compute BMI and determine category flags.
#
# Inputs:
# - weight_kg (float)
# - height_m (float)
#
# Outputs:
# - BMI (rounded)
# - Underweight, Normal, Overweight flags
#
# Validations:
# - weight_kg > 0
# - height_m > 0
#
# Test cases:
# 1) Normal: 70, 1.75 → normal
# 2) Border: 90, 1.70 → overweight
# 3) Error: height = 0 → invalid
# ================================================================
"""
weight_text = input("Enter weight (kg): ").strip()
height_text = input("Enter height (m): ").strip()

try:
    weight_kg = float(weight_text)
    height_m = float(height_text)

    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m ** 2)
        bmi_rounded = round(bmi, 2)

        is_underweight = (bmi < 18.5)
        is_normal = (18.5 <= bmi < 25.0)
        is_overweight = (bmi >= 25.0)

        print("BMI:", bmi_rounded)
        print("Underweight:", str(is_underweight).lower())
        print("Normal:", str(is_normal).lower())
        print("Overweight:", str(is_overweight).lower())

except:
    print("Error: invalid input")

"""

# ================================================================
# CONCLUSIONS
# ================================================================
# Integers and floats work together to solve real-world problems
# such as payroll, loans, and health calculations. Comparisons 
# produce boolean values that drive decisions in if-statements. 
# Proper validation prevents errors like negative values or 
# division by zero. Logical operators (and, or, not) help build 
# complex conditions. These patterns are common across many 
# applications such as discounts, overtime, and BMI evaluation.
# ================================================================


# ================================================================
# REFERENCES
# ================================================================
# 1) Python documentation - Numeric Types
# 2) Python documentation - Boolean Type
# 3) W3Schools - Python Operators
# 4) RealPython - Data Types in Python
# 5) Apuntes de clase – Validación de datos numéricos
# ================================================================


# ================================================================
# GITHUB REPOSITORY
# ================================================================
# URL: _______________________________________________
# ================================================================


# ================================================================
# CHECKLIST
# ================================================================
# [ ] File name follows format
# [ ] Includes: cover, summary, problems, conclusions, references
# [ ] Variables in English
# [ ] Includes validations
# [ ] Includes test cases
# [ ] Tested with real inputs
# [ ] Repository added
# ================================================================
""""

https://youtu.be/CCUNuqqn7PQ?si=HltURE4xKIDyQjm9
https://youtu.be/9k91jETchkI?si=3jr1oLLRh44mghYe
https://youtu.be/Pr-9wkSJDJk?si=ekXXTMe1kblZUbZ_
https://youtu.be/OvafT2HL0uU?si=tbUWDtTrdG60q3xk
https://youtu.be/WSQvaPHsm64?si=EJurIIuAx-bDLgl5
https://youtu.be/tb6EYiHtcXU?si=pJIBO9-hqXKYw0_l

"""