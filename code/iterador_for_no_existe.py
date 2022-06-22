# Creando un iterador

my_list = [1,2,3,4,5]
my_iter = iter(my_list)

# Iterando un iterador

print(next(my_iter))

# Cuando no quedan datos, la excepción StopIteration es elevada
# Creando un iterador

my_list = [1,2,3,4,5]
my_iter = iter(my_list)

# Iterando un iterador

while True: #ciclo infinito
  try:
    element = next(my_iter)
    print(element)
  except StopIteration:
    break
Momento impactante: El ciclo “for” dentro de Python, no existe. Es un while con StopIteration. 🤯🤯🤯

my_list = [1,2,3,4,5]

for element in my_list:
  print(element)
