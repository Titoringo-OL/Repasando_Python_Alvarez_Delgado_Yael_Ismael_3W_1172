print("Alvarez Delgado Yael Ismael 3W 1172")
print(" ")
# Nombre y apellido en dos variables diferentes
n = "Yael"  
a = "Alvarez" 

# Comprobamos si el nombre es el correcto
if n == "Yael":
    # Si el nombre es correcto, se comprueba si el apellido tambien es correcto
    if a == "Alvarez":
        # Si el apellido es corrcto, se imprime que el nombre y apellido son correctos
        print("Nombre y apellido correctos.")
    else:
        # Si el nombre es correcto pero el apellido no, se imprime que el apellido es incorrecto
        print("Apellido incorrecto.")
else:
    # Si el nombre no es correcto, se imprime que el usuario es desconocido
    print("Usuario desconocido.")
