def decorador(func):
    def envoltura():
        print("Esto se añade a mi función original.")
        func()
    return envoltura

def saludo():
    print("¡Hola!")

saludo()
# Salida:
# ¡Hola!

saludo = decorador(saludo) # Se guarda la función decorada en la variable saludo
saludo()                   # La función saludo está ahora decorada
# Salida:
# Esto se añade a mi función original.
# ¡Hola!



#------------------------------------------------------------------------ otra forma de hacerlo
@decorador# azucar de sintaxis, o azucar sintactica 
def saludo():
    print("¡Hola!")
    
saludo()
# Salida:
# Esto se añade a mi función original.
# ¡Hola!
