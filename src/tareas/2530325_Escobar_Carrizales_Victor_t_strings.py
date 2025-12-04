# File name (rename before submitting): 0000000_Victor_t_strings.py
#
# Portada:
# Name: Victor Placeholder
# Matricula: 0000000
# Group: GroupPlaceholder
#
# Executive Summary:
# This file implements six string-processing problems in Python aimed at real-world
# input/output validation and formatting. A Python string is an immutable sequence of
# Unicode characters. Typical operations used here include trimming (strip), casing
# (lower/upper/title), splitting/joining, slicing, searching and replacing. Input
# normalization and validation are crucial to avoid garbage data and unexpected behavior.
# Each problem includes Description, Inputs, Outputs, Validations and three concrete test
# cases (normal, border, error). Code follows naming conventions and prints clear English messages.
#
# Principles and Good Practices (short):
# - Strings are immutable: operations produce new strings.
# - Normalize inputs with strip() and lower()/title() where appropriate.
# - Avoid magic numbers — use named constants for index/length limits.
# - Validate input layers: non-empty -> format -> content-specific checks.
# - Use built-in string methods rather than reimplementing them.
#
# ------------------------------------------------------------------------------

# Constants
MIN_NAME_WORDS = 2
MIN_PALINDROME_CHARS = 3
LABEL_FIXED_LENGTH = 30

# ----------------------------
# Problem 1: Full name formatter (name + initials)
# Description:
# Given a single-string full name (e.g., "juan carlos tovar"), normalize spacing and case,
# return Title Case full name and initials like "J.C.T.".
#
# Inputs:
# - full_name (string)
#
# Outputs:
# - "Formatted name: <Name In Title Case>"
# - "Initials: <X.X.X.>"
#
# Validations:
# - full_name not empty after strip()
# - must contain at least two words
#
# Test cases:
# 1) Normal: "  juan   carlos tovar  " -> "Formatted name: Juan Carlos Tovar" ; "Initials: J.C.T."
# 2) Border: "Ana Maria" -> "Formatted name: Ana Maria" ; "Initials: A.M."
# 3) Error: "   " -> Error: invalid input
# ----------------------------
def format_name_and_initials(full_name: str) -> tuple:
    if full_name is None:
        raise ValueError("Error: invalid input (none provided)")

    cleaned = full_name.strip()
    if not cleaned:
        raise ValueError("Error: invalid input (empty string)")

    parts = [p for p in cleaned.split() if p]
    if len(parts) < MIN_NAME_WORDS:
        raise ValueError("Error: invalid input (must contain at least two words)")

    formatted_name = " ".join(parts).title()

    initials = ".".join([p[0].upper() for p in parts]) + "."
    return formatted_name, initials


# ----------------------------
# Problem 2: Simple email validator (structure + domain)
# Description:
# Validate basic email structure and extract domain.
#
# Inputs:
# - email_text (string)
#
# Outputs:
# - "Valid email: true" or "Valid email: false"
# - If valid: "Domain: <domain_part>"
#
# Validations:
# - email_text not empty after strip()
# - exactly one '@'
# - no spaces
# - domain contains at least one '.'
#
# Test cases:
# 1) Normal: "User@example.com" -> Valid true, Domain: example.com
# 2) Border: "a@b.c" -> Valid true, Domain: b.c
# 3) Error: "user@@example.com" -> Valid false
# ----------------------------
def validate_email_structure(email_text: str) -> dict:
    if email_text is None:
        return {"valid": False, "domain": "", "message": "Error: invalid input (none provided)"}

    email = email_text.strip()
    if not email:
        return {"valid": False, "domain": "", "message": "Error: invalid input (empty string)"}

    if " " in email:
        return {"valid": False, "domain": "", "message": "Error: invalid input (contains spaces)"}

    at_count = email.count("@")
    if at_count != 1:
        return {"valid": False, "domain": "", "message": "Valid email: false"}

    local_part, domain_part = email.split("@", 1)
    if not local_part or not domain_part or "." not in domain_part:
        return {"valid": False, "domain": "", "message": "Valid email: false"}

    return {"valid": True, "domain": domain_part.lower(), "message": "Valid email: true"}


# ----------------------------
# Problem 3: Palindrome checker (ignoring spaces and case)
# Description:
# Determine if a phrase is a palindrome, ignoring spaces and case.
#
# Inputs:
# - phrase (string)
#
# Outputs:
# - "Is palindrome: true" or "Is palindrome: false"
# - (Optional) Normalized version of phrase
#
# Validations:
# - phrase not empty after strip()
# - normalized length at least MIN_PALINDROME_CHARS
#
# Test cases:
# 1) Normal: "Anita lava la tina" -> true
# 2) Border: "aba" -> true
# 3) Error: "  " -> invalid input
# ----------------------------
def is_palindrome_phrase(phrase: str) -> dict:
    if phrase is None:
        return {"is_palindrome": False, "normalized": "", "message": "Error: invalid input (none provided)"}

    cleaned = phrase.strip()
    if not cleaned:
        return {"is_palindrome": False, "normalized": "", "message": "Error: invalid input (empty string)"}

    normalized = cleaned.replace(" ", "").lower()
    if len(normalized) < MIN_PALINDROME_CHARS:
        return {"is_palindrome": False, "normalized": normalized, "message": "Error: invalid input (too short after cleaning)"}

    is_pal = normalized == normalized[::-1]
    return {"is_palindrome": is_pal, "normalized": normalized, "message": f"Is palindrome: {str(is_pal).lower()}"}


# ----------------------------
# Problem 4: Sentence word stats (lengths and first/last word)
# Description:
# From a sentence compute: word count, first word, last word, shortest and longest word.
#
# Inputs:
# - sentence (string)
#
# Outputs:
# - "Word count: <n>"
# - "First word: <...>"
# - "Last word: <...>"
# - "Shortest word: <...>"
# - "Longest word: <...>"
#
# Validations:
# - sentence not empty after strip()
# - at least one valid word after split()
#
# Test cases:
# 1) Normal: "  The quick brown fox  " -> count 4, first "The", last "fox", shortest "The"/"fox", longest "quick"/"brown"
# 2) Border: "Hello" -> count 1, first "Hello", last "Hello"
# 3) Error: "    " -> invalid
# ----------------------------
def sentence_word_stats(sentence: str) -> dict:
    if sentence is None:
        raise ValueError("Error: invalid input (none provided)")

    cleaned = sentence.strip()
    if not cleaned:
        raise ValueError("Error: invalid input (empty string)")

    words = [w for w in cleaned.split() if w]
    if not words:
        raise ValueError("Error: invalid input (no words found)")

    word_count = len(words)
    first_word = words[0]
    last_word = words[-1]

    # Find shortest and longest (by length). If ties, first occurrence is taken.
    shortest = min(words, key=lambda s: len(s))
    longest = max(words, key=lambda s: len(s))

    return {
        "word_count": word_count,
        "first_word": first_word,
        "last_word": last_word,
        "shortest_word": shortest,
        "longest_word": longest
    }


# ----------------------------
# Problem 5: Password strength classifier
# Description:
# Classify password as 'weak','medium' or 'strong' using rules documented here:
# - Weak: length < 8 OR only one character class (e.g., all lowercase or digits only)
# - Medium: length >= 8 and at least two classes among {lower, upper, digit, special}
# - Strong: length >= 8 and at least three classes among {lower, upper, digit, special}
#
# Inputs:
# - password_input (string)
#
# Outputs:
# - "Password strength: weak/medium/strong"
#
# Validations:
# - password not empty
# - length checked with len()
#
# Test cases:
# 1) Normal: "Str0ngPass!" -> strong
# 2) Border: "password" -> weak (length 8 but only lowercase)
# 3) Error: "" -> invalid
# ----------------------------
def classify_password_strength(password_input: str) -> dict:
    if password_input is None:
        return {"valid": False, "strength": "invalid", "message": "Error: invalid input (none provided)"}

    pwd = password_input.strip()
    if not pwd:
        return {"valid": False, "strength": "invalid", "message": "Error: invalid input (empty string)"}

    length = len(pwd)
    has_lower = any(c.islower() for c in pwd)
    has_upper = any(c.isupper() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(not c.isalnum() for c in pwd)

    classes = sum([has_lower, has_upper, has_digit, has_special])

    if length < 8 or classes <= 1:
        strength = "weak"
    elif length >= 8 and classes == 2:
        strength = "medium"
    elif length >= 8 and classes >= 3:
        strength = "strong"
    else:
        # length >=8 but classes == 1 handled above; fallback:
        strength = "weak"

    return {"valid": True, "strength": strength, "message": f"Password strength: {strength}"}


# ----------------------------
# Problem 6: Product label formatter (fixed-width text)
# Description:
# Given product name and price, create a single-line label:
# "Product: <NAME> | Price: $<PRICE>"
# The label must be exactly LABEL_FIXED_LENGTH characters: pad with spaces to the right or trim to fit.
#
# Inputs:
# - product_name (string)
# - price_value (string or number)
#
# Outputs:
# - "Label: '<exactly 30 characters>'"
#
# Validations:
# - product_name not empty after strip()
# - price_value convertible to a positive number
#
# Test cases:
# 1) Normal: ("Widget", 12.5) -> e.g. "Product: Widget | Price: $12.5" padded to 30 chars
# 2) Border: ("LongProductNameThatExceedsWidth", 123456) -> trimmed to 30 chars
# 3) Error: ("   ", "free") -> invalid (name empty and price not positive-number)
# ----------------------------
def format_product_label(product_name: str, price_value) -> str:
    if product_name is None:
        raise ValueError("Error: invalid input (product name none)")

    name_clean = product_name.strip()
    if not name_clean:
        raise ValueError("Error: invalid input (product name empty)")

    # Validate price: try to convert to float and ensure non-negative
    try:
        price_num = float(price_value)
    except Exception:
        raise ValueError("Error: invalid input (price not a number)")

    if price_num < 0:
        raise ValueError("Error: invalid input (price must be non-negative)")

    # Build base label
    label_base = f"Product: {name_clean} | Price: ${price_num}"
    # Ensure exactly LABEL_FIXED_LENGTH chars
    if len(label_base) < LABEL_FIXED_LENGTH:
        label_fixed = label_base + " " * (LABEL_FIXED_LENGTH - len(label_base))
    else:
        label_fixed = label_base[:LABEL_FIXED_LENGTH]

    return label_fixed


# ----------------------------
# Run concrete test cases for each problem and print outputs
# ----------------------------
def run_tests():
    print("----- Problem 1 Tests -----")
    tests_p1 = [
        ("  juan   carlos tovar  ", "Normal"),
        ("Ana Maria", "Border"),
        ("   ", "Error")
    ]
    for val, tag in tests_p1:
        try:
            name, initials = format_name_and_initials(val)
            print(f"{tag} -> Formatted name: {name} ; Initials: {initials}")
        except Exception as e:
            print(f"{tag} -> {e}")

    print("\n----- Problem 2 Tests -----")
    tests_p2 = [
        ("User@example.com", "Normal"),
        ("a@b.c", "Border"),
        ("user@@example.com", "Error")
    ]
    for val, tag in tests_p2:
        res = validate_email_structure(val)
        if res["valid"]:
            print(f"{tag} -> Valid email: true ; Domain: {res['domain']}")
        else:
            print(f"{tag} -> {res['message']}")

    print("\n----- Problem 3 Tests -----")
    tests_p3 = [
        ("Anita lava la tina", "Normal"),
        ("aba", "Border"),
        ("   ", "Error")
    ]
    for val, tag in tests_p3:
        res = is_palindrome_phrase(val)
        if res["message"].startswith("Error"):
            print(f"{tag} -> {res['message']}")
        else:
            print(f"{tag} -> {res['message']} ; Normalized: '{res['normalized']}'")

    print("\n----- Problem 4 Tests -----")
    tests_p4 = [
        ("  The quick brown fox  ", "Normal"),
        ("Hello", "Border"),
        ("    ", "Error")
    ]
    for val, tag in tests_p4:
        try:
            stats = sentence_word_stats(val)
            print(f"{tag} -> Word count: {stats['word_count']}, First: {stats['first_word']}, Last: {stats['last_word']}, Shortest: {stats['shortest_word']}, Longest: {stats['longest_word']}")
        except Exception as e:
            print(f"{tag} -> {e}")

    print("\n----- Problem 5 Tests -----")
    tests_p5 = [
        ("Str0ngPass!", "Normal"),
        ("password", "Border"),
        ("", "Error")
    ]
    for val, tag in tests_p5:
        res = classify_password_strength(val)
        if not res["valid"]:
            print(f"{tag} -> {res['message']}")
        else:
            print(f"{tag} -> {res['message']}")

    print("\n----- Problem 6 Tests -----")
    tests_p6 = [
        (("Widget", 12.5), "Normal"),
        (("LongProductNameThatExceedsWidth", 123456), "Border"),
        (("   ", "free"), "Error")
    ]
    for (name, price), tag in tests_p6:
        try:
            label = format_product_label(name, price)
            # Show between quotes to visualize padding/trimming
            print(f"{tag} -> Label: '{label}' (len={len(label)})")
        except Exception as e:
            print(f"{tag} -> {e}")


if __name__ == "__main__":
    run_tests()

# ----------------------------
# Conclusions (5-8 lines) - comments:
#
# String handling is essential for robust data entry and output formatting in real systems.
# Use strip() to remove accidental whitespace and lower()/title() to normalize content before comparisons.
# split()/join() are useful for tokenization and reconstruction; slicing helps when fixed-width formats are required.
# Normalization prevents mismatch errors (e.g., comparing "Email@Example.com" with "email@example.com").
# Validations (non-empty -> format -> content) prevent garbage data and make error handling predictable.
# Strings are immutable: each operation returns a new string, so avoid excessive copies in tight loops.
# Proper use of named constants (not magic numbers) and clear messages improves maintainability.
#
# References (minimum 5) - comments:
# References:
# 1) Python documentation - Built-in Types: Text Sequence Type — str. https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# 2) Python docs - str methods. https://docs.python.org/3/library/stdtypes.html#string-methods
# 3) Real Python - Working with Strings in Python. https://realpython.com/python-strings/
# 4) GeeksforGeeks - String Handling in Python. https://www.geeksforgeeks.org/python-strings/
# 5) Stack Overflow - community Q&A for practical string problems. https://stackoverflow.com/
#
# Repository (replace with your repo):
# https://github.com/yourusername/your-repo
#
# Delivery checklist:
# - [ ] File named as: matricula_ApellidoNombre_t_strings.py
# - [ ] Portada fields replaced with actual name, matricula, group
# - [ ] Executive summary present
# - [ ] Problems 1..6 implemented with Description, Inputs, Outputs, Validations, 3 test cases each
# - [ ] Conclusions and References included
# - [ ] Run the script to verify the printed test outputs before submission
#
# End of file.
