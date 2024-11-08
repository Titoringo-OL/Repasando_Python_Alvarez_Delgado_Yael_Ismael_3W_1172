print("Alvarez Delgado Yael Ismael 3W 1172")
print(" ")
# Se almacena la nota en una variable
nota = 10  # Puedes cambiar este valor para probar con diferentes notas

# Comprobamos en qué rango de notas se encuentra
if 0 <= nota < 5:
    # Si la nota es mayor o igual a 0 y menor que 5
    print("SUSPENSO")
elif 5 <= nota < 6:
    # Si la nota es mayor o igual a 5 y menor que 6
    print("SUFICIENTE")
elif 6 <= nota < 7:
    # Si la nota es mayor o igual a 6 y menor que 7
    print("BIEN")
elif 7 <= nota < 9:
    # Si la nota es mayor o igual a 7 y menor que 9
    print("NOTABLE")
elif 9 <= nota <= 10:
    # Si la nota es mayor o igual a 9 y menor o igual a 10
    print("SOBRESALIENTE")
else:
    # Si la nota no está en ningún rango válido
    print("NOTA NO VÁLIDA")
