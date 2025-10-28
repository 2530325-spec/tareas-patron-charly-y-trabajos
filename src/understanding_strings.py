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