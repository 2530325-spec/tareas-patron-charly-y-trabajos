

# If statement 
"""
    programa para pedir la edad a un usuario
    que diga si el usario es menor de edad 
    o mayor de edad
"""



#try: except:
age = 0
try:
    age = int(input("dime tu edad: "))

except Exception as err:
    print(err)
#if-elif-else
if age>=18 and age <=100 :
    print("puto viejo ya jubilate")
    print("no le sirves al epstein")
elif age <18 and age>0 :
    print("Eres menor mi todo botsita")
    print("le sirves a epstein cuidado")
elif age>100 :
    print("tienes mas de un siglo vivo :v")
elif age < 0 :
    print("estas en los huevos de tu jefe o que")

 