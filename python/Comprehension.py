squares = [x+1 for x in range(1,11)]
print("Los cuadrados: ",squares)

celsius = [0,10,20,30,40]
fahremheit =[((9/5)*x)+32 for x in celsius ]

print(len(celsius))
print(fahremheit)

evens = [x for x in range(1,20) if x%2==0]
print(evens)


matrix =[[1,2,3],
         [4,5,6],
         [7,8,9]]


transposed =[[row[i] for row in matrix] for i in range (len(matrix[0]))]