"""
slicing a list
"""
jojos_bizarre_adventures = ["Jonathan", "Joseph", "Jotaro", "Josuke", "Giorno Giovanna"]
print("original", jojos_bizarre_adventures)
print("\n")
print("slicing", jojos_bizarre_adventures[1:4])  # Output: ['Joseph', 'Jotaro', 'Josuke']
print("\n")
print ("slice", jojos_bizarre_adventures[1:4])
print("\n")
print("Slice", jojos_bizarre_adventures[:4])
print("\n")
print("SLICE", jojos_bizarre_adventures[2:])
print("\n")
print("slice", jojos_bizarre_adventures[-3:])
print("\n")
print("Slice", jojos_bizarre_adventures[5:])

# slicing en un for

jojos_bizarre_adventures = ["Jonathan", "Joseph", "Jotaro", "Josuke", "Giorno Giovanna"]
print ("aqui se presentan los primeros tres jojos")
for jojo in jojos_bizarre_adventures[:3]:
    print(jojo.title())
print("\n")

# copiando una lista

jojos_bizarre_adventures = ["Jonathan", "Joseph", "Jotaro", "Josuke", "Giorno Giovanna"]
# jojos_2 = players <- ERROR asi no se copia una lista
jojos_2 = jojos_bizarre_adventures[:]
print (jojos_2)

jojos_3 = list(jojos_bizarre_adventures)
print ( jojos_3)
jojos_4 = jojos_bizarre_adventures.copy()
print (jojos_4)


