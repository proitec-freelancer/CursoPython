nombre_curso = "Ultimate Python"
descripcion_curso = """
Ultima Python, 
Este curso comtempla todos los detalles que necesitas aprender
para encontar un trabajo como programador  
"""
print(nombre_curso, descripcion_curso)

# Mostramos por pantalla la longitud del string con la ṕalabra len
print(len(nombre_curso))

# Accedemos al indice 0 del string
print(nombre_curso[0])

# Separamos o cortamos desde el indice 0 del string hasta el indice 8 que en este caso seria ultimate
print(nombre_curso[0:8])

# Accede desde el indice 9 como no definimos el indice , llegara hasta el finaal
print(nombre_curso[9:])

# En este caso le dimos en indice final , pero no del inicio python asume el valor por defecto que es 0
print(nombre_curso[:8])

# como no definimos los indices toma la longitud completa del string
print(nombre_curso[:])
