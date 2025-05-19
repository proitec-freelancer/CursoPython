animal = " ChanCHito feliz "

# Transforma nuestro string en mayusculas con el metodo upper()
print(animal.upper())
# Transforma nuestro string en minusculas con el metodo lower()
print(animal.lower())
# Tranforma el primer caracter de nuestro string en mayuscula con el metodo capitalize() y todo el resto lo deja en minuscula
print(animal.strip().capitalize())
# Tambien se pueden encadenar los metodos.
# Transforma todos los primeros caracteres de nuestro string en mayuscula con el metodo title()
print(animal.title())
# Remueve el primer espacio y el ultimo espacio del ultimo string
print(animal.strip())
print(animal.lstrip())  # Quita los espacios de la derecha
print(animal.rstrip())  # Quita los espacios de la izquierda
# Sirve para colocar comillas simples y llaves a las palabras de un string separado
# print(animal.split())
# Busca un criterio y devuelve su indice, si arroja número negativo es por que no lo encontro
print(animal.find("CH"))
# Reemplaza un caracter o palabra por otro, necesita minimo 2 argumentos.
print(animal.replace("nCH", "j"))
# Busca el criterio en caso de encontrarlo devuelve True, en caso de no encontrarlo devuelve False.
print("nCH" in animal)
print("nCH" not in animal)  # En caso de no encontrar el criterio devuelve true
