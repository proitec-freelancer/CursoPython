# for numero in range(5):  # 0, 1, 2, 3, 4 recorre e imprime los indices
#     print(numero)


# for numero in range(5):  # 0, 1, 2, 3, 4 recorre e imprime los indices
#     print(numero, numero * 'hola mundo ')

######################################################################################
# buscar = 3

# for numero in range(3):  # 0, 1, 2, 3, 4 recorre e imprime los indices
#     if numero == buscar:
#         print("Encontrado", buscar)

#######################################################################################

# buscar = 3

# for numero in range(6):  # 0, 1, 2, 3, 4 recorre e imprime los indices
#     print(numero)
#     if numero == buscar:
#         print("Encontrado", buscar)
#         break

#########################################################################################

buscar = 10

for numero in range(5):  # 0, 1, 2, 3, 4 recorre e imprime los iterables y las listas y tuplas
    print(numero)
    if numero == buscar:
        print("Encontrado", buscar)
        break

else:
    print("No encontré el número buscado xC")


###########################################################################################

for char in "Ultimate python":
    print(char)
