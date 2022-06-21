Closures
Nested functions: Las funciones anidadas son simplemente funciones creadas dentro de otra función. Podemos hacer return de una función creada dentro de otra función 😵 y luego guardar esas funciones en variables que podemos utilizar.

def main():
	a = 1
	def nested():
		print(a)
	return nested

my_func = main()
my_func()
# 1
Eso anterior es un closure 🤯 y es básicamente cuando una variable de un scope superior es recordada por una función de scope inferior (aunque luego se elimine la de scope superior).

def main():
	a = 1
	def nested():
		print(a)
	return nested

my_func = main()
my_func()
# 1
del(main)
my_func()
# 1
Reglas para encontrar un closure: 🔥

Debemos tener una nested function.
La nested function debe referenciar un valor de un scope superior.
La función que envuelve a la nested function debe retornarla también.
Ejemplo de closures para crear funciones:

def make_multiplier(x):
	def multiplier(n):
		return x*n
	return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3)) # 30
print(times4(5)) #20
print(times10(times4(2))) # 80
Los closure aparecen en dos casos particulares: cuando tenemos una clase corta (con un solo método), los usamos para que sean elegantes. El segundo caso, es cuando usamos decoradores 👀
