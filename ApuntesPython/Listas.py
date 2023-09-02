

# las listas son estructuras de datos lineales
# Se crean usando brackes ej: my_list = []
# las listas son ordenadas (Orden de insersion), esto quiere dicr
# que el ultimo dato ingresado ocupará la ultima posición.
# Emplea métodos para manipular los items de la misma.
# Como los array la primera posicion inicia en 0
# Permite items duplicados.
# Las listas son mutables, es decir podemos agregar , actualizar o remover items
# Puede contener distintos tipos de datos


nombres = ["Juan", "Pepito", "Maria", "Lisa"]

# len() valida el tamaño de la lista.
print(len(nombres))
print(type(nombres))

listaDatos= ["Pepito", "Perez", 1000100100,1.80,True]

print(f"El Numero de doc es: {listaDatos[2]}")

# Slicing de datos 
print(listaDatos[0:2])
print(listaDatos[1:4])
print(listaDatos[:4])
print(listaDatos[2:])

print(listaDatos[:-1])
print(listaDatos[:-2])
print(listaDatos[-4:-1])
print(listaDatos[1:4])

