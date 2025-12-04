# PORTADA
# ================================================================
# Name: Escobar Carrizales Victor
# Matriculation: 2530325
# Group: 103 
#   In this file, i have to create diferents
#   code for the correct use of strings 
#   using functions and methods.


# what's a string?

"""

What's a string ?
             in python a string is any character 
             between ¨¨ or '' it can be numbers or letters
             What basic operations can be performed?

             With strings, you can use concatenation, but the most common option is f strings,
             which is used to join text, real numbers, floats, or complex numbers.
             We can also use methods that define any text;
             these are also very useful for normalizing text, as they include:
             uppercase: makes all letters uppercase
             lowercase: the opposite, makes all letters lowercase
             title: makes the first letter uppercase and the rest lowercase
             strip: removes whitespace from the text; typing it just like this removes all spaces,
             but there's also rstrip which removes only the spaces on the right side,
             and lstrip which removes the whitespace on the left side
             lenghth: counts the number of characters in the string.

"""
 
# firts code: full name formater (Name+Initials)
"""

in this code i have to use the input, eliminate the white spaces, use the method title and with that 
write the name with title and the initials

"""


def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value.title()
        else:
            print("Empty input is not allowed. Try again.\n")

def full_name(first_name, middle_name, last_name1, last_name2):
    full_name = f"{first_name} {middle_name} {last_name1} {last_name2}"
    return full_name  

first_name = get_non_empty("Put your first name: ")
middle_name = get_non_empty("Put your middle name: ")
last_name1 = get_non_empty("Put your first last name: ")
last_name2 = get_non_empty("Put your second last name: ")

Initials = f"{first_name[0]}. {middle_name[0]}. {last_name1[0]}. {last_name2[0]}."

Name = full_name(
    first_name,
    middle_name,
    last_name1,
    last_name2
)

print("Your full name is: " + Name)
print("Your initials: " + Initials)

"""
in the next progam we have to check if the 
string that the user user bring to us have a @ and a . after this
if the string count with this two we have to show the full email and 
the domain and print this too


""""""
# in the next code i have to check a string 

"""
_________________________________________________________________________________________________________________
_________________________________________________________________________________________________________________



def check_email():
    email = input("Enter your email: ")

    if email.strip() == "":
        print("Email cannot be empty or only spaces.")
        return
    email = email.strip()

    if " " in email:
        print("Spaces are not allowed in the email.")
        return
    at_count = email.count("@")
   
    if at_count != 1:
        print("Email must contain exactly one '@'.")
        return
    
    Position_Domain = email.find("@")

    domain = email[Position_Domain + 1:]

    if "." not in domain:
        print("The domain doesn't contain a dot.")
        return

    print("Full email: ", email)
    print("Domain: ", domain)
    print("Number of '@' symbols: ", at_count)
check_email()

"""
the check in this has been done with the use of "for"
because for is a check of any of the conditions  i put it will show or do the thing i do and 
if the string pass go to a return to continue checking the next.
"""

"""
_______________________________________________________________________________________________________________
_______________________________________________________________________________________________________________

"""
# palindrome checker 

""" 
in this code i have to check if any string write going backwards 
is the same text that write in the right way 
with that check 
show with a print if the text is palindrome or not 
and optional print the normalize text 
"""

def check_palindrome(phrase):
    if phrase.strip() == "":
               print("Error: The phrase cannot be empty.")
               return
    
    normalize_text = phrase.lower().replace(" ", "")

    if len(normalize_text) < 3:
     print("Error: The phrase must have at least 3 characters after cleaning.")
     return

    is_palindrome = normalize_text == normalize_text[::-1]

    print(f"Normalized phrase: {normalize_text}")
    print(f"Is palindrome: {is_palindrome}")


text = input("Enter a phrase: ")
check_palindrome(text)

"""

______________________________________________________________________________________________________

______________________________________________________________________________________________________

"""

#Sentence word stats (lengths and first/last word)
sentence = input("Enter a sentence: ")


if sentence.strip() == "":
    print("it cant be empty what's up")
else:

 words = sentence.strip().split()
if len(words) == 0:
 print("Error: The sentence must contain at least one valid word.")
else:
 word_count = len(words)

first_word = words[0]
last_word = words[-1]
shortest_word = min(words, key=len)
longest_word = max(words, key=len)

print(f"Word count: {word_count}")
print(f"First word: {first_word}")
print(f"Last word: {last_word}")
print(f"Shortest word: {shortest_word}")
print(f"Longest word: {longest_word}")

# in this code i have something that can i name as a error and 
# that is that is any two words that have the same quantity of letters 
# the code only will show one word 

"""

______________________________________________________________________________________________________________
______________________________________________________________________________________________________________

""""""

______________________________________________________________________________________________________

______________________________________________________________________________________________________

"""

#Sentence word stats (lengths and first/last word)

sentence = input("Enter a sentence: ")


if sentence.strip() == "":
    print("it cant be empty what's up")
else:

 words = sentence.strip().split()
if len(words) == 0:
 print("Error: The sentence must contain at least one valid word.")
else:
 word_count = len(words)

first_word = words[0]
last_word = words[-1]
shortest_word = min(words, key=len)
longest_word = max(words, key=len)

print(f"Word count: {word_count}")
print(f"First word: {first_word}")
print(f"Last word: {last_word}")
print(f"Shortest word: {shortest_word}")
print(f"Longest word: {longest_word}")

# in this code i have something that can i name as a error and 
# that is that is any two words that have the same quantity of letters 
# the code only will show one word 

"""

______________________________________________________________________________________________________________
______________________________________________________________________________________________________________

"""
### password strenght 

password_input = input("Enter your password: ")

if password_input.strip() == "":
    print("it can't be empty")
else:

    length = len(password_input)

    has_upper = False
    has_lower = False
    has_digit = False
    has_alnum = False

    for char in password_input:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

        if char.isalnum():
            has_alnum = True

    if length < 6:
        strength = "weak"
    elif length >= 6 and (has_upper or has_lower) and has_digit:
        strength = "medium"
    elif length >= 8 and has_upper and has_lower and has_digit and has_alnum:
        strength = "strong"
    else:
        strength = "weak"

    print(f"Password strength: {strength}")

    # in this code we can see the checks that if the password have atleast 6 digits on the string
    #the pasword is weak and if the password has the same number of letters but if the password
    # have a upper o lower and a digit it will be a medium strenght pass word 
    # and for the last to say that the password it have to have at least 8 digits on the string and 
    #pass a check that it coi¿ntain a upper, lower a number and a digit that its a verifier taht that what 
    #the code its checking its a string and with all of that the code will say that de code its strong 
 
"""

________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________

"""

product = input("Enter product name: ")
cost = input("Enter product price: ")


if product.strip() == "":
    print("Error: Product name cannot be empty.")
else:
    try:
        amount = float(cost)
        if amount <= 0:
            print("Error: Price must be a positive number.")
        else:
            toshow = str(amount)

            label = f"{product.strip()} - ${toshow}"

            if len(label) < 30:
                label = label + " " * (30 - len(label))
            else:
                label = label[:30]

            print(f'Label: "{label}"')

    except ValueError:
        print("Error: Price must be a valid number.")

"""
in this code we have to make thaht the product name should not be empty
and the price should be a positive number
i use the else and if for validate the for can't be empty 
any one of this 2 values, the conditionals 
will print an error message

"""

#
# _____________________________________________________________________________________________________
#________________________________________________________________________________________________________
#

"""

in this code we can see that in the use of strings 
normiliae and methods are basicly needed for do almopst anything 
beacause the user can write anything and sometimes that can make ur code fail
for that the methods like strip, lower , upper and title are very useful
because with them we can get a text without things we dont need 
and it its nota seen by the user it just help the code to work properly

"""

### 
####
###
# references
"""

https://youtu.be/CCUNuqqn7PQ?si=HltURE4xKIDyQjm9
https://youtu.be/9k91jETchkI?si=3jr1oLLRh44mghYe
https://youtu.be/Pr-9wkSJDJk?si=ekXXTMe1kblZUbZ_
https://youtu.be/OvafT2HL0uU?si=tbUWDtTrdG60q3xk
https://youtu.be/WSQvaPHsm64?si=EJurIIuAx-bDLgl5
https://youtu.be/tb6EYiHtcXU?si=pJIBO9-hqXKYw0_l

"""