
age=0
try:
     age = int(input("dime tu edad: "))
except Exception as err:
    print(err)


if age <= 4 :
    print("pasas gratis")
elif age >= 18 and age < 65 :
    print("el precio de tu boleto son $500")
elif age > 4 and age < 18 :
    print("el precio de tu boleto es $200")
elif age >= 65 :
    print("traete a tu abuelo y pasas gratis")