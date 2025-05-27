# numero = 1
# while numero < 100:
#     print(numero)
#     numero *= 2 # el resultado lo va multiplicando por 2

# comando = ""

# while comando.lower() != "salir":  # el comando se convierte a minusculas en caso de usar minusculas en el string
# tomamos por consola el valor ingresado por el usuario
#    comando = input("$ ")
# comando = input("¿Qué deseas hacer? ")
#    print(comando)

############################# Loops infinito ###########################
# comando = ""

# while True:
#     comando = input("$ ")
#     print(comando)
############################# Loops infinito ###########################
# comando = ""

while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break
