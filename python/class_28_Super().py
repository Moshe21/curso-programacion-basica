class person:
    def __init__(self,name, age):
        self.name =name
        self.age = age
    
    def greet(self):
        print(f'hola,mi nombre es {self.name}')
        print(f'tengo {self.age} años')

person1 = person("ana",16)
person2 = person("carlo",20)

person1.greet()
person2.greet()