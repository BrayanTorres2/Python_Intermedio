Closures
Nested functions: Las funciones anidadas son simplemente funciones creadas dentro de otra funci贸n. Podemos hacer return de una funci贸n creada dentro de otra funci贸n 馃樀 y luego guardar esas funciones en variables que podemos utilizar.

def main():
	a = 1
	def nested():
		print(a)
	return nested

my_func = main()
my_func()
# 1
Eso anterior es un closure 馃く y es b谩sicamente cuando una variable de un scope superior es recordada por una funci贸n de scope inferior (aunque luego se elimine la de scope superior).

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
Reglas para encontrar un closure: 馃敟

Debemos tener una nested function.
La nested function debe referenciar un valor de un scope superior.
La funci贸n que envuelve a la nested function debe retornarla tambi茅n.
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
Los closure aparecen en dos casos particulares: cuando tenemos una clase corta (con un solo m茅todo), los usamos para que sean elegantes. El segundo caso, es cuando usamos decoradores 馃憖
