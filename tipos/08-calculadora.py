n1 = input("Ingresa primer número: ")
n2 = input("Ingresa segundo número: ")

n1 = int(n1)  # Con esto transformamos el string a número
# Considerar que si se ingresa string palabras no se pueden convertir a números
n2 = int(n2)

# print(n1, n2)  # En este momento no esta mostrando los datos ingresados como string
# En este momento no esta mostrando los datos ingresados como string y en los concatena
# print(n1 + n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
Para los números {n1} y {n2},
el resultado de la suma es: {suma}.
el resultado de la resta es: {resta}.
el resultado de la multiplicación es: {multi}.
el resultado de la división es: {div}.
"""
print(mensaje)
