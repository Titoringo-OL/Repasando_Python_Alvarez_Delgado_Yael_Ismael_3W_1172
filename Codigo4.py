print("Alvarez Delgado Yael Ismael 3W 1172")
print(" ")
# Lista con las notas
notas = [7.5, 9, 6, 8.5, 4, 3.2, 10]  

# Comprobamos si la lista de notas no está vacía
if notas:
    # Encontramos la nota más baja utilizando la función min()
    n_b = min(notas)
    
    # Encontramos la nota más alta utilizando la función max()
    n_a = max(notas)
    
    # Imprimimos la nota más baja y la más alta
    print("La nota más baja es:", n_b)
    print("La nota más alta es:", n_a)
else:
    # Si la lista de notas está vacía, se muestra un mensaje de advertencia
    print("La lista de notas está vacía.")
