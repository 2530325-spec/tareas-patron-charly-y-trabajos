"""
    las tuplas son listas de elementos
    que no cambian de tamaño. Las tuplas son
    listas multiples.

    Se utilizan los () para definir una tupla.
    o la palabras reservada tuple()

    si tenemos un rectangulo que siempre va a tener
    cierto tamaño, podemos asegurar que su tamaño
    no va a  cambiar si colocamos sus valoresen 
    una tupla.
    
    """

# ejemplo de tuplas

dimensions = (200,50)
print (dimensions)
print(dimensions[0])
print(dimensions[1])

# dimensions[0]=300 #no se puede #type error

for dimension in dimensions:
    print(dimension)



"""
    No podemos modificar una tupla directamente, 
    lo que si podemos hacer es cambiar la 
    asignacion a una variable que almacena una
    tupla
"""
dimensions = (200,50)
print(dimensions)

dimensions= (400,50,40)
print (dimensions)
