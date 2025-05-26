# and, or, not

# and ambas variables deben ser true
# or al menos una debe ser true
# not cambia el valor de la variable seleccionada, invierte el valor

gas = False
encendido = True
edad = 18

# if gas or encendido:
#     print("Puedes avanzar")
#######################################################################
# En este caso se ejecutan las condiciones de los parentesis primero
# if not gas and (encendido and edad > 17):
#     print("Puedes avanzar")

# else:
# Si no se cumple la condición se ejecuta este bloque
#   print("No puedes avanzar")
#########################################################################

# en este caso ocupamos la operación de corto circuito, dependiendo del operador en este caso and en caso que la condición
# de la izquierda la primera fuera falsa no se siguen ejecuntando el resto de las condiciones en caso de grandes operaciones
# esta nos podria ahorrar tiempo de ejecución
if not gas and encendido and edad > 17:
    print("Puedes avanzar")
