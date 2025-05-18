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
# Sirve para colocar comillas simples y llaves a las palabras de un string separado
print(animal.rstrip())
print(animal.lstrip())
print(animal.rsplit())
