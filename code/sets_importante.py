Union
El resultado de combinar todos los elementos de dos sets

my_set1 = { 3, 4, 5}
my_set2 = { 5, 6, 7}

my_set3 = my_set1 | my_set2
print(my_set3)

# {3, 4, 5, 6, 7}
se usa el operador | para combinar sets

intersección
Combinar ambos sets y quedarme solo con los que tienen elementos en común

my_set1 = { 3, 4, 5}
my_set2 = { 5, 6, 7}

my_set3 = my_set1 & my_set2
print(my_set3)
#{5}
se usa el & para que se intercepten

Diferencia
La diferencia es el resultado de tomar 2 sets y de uno quitar los elementos que tiene el otro. usamos el operador -

my_set1 = { 3, 4, 5}
my_set2 = { 5, 6, 7}

my_set3 = my_set1 - my_set2
my_set4 = my_set2 - my_set1
print(my_set4)

# {3,4}
# {6,7}
Diferencia simétrica
Lo contrario de la intercepción. Me quedo con los elementos que
no se comparten entre los dos sets. se usa el operador ^

my_set1 = { 3, 4, 5}
my_set2 = { 5, 6, 7}

my_set3 = my_set1 ^ my_set2
print(my_set3)

#{3,4,6,7}
