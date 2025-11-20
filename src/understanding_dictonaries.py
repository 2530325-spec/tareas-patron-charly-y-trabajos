#simple dictionary
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print("\n")

#the simpliest dictiomary
alien_1 = {}
alien_1 = {'color':'yellow'}
print(alien_1['color'])
print(alien_0['points'])
print("\n")

# empty dictionary
alien_2 = {}


# modifying key-value pairs to a dictionary
alien_2 = {'color':'yellow'}
alien_2['color'] = 'blue'




# adding new key-value pairs
alien_2['x_position'] = 0
alien_2['y_position'] = 25
print (alien_2)


print("\n")

## Dictionary to store similar objects
favorite_languages = {
    'jen': 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'

}
print(f"sarah favorite laguage is {favorite_languages['sarah']}")
print("\n")

#looping through all key-value pairs
for key , value in favorite_languages.items():
    print(f"{key.title()}'s favorite \
languafe is {value.title()}. ")