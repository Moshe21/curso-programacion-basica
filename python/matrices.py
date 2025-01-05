image = [
    [255, 0, 0, 0, 255],
    [0, 255, 0, 255, 0],
    [0, 0, 255, 0, 0],
    [0, 255, 0, 255, 0],
    [255, 0, 0, 0, 255]
]


print(image)
libros_numeros= {1:"uno", 2:"dos",3:"tres"}
print(libros_numeros)

informacion={"nombre":"carla",
            "apellido":"FLORIDA",
            "altura": {1.60,}, 
           "edad": 26}
print (informacion)

del informacion['edad']
print(informacion)
claves=informacion.keys()
print(type(claves))
Values=informacion.values()
print(Values)
pairs=informacion.items()
print(pairs)

contacts={"Carla":{
                    "apellido":"FLORIDA",
                    "altura": {1.60,}, 
                    "edad": 26},
           
           "Mario":{
                    "apellido":"meta",
                    "altura": {1.80,}, 
                    "edad": 17},
           
           "Estefani":{
                    "apellido":"villao",
                    "altura": {1.50,}, 
                    "edad": 28}
}
print(contacts)