"""un string es de manera sencilla una serie de caracteres

    en pyhton todo lo que se ENCUENTRE DENTRO DE COMILLAS
    SIMPLES '' O DOBLES COmillAS "" es considerado un STRING


    Por ejemplo:
        "estro es un string"
        'esto tambien es un string'
        'le dige a mi amigo pablo "como que eres puñal !!!!"

        "el lenguaje 'PYTHON' kkeva el nombre en honor a Monty Python , no por la serpiente"

"""

# STRINGS

name = "clase de programaciom"
print()
print (name)
print()
print (name.title())
print()
print(name)
print()


"""
    un metodo es una accion que python  
    puede realizar en un fragmento de 
    datos o sobre una variable

    El punto (.) despues de una variable string 
    seguid del metodo tittle() dice que 
    se tiene que ejecutar el metodo tittle () de 
    la variable name.

    todos los metodos van segiidos de parentesis
    por que en ocasiones encesitan informacion
    adicional para funcionar , lo caul iria dentro
    de los parentesis

    en esta ocasion el metodo .title () no requiere 
    informacion adivional para ejecutarse.
"""

# OTROS METODOS

print ("para mayusculas :", name.upper())
print ("para mayusculas :", name.lower())



# CONCATENACION DE STRINGS

first_name = "Epigmenio"
last_name = "de la cruz"
full_name = first_name + "" + last_name

print (full_name)
print ("Hola " , "!" + full_name.title() + "!")

message = "Hola " , "!" + full_name.title() + "!"

print (message)



#WHITESPACES
"""
    Whitespace se refiere a cualquier caracter 
    que no se imprime, es decir, un espacio en blanco
    un tabulador o un salto de linea. Los whitespaces
    se utiliza comunmente para organizar las salidas
    en pantalla de tal manera que sea mas amigable de 
    leer o ver para los usuarios
"""

print("python")
print("\tpython") # tabulador antes de python
print("\t\tpython")# tabulador antes de python
print("languages: \n\tpython\n\tJava\n\tJavaScripts")# salto de linea



# Eliminacion de WHIESPACE
print("\n\n ELIMINACION DE ESPACIOS EN BLANCO")
favorite_language = " python "

print(favorite_language)

print(favorite_language.rstrip())

print(favorite_language.lstrip())

print(favorite_language.strip())

# Syntax Error con strings

print("\n\nSyntax Error con Strings")

message = 'Una fortaleza de python es su comunidad activa'

print(message)
# un syntax error seria message = 'una fortaleza de "python"es su comunidad activa'

message = 'una fortaleza de "python"es su comunidad activa'

print (message)

