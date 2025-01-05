"""nombre = input("ingrese su nombre:")
print(nombre)
edad=int(input('cuantos años tienes'))
print(edad)
print(type(edad))
"""
list_mix=['hello',1,1.23,["manzana","banana","pero",1]]

print(list_mix[-1])
print(type(list_mix[-1]))
""""
frase_list='hello wordlz'
print(frase_list[0])
print(frase_list[1])
print(frase_list[-1])
"""

#print(list_mix[2:])

list_mix.insert(4,['a','b','c'])
print(list_mix)

print(len(list_mix))
print(list_mix.index(False))

numeros=[5,4,86,54,2,62,15]
print('el numero mayor es:',max(numeros))
print('el numero menor es:',min(numeros))

del list_mix[5]

del list_mix[:2]

print(list_mix)

del numeros
print(numeros)