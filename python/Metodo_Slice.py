a = [1,2,3,4,5]
b = a
print(a)
print(b)
del a[5]

print(id(a))
print(id(b))
print(a)
print(b)
c = a [:]
print(id(c))
print(c)
a.append(6)
print(a)
print(b)
print(c)

print(type(d))

d=(1,2,3,4,5)

d.append(6)
del d(0)
del d