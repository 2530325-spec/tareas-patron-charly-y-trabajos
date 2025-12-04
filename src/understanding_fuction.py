def greetting_paulo():
    """
    docstring for greetting_paulo
    esta funcion saluda a paulo
    """
    print ("hello paulo")



    """
    vamos a hacer una funcion que pida al usuarii
    first_naame, middle_name, Last_name

    la funcion debe regresar el nombre completo
    """
    # la funcion tiene 3 parametros
def create_full_name(first_name, last_name, middle_name= ""):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name
user_first_name = input("escribe tu primer nombre:").strip().lower()
user_middle_name = input("escribe tu segundo nombre: ").strip().lower()
user_last_name = input("escribe tu apellido: ").strip().lower()

# argumentos 
print(create_full_name(user_first_name, user_middle_name, user_last_name).title())
# argumentos posicionales - positional arguments
generated_full_name = create_full_name(
    user_first_name,
  user_middle_name, 
   user_last_name).title()
print (generated_full_name)

# args, kwargs
"""
cosas para estudiar en python

        explorar archivos(Diccionarios, txt, csv)
        args por consolo(sys)
        cli -command linear interface
        generadores
        intenadores
        gils
        oop - oriented objects programming
        testing
        imports y como instalar modulo de python

"""
